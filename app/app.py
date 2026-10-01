from flask import Flask, request, redirect, url_for, render_template_string
import csv
import os
import json
from collections import Counter, defaultdict

app = Flask(__name__)

# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

DATA_FILE = os.path.join(DATA_DIR, "current_dataset.csv")


# ============================================================
# DEFAULT EMPTY DATASET
# ============================================================

DEFAULT_COLUMNS = [
    "race",
    "gender",
    "age",
    "admission_type_id",
    "discharge_disposition_id",
    "admission_source_id",
    "time_in_hospital",
    "num_lab_procedures",
    "diag_1",
    "diag_2",
    "diag_3"
]


# ============================================================
# DATA FUNCTIONS
# ============================================================

def normalize_row(row):
    """
    Makes uploaded CSV column names easier to work with.
    """

    clean = {}

    for key, value in row.items():

        if key is None:
            continue

        key = key.strip().lower()
        value = "" if value is None else str(value).strip()

        clean[key] = value

    return clean


def load_data():

    if not os.path.exists(DATA_FILE):
        return []

    try:

        with open(DATA_FILE, "r", encoding="utf-8-sig", newline="") as f:

            reader = csv.DictReader(f)

            rows = []

            for row in reader:
                rows.append(normalize_row(row))

            return rows

    except Exception:
        return []


def save_data(rows):

    if not rows:
        return

    # Keep all columns appearing anywhere in the dataset
    columns = []

    for row in rows:

        for key in row.keys():

            if key not in columns:
                columns.append(key)

    with open(DATA_FILE, "w", encoding="utf-8", newline="") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=columns,
            extrasaction="ignore"
        )

        writer.writeheader()

        for row in rows:

            writer.writerow(row)


def safe_int(value, default=0):

    try:
        return int(float(str(value).strip()))
    except Exception:
        return default


def safe_float(value, default=0):

    try:
        return float(str(value).strip())
    except Exception:
        return default


# ============================================================
# AGE CLEANING
# ============================================================

def clean_age(age):

    age = str(age).strip()

    if age.startswith("["):

        age = age.replace("[", "").replace(")", "").replace("]", "")

        parts = age.split("-")

        if parts:

            first = parts[0]

            if first.isdigit():
                return int(first)

    if age.isdigit():
        return int(age)

    return None


def age_group(age):

    age_number = clean_age(age)

    if age_number is None:
        return "Unknown"

    if age_number < 40:
        return "<40"

    if age_number < 60:
        return "40–59"

    if age_number < 70:
        return "60–69"

    if age_number < 80:
        return "70–79"

    return "80+"


# ============================================================
# DIAGNOSIS CLASSIFICATION
# ============================================================

def diagnosis_category(code):

    if not code:
        return "Other / Unclassified"

    code = str(code).strip().upper()

    # remove V and E style formatting
    try:

        number = float(code.replace("V", "").replace("E", ""))

    except Exception:
        return "Other / Unclassified"

    # ICD-9 ranges

    if 390 <= number <= 459 or number == 785:
        return "Circulatory Diseases"

    if 250 <= number < 251:
        return "Diabetes Complications"

    if 460 <= number <= 519 or number == 786:
        return "Respiratory Conditions"

    if 520 <= number <= 579 or number == 787:
        return "Digestive Disorders"

    if 580 <= number <= 629 or number == 788:
        return "Genitourinary Issues"

    if 710 <= number <= 739:
        return "Musculoskeletal Disorders"

    if 800 <= number <= 999:
        return "Trauma & Injury"

    if 140 <= number <= 239:
        return "Neoplasms / Oncology"

    return "Other / Unclassified"


# ============================================================
# ANALYTICS
# ============================================================

