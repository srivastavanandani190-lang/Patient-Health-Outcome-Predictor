 <div align="center">

  <!-- Animated SVG Header Banner -->
  <img src="./assets/gemini-svg.svg" alt="Patient Health Outcome Predictor Banner" width="100%" />

  <br/>

  <!-- Matching Tagline -->
  <h2>🩺 Mastering Clinical Outcome Analytics</h2>
  <p><i>"Transforming EHR patterns into explainable, life-saving predictive care."</i></p>

  <!-- Color-Coded Metadata Badges (Matching reference style) -->
  <p>
    <img src="https://img.shields.io/badge/DOMAIN-HEALTHCARE%20%26%20PHARMA-007ACC?style=for-the-badge&logo=medicare&logoColor=white" />
    <img src="https://img.shields.io/badge/PROJECT-P__025-00A896?style=for-the-badge" />
    <img src="https://img.shields.io/badge/TEAM-NEVER--MIND-028090?style=for-the-badge&logo=github&logoColor=white" />
    <img src="https://img.shields.io/badge/LEAD-NANDANI%20KUMARI-05668D?style=for-the-badge" />
  </p>

   
</div>

---

## 💡 Problem vs. Solution

<div align="center">

<table>
<tr>

<td width="48%" align="center" bgcolor="#EAF4FF">

<h3>❌ CURRENT PROBLEMS</h3>

<br>

🔴 <b>Undetected 30-Day Readmission Risk</b><br>
Patient readmission risk may remain unnoticed at discharge.

<br><br>

🔴 <b>Black-Box Predictions</b><br>
Risk predictions can lack clear explanations of contributing factors.

<br><br>

🔴 <b>Siloed Healthcare Data</b><br>
Limited visibility into population-level trends and patterns.

</td>

<td width="4%" align="center">

➡️

</td>

<td width="48%" align="center" bgcolor="#E8FAF4">

<h3>✅ OUR SOLUTION</h3>

<br>

🟢 <b>Risk Scoring</b><br>
Analyze patient data to identify readmission risk.

<br><br>

🟢 <b>Explainable Insights</b><br>
Highlight important factors contributing to patient risk.

<br><br>

🟢 <b>Interactive Analytics</b><br>
Visualize population trends, diagnosis patterns and outcomes.

</td>

</tr>
</table>

</div>

---

## 🎨 System Architecture (HLD & LLD)

Here is the full system architecture visual, colored with our presentation palette (**Teal, Sky Blue, Violet, Amber, and Emerald**).

### 🔷 High Level Design (HLD)
```mermaid
flowchart TD
    %% Custom Styling
    classDef staff fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#000000,font-weight:bold;
    classDef dash fill:#f0f9ff,stroke:#0284c7,stroke-width:2px,color:#000000,font-weight:bold;
    classDef backend fill:#ecfdf5,stroke:#059669,stroke-width:2px,color:#000000,font-weight:bold;
    classDef data fill:#fffbeb,stroke:#d97706,stroke-width:2px,color:#000000,font-weight:bold;
    classDef ml fill:#faf5ff,stroke:#7e22ce,stroke-width:2px,color:#000000,font-weight:bold;
    classDef result fill:#f0fdf4,stroke:#16a34a,stroke-width:3px,color:#000000,font-weight:bold;

    User["👨‍⚕️ Hospital Staff / Analyst<br/><small>Enters vitals, reviews risk probabilities</small>"]:::staff
    UI["💻 Frontend Dashboard<br/><small>Patient Intake Form • CSV Upload • Risk Alerts</small>"]:::dash
    API["⚙️ Backend Server — Python / Flask<br/><small>Request Validation • Pipeline Orchestrator • REST Endpoints</small>"]:::backend
    Data[("🗄️ Data Layer<br/><small>UCI Benchmark (130-US Hospitals) + Synthetic Cohorts</small>")]:::data
    Engine["🧠 ML & Explainability Engine<br/><small>scikit-learn Pipelines • SMOTE Balancing • SHAP Explainer</small>"]:::ml
    Output["📊 Results & Visual Analytics<br/><small>Calibrated Probability • Risk Category Band • Feature Attributions</small>"]:::result

    User -->|"1. Submits Clinical Parameters"| UI
    UI -->|"2. JSON Payload"| API
    API <-->|"3. Data Retrieval & Store"| Data
    API <-->|"4. Scoring & Attribution"| Engine
    API -->|"5. Predictions & SHAP Values"| UI
    UI -->|"6. Renders Actionable Insights"| Output
```

---