def build_analysis(rows):

    total = len(rows)

    if total == 0:

        return {
            "total": 0,
            "top_diagnosis": "No data",
            "top_race": "No data",
            "avg_stay": 0,
            "diagnosis": {},
            "gender": {},
            "race": {},
            "age": {},
            "admission_type": {},
            "admission_source": {},
            "diagnosis_stay": {}
        }

    # --------------------------------------------------------
    # Counters
    # --------------------------------------------------------

    diagnosis_counter = Counter()
    gender_counter = Counter()
    race_counter = Counter()
    age_counter = Counter()
    admission_type_counter = Counter()
    admission_source_counter = Counter()

    diagnosis_stay = defaultdict(list)

    total_stay = 0
    stay_count = 0

    # --------------------------------------------------------
    # Process every row
    # --------------------------------------------------------

    for row in rows:

        # Diagnosis
        diag = diagnosis_category(
            row.get("diag_1", "")
        )

        diagnosis_counter[diag] += 1

        # Gender
        gender = row.get("gender", "").strip()

        if not gender:
            gender = "Unknown"

        gender_counter[gender] += 1

        # Race
        race = row.get("race", "").strip()

        if not race:
            race = "Unknown"

        race_counter[race] += 1

        # Age
        age = age_group(
            row.get("age", "")
        )

        age_counter[age] += 1

        # Admission Type
        admission_type = row.get(
            "admission_type_id",
            ""
        ).strip()

        if not admission_type:
            admission_type = "Unknown"

        admission_type_counter[admission_type] += 1

        # Admission Source
        source = row.get(
            "admission_source_id",
            ""
        ).strip()

        if not source:
            source = "Unknown"

        admission_source_counter[source] += 1

        # Hospital stay
        stay = safe_float(
            row.get("time_in_hospital", "")
        )

        if stay > 0:

            total_stay += stay
            stay_count += 1

            diagnosis_stay[diag].append(stay)

    # --------------------------------------------------------
    # Percentages
    # --------------------------------------------------------

    def percentages(counter):

        result = {}

        for key, value in counter.items():

            result[key] = {
                "count": value,
                "percentage": round(
                    (value / total) * 100,
                    1
                )
            }

        return result

    # --------------------------------------------------------
    # Average stay by diagnosis
    # --------------------------------------------------------

    diagnosis_stay_avg = {}

    for diagnosis, values in diagnosis_stay.items():

        if values:

            diagnosis_stay_avg[diagnosis] = round(
                sum(values) / len(values),
                2
            )

    # --------------------------------------------------------
    # Final analysis
    # --------------------------------------------------------

    return {

        "total": total,

        "top_diagnosis":
            diagnosis_counter.most_common(1)[0][0]
            if diagnosis_counter else "N/A",

        "top_race":
            race_counter.most_common(1)[0][0]
            if race_counter else "N/A",

        "avg_stay":
            round(total_stay / stay_count, 2)
            if stay_count else 0,

        "diagnosis":
            percentages(diagnosis_counter),

        "gender":
            percentages(gender_counter),

        "race":
            percentages(race_counter),

        "age":
            percentages(age_counter),

        "admission_type":
            percentages(admission_type_counter),

        "admission_source":
            percentages(admission_source_counter),

        "diagnosis_stay":
            diagnosis_stay_avg
    }


# ============================================================
# MAIN DASHBOARD
# ============================================================

@app.route("/")
def dashboard():

    rows = load_data()

    analysis = build_analysis(rows)

    return render_template_string(
        DASHBOARD_HTML,
        analysis=analysis
    )


# ============================================================
# CSV UPLOAD
# ============================================================

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("csv_file")

    mode = request.form.get(
        "mode",
        "append"
    )

    if not file or file.filename == "":
        return redirect(url_for("dashboard"))

    try:

        content = file.read().decode(
            "utf-8-sig"
        )

        reader = csv.DictReader(
            content.splitlines()
        )

        uploaded_rows = []

        for row in reader:

            uploaded_rows.append(
                normalize_row(row)
            )

        if mode == "replace":

            save_data(uploaded_rows)

        else:

            current = load_data()

            current.extend(
                uploaded_rows
            )

            save_data(current)

    except Exception as e:

        print("UPLOAD ERROR:", e)

    return redirect(url_for("dashboard"))


# ============================================================
# PATIENT ENTRY PAGE
# ============================================================

@app.route("/patient-entry")
def patient_entry():

    return render_template_string(
        PATIENT_HTML
    )


# ============================================================
# ADD PATIENT
# ============================================================

@app.route("/add-patient", methods=["POST"])
def add_patient():

    row = {

        "race":
            request.form.get(
                "race",
                "Unknown"
            ),

        "gender":
            request.form.get(
                "gender",
                "Unknown"
            ),

        "age":
            request.form.get(
                "age",
                ""
            ),

        "admission_type_id":
            request.form.get(
                "admission_type_id",
                ""
            ),

        "discharge_disposition_id":
            request.form.get(
                "discharge_disposition_id",
                ""
            ),

        "admission_source_id":
            request.form.get(
                "admission_source_id",
                ""
            ),

        "time_in_hospital":
            request.form.get(
                "time_in_hospital",
                "0"
            ),

        "num_lab_procedures":
            request.form.get(
                "num_lab_procedures",
                "0"
            ),

        "diag_1":
            request.form.get(
                "diag_1",
                ""
            ),

        "diag_2":
            request.form.get(
                "diag_2",
                ""
            ),

        "diag_3":
            request.form.get(
                "diag_3",
                ""
            )
    }

    mode = request.form.get(
        "mode",
        "append"
    )

    if mode == "replace":

        save_data([row])

    else:

        current = load_data()

        current.append(row)

        save_data(current)

    return redirect(url_for("dashboard"))


# ============================================================
# CLEAR DATA
# ============================================================

@app.route("/clear-data", methods=["POST"])
def clear_data():

    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

    return redirect(url_for("dashboard"))


# ============================================================
# DASHBOARD HTML
# ============================================================

DASHBOARD_HTML = r"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Patient Health Intelligence</title>

<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>

<style>

*{
    box-sizing:border-box;
}

html,
body{
    margin:0;
    padding:0;
    background:#050807;
    color:#f5f7f6;
    font-family:
        Inter,
        Segoe UI,
        Arial,
        sans-serif;
}

/* =========================================================
   BODY
========================================================= */

body{

    min-height:100vh;

    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(0,255,180,.07),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(30,130,255,.06),
            transparent 25%
        ),
        #050807;
}


/* =========================================================
   HEADER
========================================================= */

.header{

    height:82px;

    padding:
        0 32px;

    display:flex;

    align-items:center;

    justify-content:space-between;

    border-bottom:
        1px solid
        rgba(255,255,255,.08);

    background:
        rgba(7,10,9,.88);

    backdrop-filter:
        blur(18px);

    position:sticky;

    top:0;

    z-index:20;
}

.brand{

    display:flex;

    align-items:center;

    gap:14px;
}

.logo{

    width:46px;

    height:46px;

    border-radius:14px;

    display:flex;

    align-items:center;

    justify-content:center;

    background:
        linear-gradient(
            145deg,
            #06271d,
            #0d1513
        );

    border:
        1px solid
        rgba(32,230,160,.45);

    box-shadow:
        0 0 24px
        rgba(32,230,160,.10);
}

.logo svg{

    width:31px;

    height:31px;
}

.title{

    font-size:24px;

    font-weight:800;

    letter-spacing:-.6px;
}

.title span{

    color:#20e6a0;
}

.subtitle{

    margin-top:3px;

    color:#8d9a96;

    font-size:12px;
}

.header-actions{

    display:flex;

    align-items:center;

    gap:10px;
}

.live{

    padding:
        8px 13px;

    border-radius:20px;

    color:#20e6a0;

    background:
        rgba(32,230,160,.08);

    border:
        1px solid
        rgba(32,230,160,.25);

    font-size:12px;

    font-weight:700;
}

.btn{

    text-decoration:none;

    border:0;

    cursor:pointer;

    color:#06100c;

    font-weight:800;

    background:#20e6a0;

    padding:
        10px 15px;

    border-radius:10px;

    transition:.2s;
}

.btn:hover{

    transform:translateY(-1px);

    box-shadow:
        0 8px 24px
        rgba(32,230,160,.18);
}


/* =========================================================
   PAGE
========================================================= */

.page{

    width:min(
        1480px,
        calc(100% - 40px)
    );

    margin:24px auto 40px;
}


/* =========================================================
   UPLOAD
========================================================= */

.upload-card{

    padding:18px;

    border-radius:16px;

    background:
        linear-gradient(
            145deg,
            rgba(17,24,22,.95),
            rgba(8,12,11,.95)
        );

    border:
        1px solid
        rgba(255,255,255,.08);

    box-shadow:
        0 20px 60px
        rgba(0,0,0,.22);

    margin-bottom:18px;
}

.upload-top{

    display:flex;

    align-items:center;

    justify-content:space-between;

    gap:20px;
}

.section-title{

    font-size:16px;

    font-weight:800;
}

.section-desc{

    color:#8d9a96;

    font-size:12px;

    margin-top:5px;
}

.upload-controls{

    display:flex;

    gap:10px;

    align-items:center;

    flex-wrap:wrap;
}

.file-input{

    color:#aab5b1;

    background:#0b100e;

    border:
        1px solid
        rgba(255,255,255,.10);

    padding:8px;

    border-radius:9px;
}

select{

    color:#eaf0ed;

    background:#0b100e;

    border:
        1px solid
        rgba(255,255,255,.10);

    padding:10px 12px;

    border-radius:9px;
}

.btn-blue{

    background:#2e9df4;

    color:white;
}

.btn-orange{

    background:#ff9d3c;

    color:#10100c;
}

.btn-red{

    background:#ff5d69;

    color:white;
}


/* =========================================================
   KPI
========================================================= */

.kpi-grid{

    display:grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap:14px;

    margin-bottom:16px;
}

.kpi{

    min-height:118px;

    padding:18px;

    border-radius:15px;

    background:
        linear-gradient(
            145deg,
            rgba(18,25,23,.96),
            rgba(8,12,11,.96)
        );

    border:
        1px solid
        rgba(255,255,255,.07);

    position:relative;

    overflow:hidden;
}

.kpi::after{

    content:"";

    position:absolute;

    width:100px;

    height:100px;

    right:-50px;

    top:-50px;

    border-radius:50%;

    background:
        rgba(32,230,160,.08);
}

.kpi-label{

    color:#7f8b87;

    font-size:11px;

    text-transform:uppercase;

    letter-spacing:.8px;

    font-weight:800;
}

.kpi-value{

    margin-top:9px;

    font-size:25px;

    font-weight:850;
}