### 🔶 Low Level Design (LLD Modular Pipeline)
```mermaid
flowchart TD
    classDef p1 fill:#eff6ff,stroke:#3b82f6,stroke-width:2px,color:#1e3a8a,font-weight:bold;
    classDef p2 fill:#f0f9ff,stroke:#0284c7,stroke-width:2px,color:#0369a1,font-weight:bold;
    classDef p3 fill:#fffbeb,stroke:#d97706,stroke-width:2px,color:#78350f,font-weight:bold;
    classDef p4 fill:#fdf2f8,stroke:#db2777,stroke-width:2px,color:#831843,font-weight:bold;
    classDef p5 fill:#f0fdfa,stroke:#0f766e,stroke-width:2px,color:#134e4a,font-weight:bold;
    classDef p6 fill:#faf5ff,stroke:#7c3aed,stroke-width:2px,color:#4c1d95,font-weight:bold;
    classDef p7 fill:#f0fdf4,stroke:#16a34a,stroke-width:3px,color:#14532d,font-weight:bold;

    M1["01 • Patient Input Module<br/><small>Age • Gender • Admission Type • Time in Hospital • Lab Counts • Diagnoses</small>"]:::p1
    M2["02 • Validation Module<br/><small>Schema validation, data type enforcement, range boundaries & missing value detection</small>"]:::p2
    M3["03 • Preprocessing Module<br/><small>Median Imputation • One-Hot Feature Encoding • Scaling & Alignment</small>"]:::p3
    M4["04 • ML Prediction Module<br/><small>Trained Pipeline Estimator • Probability Estimation via model.joblib</small>"]:::p4
    M5A["05A • Risk Classification<br/><small>Configured Threshold Bands: Low | Moderate | High</small>"]:::p5
    M5B["05B • SHAP XAI Module<br/><small>Feature Attributions & Local Factor Explanations</small>"]:::p6
    M6["06 • Output & Dashboard Module<br/><small>Plotly Visualizations • Dynamic Clinical Summary Delivery</small>"]:::p7

    M1 ==> M2 ==> M3 ==> M4
    M4 ==> M5A
    M4 ==> M5B
    M5A ==> M6
    M5B ==> M6
```

---

## 🔄 Data Flow Diagrams (DFD)

### 📌 DFD Level 0 — System Context View
```mermaid
flowchart LR
    classDef ent fill:#eff6ff,stroke:#2563eb,stroke-width:2px,color:#1e3a8a,font-weight:bold;
    classDef proc fill:#f0fdf4,stroke:#22c55e,stroke-width:3px,color:#14532d,font-weight:bold;
    classDef out fill:#faf5ff,stroke:#9333ea,stroke-width:2px,color:#581c87,font-weight:bold;

    Staff["👨‍⚕️ Hospital Staff / Analyst"]:::ent
    P0(("0.0<br/>Healthcare Readmission<br/>Prediction System")):::proc
    Dash["📊 Clinical Dashboard & Reports"]:::out

    Staff -->|"Patient Vitals & Intake Data"| P0
    P0 -->|"Calculated Readmission Risk"| Staff
    P0 -->|"Population Analytics & Factor Distributions"| Dash
    Dash -->|"Query Filters & What-if Scenarios"| P0
```

---

### 📌 DFD Level 1 — Decomposed Data Routing
```mermaid
flowchart TD
    classDef ext fill:#eff6ff,stroke:#3b82f6,stroke-width:2px,color:#1e40af,font-weight:bold;
    classDef p1 fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d,font-weight:bold;
    classDef p2 fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#075985,font-weight:bold;
    classDef store fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#92400e,font-weight:bold;
    classDef out fill:#f3e8ff,stroke:#7e22ce,stroke-width:2px,color:#581c87,font-weight:bold;

    Staff["👨‍‍⚕️ Hospital Staff / Analyst"]:::ext
    Patient["🧑 Patient Entity"]:::ext
    P1(("1.0<br/>Manage & Cleanse<br/>Patient Data")):::p1
    P2(("2.0<br/>Generate Risk Predictions<br/>& Explainable Reports")):::p2
    DB[("D1 • Healthcare Database<br/>(Encounter Logs, Encoders, Pipelines)")]:::store
    Dash["📊 Interactive Visual Dashboard"]:::out

    Staff -->|"Patient Demographics & Medical Codes"| P1
    Patient -->|"Medical History & Stay Info"| P1
    P1 -->|"Validated Feature Set"| P2
    P1 <-->|"Store & Query Clean Encounters"| DB

    Staff -->|"Select Cohort & Trigger Analysis"| P2
    P2 <-->|"Load Pre-trained Pipeline Artifacts"| DB
    P2 -->|"Risk Probabilities & SHAP Explanations"| Dash
    P2 -->|"Patient Risk Summary Report"| Staff
```

---

## 🛠️ Technology Stack Breakdown

<div align="center">

| Module | Technologies | Icon / Badge | Role in Project |
| :--- | :--- | :---: | :--- |
| **Backend Core** | Python 3.9+, Flask, Gunicorn | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) | Lightweight REST API routing and prediction endpoints |
| **Data Engine** | Pandas, NumPy | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | Vectorized preprocessing, null imputation, and data cleaning |
| **ML Framework** | scikit-learn, joblib | ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) | Pipeline architecture, hyperparameter tuning & serialization |
| **Class Balancing** | imbalanced-learn (SMOTE) | ![SMOTE](https://img.shields.io/badge/SMOTE-Balanced-brightgreen?style=flat-square) | Resolves 30-day readmission label skewness |
| **Explainable AI** | SHAP (SHapley Additive exPlanations) | ![SHAP](https://img.shields.io/badge/SHAP-Explainable%20AI-9cf?style=flat-square) | Localized feature contribution attribution for clinicians |
| **Visual Analytics** | Plotly Express, HTML5, CSS3 | ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white) | Interactive donut charts, gender splits, and risk gauges |

</div>

---

## ⚡ Quick Start & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/srivastavanandani190-lang/Patient-Health-Outcome-Predictor.git
cd Patient-Health-Outcome-Predictor
```

### 2. Configure Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch the Web Application
```bash
python app.py
```
> Navigate to `http://127.0.0.1:5000` to interact with the prediction form and live analytics dashboard.

---

## 🛡️ Privacy, Ethics & Regulatory Compliance

* **HIPAA Safe Harbor:** Built strictly on de-identified and synthetic benchmark cohorts (UCI repository). No personally identifiable protected health information (PHI) is processed or stored.
* **Explainability by Design:** Rather than offering black-box risk probabilities, every recommendation features transparent clinical factor weights to aid clinician decision-making.

---

 

 