.kpi-small{

    margin-top:5px;

    color:#899590;

    font-size:11px;
}

.green{
    color:#20e6a0;
}

.blue{
    color:#4ba8ff;
}

.orange{
    color:#ffae45;
}

.purple{
    color:#a879ff;
}


/* =========================================================
   CHART GRID
========================================================= */

.chart-grid{

    display:grid;

    grid-template-columns:
        1.25fr 1fr 1fr;

    gap:14px;
}

.card{

    min-width:0;

    border-radius:15px;

    padding:14px;

    background:
        linear-gradient(
            145deg,
            rgba(14,20,18,.97),
            rgba(7,11,10,.97)
        );

    border:
        1px solid
        rgba(255,255,255,.075);

    box-shadow:
        inset 0 1px 0
        rgba(255,255,255,.025);
}

.card-header{

    display:flex;

    align-items:center;

    justify-content:space-between;

    margin-bottom:4px;
}

.card-title{

    font-size:14px;

    font-weight:800;
}

.card-tag{

    color:#20e6a0;

    font-size:10px;

    font-weight:700;
}

.chart{

    width:100%;

    height:260px;
}

.chart-small{

    height:235px;
}


/* =========================================================
   WIDE CARDS
========================================================= */

.wide{

    grid-column:
        span 2;
}

.full{

    grid-column:
        1 / -1;
}

.insights{

    display:grid;

    grid-template-columns:
        repeat(4,1fr);

    gap:10px;
}

.insight{

    padding:14px;

    border-radius:12px;

    border:
        1px solid
        rgba(255,255,255,.07);

    background:#0a100e;
}

.insight-title{

    color:#7f8c87;

    font-size:10px;

    text-transform:uppercase;

    font-weight:800;
}

.insight-value{

    margin-top:7px;

    font-size:17px;

    font-weight:800;
}

.insight-text{

    margin-top:4px;

    color:#929e99;

    font-size:11px;

    line-height:1.5;
}


/* =========================================================
   FOOTER
========================================================= */

.footer{

    margin-top:20px;

    padding:16px;

    text-align:center;

    color:#68746f;

    font-size:11px;

    border-top:
        1px solid
        rgba(255,255,255,.06);
}


/* =========================================================
   RESPONSIVE
========================================================= */

@media(max-width:1100px){

    .kpi-grid{

        grid-template-columns:
            repeat(2,1fr);
    }

    .chart-grid{

        grid-template-columns:
            repeat(2,1fr);
    }

    .wide{

        grid-column:
            span 2;
    }

}

@media(max-width:700px){

    .header{

        height:auto;

        padding:15px;

        gap:12px;

        align-items:flex-start;
    }

    .header-actions{

        display:none;
    }

    .page{

        width:
            calc(100% - 20px);

        margin:
            15px auto;
    }

    .kpi-grid,
    .chart-grid{

        grid-template-columns:
            1fr;
    }

    .wide{

        grid-column:
            span 1;
    }

    .insights{

        grid-template-columns:
            1fr;
    }

    .upload-top{

        flex-direction:column;

        align-items:flex-start;
    }
}

</style>

</head>


<body>


<!-- =====================================================
     HEADER
===================================================== -->

<header class="header">

    <div class="brand">

        <div class="logo">

            <svg
                viewBox="0 0 48 48"
                fill="none"
                xmlns="http://www.w3.org/2000/svg">

                <path
                    d="M5 25H13L17 17L21 32L25 22L29 27H43"
                    stroke="#20E6A0"
                    stroke-width="3"
                    stroke-linecap="round"
                    stroke-linejoin="round"/>

                <path
                    d="M24 39C14 39 7 32 7 23C7 14 14 7 24 7C33 7 41 14 41 23"
                    stroke="#20E6A0"
                    stroke-width="2.5"
                    stroke-linecap="round"/>

            </svg>

        </div>

        <div>

            <div class="title">
                Patient Health
                <span>Intelligence</span>
                Dashboard
            </div>

            <div class="subtitle">
                Interactive patient analytics & hospital utilization intelligence
            </div>

        </div>

    </div>


    <div class="header-actions">

        <div class="live">
            ● LIVE ANALYSIS
        </div>

        <a
            class="btn"
            href="/patient-entry">
            + Add Patient
        </a>

    </div>

</header>


<!-- =====================================================
     PAGE
===================================================== -->

<main class="page">


<!-- =====================================================
     UPLOAD CARD
===================================================== -->

<section class="upload-card">

    <div class="upload-top">

        <div>

            <div class="section-title">
                📂 Dataset Control
            </div>

            <div class="section-desc">
                Upload any compatible patient CSV and automatically rebuild every visualization.
            </div>

        </div>


        <form
            class="upload-controls"
            action="/upload"
            method="POST"
            enctype="multipart/form-data">

            <input
                class="file-input"
                type="file"
                name="csv_file"
                accept=".csv"
                required>

            <select name="mode">

                <option value="append">
                    Add to existing data
                </option>

                <option value="replace">
                    Replace current data
                </option>

            </select>

            <button
                class="btn btn-blue"
                type="submit">

                Upload & Analyze

            </button>

        </form>

    </div>

</section>


<!-- =====================================================
     KPI CARDS
===================================================== -->

<section class="kpi-grid">


<div class="kpi">

    <div class="kpi-label">
        Total Patients
    </div>

    <div class="kpi-value green">
        {{ "{:,}".format(analysis.total) }}
    </div>

    <div class="kpi-small">
        Records currently analyzed
    </div>

</div>


<div class="kpi">

    <div class="kpi-label">
        Leading Diagnosis
    </div>

    <div class="kpi-value">
        {{ analysis.top_diagnosis }}
    </div>

    <div class="kpi-small">
        Most frequent primary diagnosis category
    </div>

</div>


<div class="kpi">

    <div class="kpi-label">
        Most Common Race
    </div>

    <div class="kpi-value blue">
        {{ analysis.top_race }}
    </div>

    <div class="kpi-small">
        Largest demographic group
    </div>

</div>


<div class="kpi">

    <div class="kpi-label">
        Average Hospital Stay
    </div>

    <div class="kpi-value orange">
        {{ analysis.avg_stay }}
        <small>days</small>
    </div>

    <div class="kpi-small">
        Calculated from time_in_hospital
    </div>

</div>


</section>


<!-- =====================================================
     CHARTS
===================================================== -->

<section class="chart-grid">


<!-- DIAGNOSIS -->

<div class="card wide">

    <div class="card-header">

        <div class="card-title">
            🩺 Patient Issues / Diagnosis Categories
        </div>

        <div class="card-tag">
            PRIMARY DIAGNOSIS
        </div>

    </div>

    <div id="diagnosisChart"
         class="chart">
    </div>

</div>


<!-- GENDER -->

<div class="card">

    <div class="card-header">

        <div class="card-title">
            👥 Gender Distribution
        </div>

        <div class="card-tag">
            DEMOGRAPHICS
        </div>

    </div>

    <div id="genderChart"
         class="chart">
    </div>

</div>


<!-- RACE -->

<div class="card">

    <div class="card-header">

        <div class="card-title">
            🌎 Race Distribution
        </div>

        <div class="card-tag">
            DEMOGRAPHICS
        </div>

    </div>

    <div id="raceChart"
         class="chart">
    </div>

</div>


<!-- AGE -->

<div class="card">

    <div class="card-header">

        <div class="card-title">
            📊 Age Group Distribution
        </div>

        <div class="card-tag">
            AGE
        </div>

    </div>

    <div id="ageChart"
         class="chart">
    </div>

</div>


<!-- ADMISSION TYPE -->

<div class="card">

    <div class="card-header">

        <div class="card-title">
            🚑 Admission Type
        </div>

        <div class="card-tag">
            UTILIZATION
        </div>

    </div>

    <div id="admissionTypeChart"
         class="chart">
    </div>

</div>


<!-- ADMISSION SOURCE -->

<div class="card">

    <div class="card-header">

        <div class="card-title">
            🏥 Admission Source
        </div>

        <div class="card-tag">
            SOURCE
        </div>

    </div>

    <div id="sourceChart"
         class="chart">
    </div>

</div>


<!-- HOSPITAL STAY -->

<div class="card wide">

    <div class="card-header">

        <div class="card-title">
            ⏱ Diagnosis vs Average Hospital Stay
        </div>

        <div class="card-tag">
            HOSPITAL UTILIZATION
        </div>

    </div>

    <div id="stayChart"
         class="chart">
    </div>

</div>


<!-- INSIGHTS -->

<div class="card full">

    <div class="card-header">

        <div class="card-title">
            💡 Key Insights
        </div>

        <div class="card-tag">
            AUTOMATED ANALYSIS
        </div>

    </div>


    <div class="insights">


        <div class="insight">

            <div class="insight-title">
                Largest Patient Issue
            </div>

            <div class="insight-value green">
                {{ analysis.top_diagnosis }}
            </div>

            <div class="insight-text">

                The most frequently recorded primary
                diagnosis category in the current dataset.

            </div>

        </div>


        <div class="insight">

            <div class="insight-title">
                Largest Race Group
            </div>

            <div class="insight-value blue">
                {{ analysis.top_race }}
            </div>

            <div class="insight-text">

                This demographic group represents the
                largest share of analyzed records.

            </div>

        </div>


        <div class="insight">

            <div class="insight-title">
                Hospital Utilization
            </div>

            <div class="insight-value orange">

                {{ analysis.avg_stay }} days

            </div>

            <div class="insight-text">

                Average recorded duration of hospitalization.

            </div>

        </div>


        <div class="insight">

            <div class="insight-title">
                Dataset Size
            </div>

            <div class="insight-value purple">

                {{ "{:,}".format(analysis.total) }}

            </div>

            <div class="insight-text">

                Patient records currently included in
                the dashboard calculations.

            </div>

        </div>


    </div>

</div>


</section>


<div class="footer">

    Patient Health Intelligence Dashboard
    • Analytics generated from uploaded patient data

</div>


</main>


<!-- =====================================================
     JAVASCRIPT
===================================================== -->

<script>

const analysis =
{{ analysis | tojson }};


/* =========================================================
   COMMON PLOT SETTINGS
========================================================= */

const baseLayout = {

    paper_bgcolor:
        "rgba(0,0,0,0)",

    plot_bgcolor:
        "rgba(0,0,0,0)",

    font:{
        color:"#d9e2de",
        family:"Inter, Segoe UI, Arial"
    },

    margin:{
        l:45,
        r:20,
        t:10,
        b:45
    },

    legend:{
        orientation:"h",
        y:-0.18,
        font:{
            size:10
        }
    },

    hoverlabel:{
        bgcolor:"#101816",
        bordercolor:"#20e6a0",
        font:{
            color:"#ffffff"
        }
    }
};


const config = {

    responsive:true,

    displaylogo:false,

    modeBarButtonsToRemove:[
        "lasso2d",
        "select2d"
    ]
};


/* =========================================================
   COLORS
========================================================= */

const chartColors = [
    "#20E6A0",
    "#39A8FF",
    "#FF9F43",
    "#9B6CFF",
    "#FF4F81",
    "#00C2FF",
    "#F7D154",
    "#FF7043",
    "#AAB7C4",
    "#4DD0E1"
];


/* =========================================================
   DIAGNOSIS
========================================================= */

const diagnosisLabels =
    Object.keys(analysis.diagnosis);

const diagnosisValues =
    diagnosisLabels.map(
        x => analysis.diagnosis[x].count
    );

Plotly.newPlot(
    "diagnosisChart",
    [{
        labels:diagnosisLabels,
        values:diagnosisValues,
        type:"pie",
        hole:.62,
        textinfo:"none",
        marker:{
            colors:chartColors
        },
        hovertemplate:
            "<b>%{label}</b><br>" +
            "Patients: %{value:,}<br>" +
            "Share: %{percent}<extra></extra>"
    }],
    {
        ...baseLayout,

        showlegend:true,

        legend:{
            orientation:"v",
            x:.58,
            y:.5,
            font:{size:9}
        }
    },
    config
);


/* =========================================================
   GENDER
========================================================= */

const genderLabels =
    Object.keys(analysis.gender);

const genderValues =
    genderLabels.map(
        x => analysis.gender[x].count
    );

Plotly.newPlot(
    "genderChart",
    [{
        x:genderLabels,
        y:genderValues,
        type:"bar",
        marker:{
            color:[
                "#FF4F81",
                "#39A8FF",
                "#9B6CFF"
            ]
        },

        hovertemplate:
            "<b>%{x}</b><br>" +
            "Patients: %{y:,}<extra></extra>"
    }],
    {
        ...baseLayout,

        margin:{
            l:45,
            r:15,
            t:10,
            b:50
        },

        xaxis:{
            gridcolor:"#18302a"
        },

        yaxis:{
            gridcolor:"#18302a",
            zeroline:false
        }
    },
    config
);


/* =========================================================
   RACE
========================================================= */

const raceLabels =
    Object.keys(analysis.race);

const raceValues =
    raceLabels.map(
        x => analysis.race[x].count
    );

Plotly.newPlot(
    "raceChart",
    [{
        labels:raceLabels,
        values:raceValues,
        type:"pie",
        hole:.58,
        textinfo:"none",
        marker:{
            colors:[
                "#20E6A0",
                "#FF8A4C",
                "#39A8FF",
                "#9B6CFF",
                "#F7D154",
                "#AAB7C4"
            ]
        },

        hovertemplate:
            "<b>%{label}</b><br>" +
            "Patients: %{value:,}<br>" +
            "Share: %{percent}<extra></extra>"
    }],
    {
        ...baseLayout,
        showlegend:true,

        legend:{
            orientation:"v",
            x:.62,
            y:.5,
            font:{size:9}
        }
    },
    config
);


/* =========================================================
   AGE
========================================================= */

const ageOrder = [
    "<40",
    "40–59",
    "60–69",
    "70–79",
    "80+",
    "Unknown"
];

const existingAgeLabels =
    ageOrder.filter(
        x => analysis.age[x]
    );

const ageValues =
    existingAgeLabels.map(
        x => analysis.age[x].count
    );

Plotly.newPlot(
    "ageChart",
    [{
        x:existingAgeLabels,
        y:ageValues,
        type:"bar",

        marker:{
            color:[
                "#39A8FF",
                "#20E6A0",
                "#FF9F43",
                "#9B6CFF",
                "#4DD0E1",
                "#AAB7C4"
            ]
        },

        hovertemplate:
            "<b>%{x}</b><br>" +
            "Patients: %{y:,}<extra></extra>"
    }],
    {
        ...baseLayout,

        xaxis:{
            gridcolor:"#18302a"
        },

        yaxis:{
            gridcolor:"#18302a",
            zeroline:false
        }
    },
    config
);


/* =========================================================
   ADMISSION TYPE
========================================================= */

const admissionLabels =
    Object.keys(analysis.admission_type);

const admissionValues =
    admissionLabels.map(
        x => analysis.admission_type[x].count
    );

Plotly.newPlot(
    "admissionTypeChart",
    [{
        labels:admissionLabels,
        values:admissionValues,
        type:"pie",
        hole:.60,

        marker:{
            colors:[
                "#39A8FF",
                "#FF9F43",
                "#20E6A0",
                "#9B6CFF",
                "#AAB7C4"
            ]
        },

        textinfo:"none",

        hovertemplate:
            "<b>%{label}</b><br>" +
            "Patients: %{value:,}<br>" +
            "Share: %{percent}<extra></extra>"
    }],
    {
        ...baseLayout,
        showlegend:true
    },
    config
);


/* =========================================================
   ADMISSION SOURCE
========================================================= */

const sourceLabels =
    Object.keys(
        analysis.admission_source
    );

const sourceValues =
    sourceLabels.map(
        x =>
            analysis.admission_source[x].count
    );


Plotly.newPlot(
    "sourceChart",
    [{
        x:sourceValues,
        y:sourceLabels,
        type:"bar",
        orientation:"h",

        marker:{
            color:"#20E6A0"
        },

        hovertemplate:
            "<b>%{y}</b><br>" +
            "Patients: %{x:,}<extra></extra>"
    }],
    {
        ...baseLayout,

        margin:{
            l:100,
            r:15,
            t:10,
            b:35
        },

        xaxis:{
            gridcolor:"#18302a"
        },

        yaxis:{
            gridcolor:"#18302a",
            automargin:true
        }
    },
    config
);


/* =========================================================
   DIAGNOSIS VS HOSPITAL STAY
========================================================= */

const stayLabels =
    Object.keys(
        analysis.diagnosis_stay
    );

const stayValues =
    stayLabels.map(
        x => analysis.diagnosis_stay[x]
    );

Plotly.newPlot(
    "stayChart",
    [{
        x:stayValues,
        y:stayLabels,
        type:"bar",
        orientation:"h",

        marker:{
            color:[
                "#20E6A0",
                "#39A8FF",
                "#FF9F43",
                "#9B6CFF",
                "#FF4F81",
                "#00C2FF",
                "#F7D154",
                "#FF7043",
                "#AAB7C4"
            ]
        },

        hovertemplate:
            "<b>%{y}</b><br>" +
            "Average stay: %{x:.2f} days" +
            "<extra></extra>"
    }],
    {
        ...baseLayout,

        margin:{
            l:170,
            r:20,
            t:10,
            b:40
        },

        xaxis:{
            title:"Average Hospital Stay (days)",
            gridcolor:"#18302a"
        },

        yaxis:{
            automargin:true
        }
    },
    config
);

</script>

</body>

</html>
"""


# ============================================================
# PATIENT ENTRY HTML
# ============================================================

PATIENT_HTML = r"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Add Patient</title>

<style>

*{
    box-sizing:border-box;
}

body{

    margin:0;

    background:
        radial-gradient(
            circle at 20% 0%,
            rgba(32,230,160,.08),
            transparent 30%
        ),
        #050807;

    color:#f5f7f6;

    font-family:
        Inter,
        Segoe UI,
        Arial;
}

.header{

    height:76px;

    padding:0 34px;

    display:flex;

    justify-content:space-between;

    align-items:center;

    border-bottom:
        1px solid
        rgba(255,255,255,.08);

    background:#070a09;
}

.logo-title{

    font-size:25px;

    font-weight:850;
}

.logo-title span{

    color:#20e6a0;
}

.back{

    color:#20e6a0;

    text-decoration:none;

    font-weight:700;
}

.container{

    width:min(
        900px,
        calc(100% - 30px)
    );

    margin:40px auto;

    padding:32px;

    border-radius:20px;

    background:
        linear-gradient(
            145deg,
            #101714,
            #070b0a
        );

    border:
        1px solid
        rgba(32,230,160,.25);

    box-shadow:
        0 25px 80px
        rgba(0,0,0,.4);
}

h1{

    margin:0;

    font-size:34px;
}

.description{

    color:#8d9a96;

    margin:8px 0 28px;
}

.form-grid{

    display:grid;

    grid-template-columns:
        1fr 1fr;

    gap:18px;
}

.field{

    display:flex;

    flex-direction:column;

    gap:7px;
}

.field label{

    color:#b6c1bd;

    font-size:12px;

    font-weight:700;
}

input,
select{

    width:100%;

    padding:13px;

    border-radius:10px;

    border:
        1px solid
        #21443a;

    background:#070d0b;

    color:white;

    outline:none;
}

input:focus,
select:focus{

    border-color:#20e6a0;

    box-shadow:
        0 0 0 3px
        rgba(32,230,160,.08);
}

.full{

    grid-column:
        1 / -1;
}

.submit-area{

    margin-top:25px;

    display:flex;

    gap:12px;

    align-items:center;

    flex-wrap:wrap;
}

button{

    border:0;

    padding:13px 20px;

    border-radius:10px;

    cursor:pointer;

    font-weight:800;

    background:#20e6a0;

    color:#04100b;
}

.replace{

    background:#ff9f43;

    color:#160d03;
}

@media(max-width:700px){

    .form-grid{

        grid-template-columns:1fr;
    }

    .full{

        grid-column:span 1;
    }

}

</style>

</head>


<body>


<header class="header">

    <div class="logo-title">

        Patient Health
        <span>Intelligence</span>

    </div>

    <a
        href="/"
        class="back">

        ← Back to Dashboard

    </a>

</header>


<main class="container">

    <h1>
        + Add Patient
    </h1>

    <div class="description">

        Enter a patient manually. The dashboard
        will automatically recalculate all
        charts and analytics.

    </div>


    <form
        action="/add-patient"
        method="POST">


        <div class="form-grid">


            <div class="field">

                <label>Race</label>

                <select name="race">

                    <option>Caucasian</option>

                    <option>AfricanAmerican</option>

                    <option>Hispanic</option>

                    <option>Asian</option>

                    <option>Other</option>

                    <option>Unknown</option>

                </select>

            </div>


            <div class="field">

                <label>Gender</label>

                <select name="gender">

                    <option>Female</option>

                    <option>Male</option>

                    <option>Unknown</option>

                </select>

            </div>


            <div class="field">

                <label>Age Group</label>

                <select name="age">

                    <option>[0-10)</option>

                    <option>[10-20)</option>

                    <option>[20-30)</option>

                    <option>[30-40)</option>

                    <option>[40-50)</option>

                    <option>[50-60)</option>

                    <option>[60-70)</option>

                    <option>[70-80)</option>

                    <option>[80-90)</option>

                    <option>[90-100)</option>

                </select>

            </div>


            <div class="field">

                <label>Admission Type ID</label>

                <select name="admission_type_id">

                    <option value="1">
                        1 - Emergency
                    </option>

                    <option value="2">
                        2 - Urgent
                    </option>

                    <option value="3">
                        3 - Elective
                    </option>

                    <option value="4">
                        4 - Newborn
                    </option>

                    <option value="5">
                        5 - Other
                    </option>

                </select>

            </div>


            <div class="field">

                <label>Admission Source ID</label>

                <input
                    name="admission_source_id"
                    type="number"
                    value="7"
                    min="0">

            </div>


            <div class="field">

                <label>Discharge Disposition ID</label>

                <input
                    name="discharge_disposition_id"
                    type="number"
                    value="1"
                    min="0">

            </div>


            <div class="field">

                <label>Time in Hospital (days)</label>

                <input
                    name="time_in_hospital"
                    type="number"
                    value="3"
                    min="1"
                    max="100">

            </div>


            <div class="field">

                <label>Number of Lab Procedures</label>

                <input
                    name="num_lab_procedures"
                    type="number"
                    value="0"
                    min="0">

            </div>


            <div class="field">

                <label>Primary Diagnosis Code</label>

                <input
                    name="diag_1"
                    placeholder="Example: 428.0"
                    required>

            </div>


            <div class="field">

                <label>Secondary Diagnosis Code</label>

                <input
                    name="diag_2"
                    placeholder="Optional">

            </div>


            <div class="field">

                <label>Third Diagnosis Code</label>

                <input
                    name="diag_3"
                    placeholder="Optional">

            </div>


            <div class="field">

                <label>Data Mode</label>

                <select name="mode">

                    <option value="append">
                        Add to existing dataset
                    </option>

                    <option value="replace">
                        Create new dataset
                    </option>

                </select>

            </div>


        </div>


        <div class="submit-area">

            <button type="submit">

                ✓ Add Patient & Update Dashboard

            </button>

            <a
                href="/"
                class="back">

                Cancel

            </a>

        </div>


    </form>

</main>

</body>

</html>
"""


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    print()
    print("==============================================")
    print(" Patient Health Intelligence Dashboard")
    print("==============================================")
    print()
    print("Open:")
    print("http://127.0.0.1:5000")
    print()
    print("Patient Entry:")
    print("http://127.0.0.1:5000/patient-entry")
    print()
 
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )