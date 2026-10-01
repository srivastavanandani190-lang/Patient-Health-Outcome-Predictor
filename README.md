<div align="center">

<!-- Animated Header Banner SVG -->
<svg viewBox="0 0 1000 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#091e3a"/>
      <stop offset="50%" stop-color="#0f3460"/>
      <stop offset="100%" stop-color="#16213e"/>
    </linearGradient>
    <linearGradient id="tealCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe"/>
      <stop offset="100%" stop-color="#4facfe"/>
    </linearGradient>
    <linearGradient id="accentPulse" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38ef7d"/>
      <stop offset="100%" stop-color="#11998e"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    @keyframes pulseLine {
      0% { stroke-dashoffset: 800; opacity: 0.3; }
      50% { opacity: 1; }
      100% { stroke-dashoffset: 0; opacity: 0.3; }
    }
    @keyframes beat {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.08); }
    }
    @keyframes floatOrb {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-8px); }
    }
    .ecg-line {
      stroke: #00f2fe;
      stroke-width: 2.5;
      fill: none;
      stroke-dasharray: 800;
      animation: pulseLine 4.5s ease-in-out infinite;
      filter: drop-shadow(0 0 6px #00f2fe);
    }
    .pulse-heart {
      transform-origin: 500px 52px;
      animation: beat 2s infinite ease-in-out;
    }
    .floating-badge {
      animation: floatOrb 3s ease-in-out infinite;
    }
  </style>

  <!-- Background Base with subtle border -->
  <rect width="1000" height="280" rx="16" fill="url(#bgGrad)"/>
  <rect x="1.5" y="1.5" width="997" height="277" rx="15" fill="none" stroke="rgba(0, 242, 254, 0.25)" stroke-width="2"/>

  <!-- Subtle Background Grid Overlay -->
  <path d="M 0,70 L 1000,70 M 0,140 L 1000,140 M 0,210 L 1000,210 M 200,0 L 200,280 M 400,0 L 400,280 M 600,0 L 600,280 M 800,0 L 800,280" stroke="rgba(255,255,255,0.04)" stroke-width="1"/>

  <!-- Animated ECG Vitals Rhythm -->
  <path class="ecg-line" d="M 0,215 L 140,215 L 160,205 L 175,225 L 195,215 L 230,215 L 245,185 L 260,250 L 280,140 L 300,240 L 315,200 L 330,215 L 460,215 L 480,205 L 495,225 L 515,215 L 560,215 L 575,175 L 590,255 L 610,135 L 630,245 L 645,195 L 660,215 L 820,215 L 840,205 L 855,225 L 875,215 L 910,215 L 925,180 L 940,245 L 960,150 L 980,230 L 1000,215" />

  <!-- Track Pill -->
  <g class="floating-badge">
    <rect x="270" y="24" width="460" height="30" rx="15" fill="rgba(0, 242, 254, 0.12)" stroke="#00f2fe" stroke-width="1"/>
    <text x="500" y="44" fill="#00f2fe" font-family="'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" text-anchor="middle">
      PROJECT P_025  •  BUSINESS ANALYTICS  •  HEALTHCARE &amp; PHARMA
    </text>
  </g>

  <!-- Big Title -->
  <text x="500" y="108" fill="#ffffff" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="34" font-weight="900" letter-spacing="0.5" text-anchor="middle" filter="url(#glow)">
    Patient Health Outcome Predictor
  </text>

  <!-- Subtitle -->
  <text x="500" y="142" fill="#93c5fd" font-family="'Segoe UI', Arial, sans-serif" font-size="15" font-weight="400" text-anchor="middle">
    Predictive Clinical Intelligence &amp; 30-Day Readmission Risk Stratification
  </text>

  <!-- Animated Bottom Badges inside SVG -->
  <g transform="translate(230, 160)">
    <!-- Team Badge -->
    <rect x="0" y="0" width="250" height="42" rx="10" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.18)" stroke-width="1"/>
    <circle cx="22" cy="21" r="10" fill="#0284c7"/>
    <text x="22" y="25" fill="#fff" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="900" text-anchor="middle">👥</text>
    <text x="44" y="18" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="700">TEAM NAME</text>
    <text x="44" y="33" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="800">Never-Mind</text>

    <!-- Member Badge -->
    <rect x="280" y="0" width="260" height="42" rx="10" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.18)" stroke-width="1"/>
    <circle cx="302" cy="21" r="10" fill="#10b981"/>
    <text x="302" y="25" fill="#fff" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="900" text-anchor="middle">👩‍💻</text>
    <text x="324" y="18" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="700">LEAD ANALYST</text>
    <text x="324" y="33" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="800">Nandani Kumari</text>
  </g>
</svg>

<br/>

<!-- Modern Shields.io Badges with Gradients & Glow -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%20%7C%203.10-00f2fe?style=for-the-badge&logo=python&logoColor=black" alt="Python"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-scikit--learn-ff9a44?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn"/>
  <img src="https://img.shields.io/badge/Explainability-SHAP%20XAI-8b5cf6?style=for-the-badge&logo=openai&logoColor=white" alt="SHAP"/>
  <img src="https://img.shields.io/badge/Web%20App-Flask%20%2B%20Jinja-0ea5e9?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/Visuals-Plotly%20Dynamic-10b981?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly"/>
  <img src="https://img.shields.io/badge/Compliance-HIPAA%20De--identified-14b8a6?style=for-the-badge&logo=shield&logoColor=white" alt="HIPAA"/>
</p>

<!-- Live Pulse Indicator -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=16&duration=3000&pause=1000&color=00F2FE&center=true&vCenter=true&width=580&lines=⚡+Scoring+30-Day+Patient+Readmission+Probabilities;🔍+Explaining+Predictions+with+SHAP+Feature+Values;📊+Live+Plotly+Dashboards+for+Hospital+Staff;🛡️+Privacy-First+Synthetic+%26+UCI+Clinical+Datasets" alt="Typing SVG" />
</p>

</div>

---

## 🌟 Clinical Key Metrics at a Glance

<div align="center">
<table>
  <tr>
    <td align="center" width="25%" style="background:#0f172a; border-radius:12px; padding:12px;">
      <font color="#38bdf8" size="2"><b>TOTAL ANALYZED RECORDS</b></font><br/>
      <font color="#00f2fe" size="6"><b>69,975+</b></font><br/>
      <font color="#94a3b8" size="2">UCI 130-US Hospitals</font>
    </td>
    <td align="center" width="25%" style="background:#0f172a; border-radius:12px; padding:12px;">
      <font color="#f43f5e" size="2"><b>LEADING DIAGNOSIS</b></font><br/>
      <font color="#fb7185" size="5"><b>Circulatory</b></font><br/>
      <font color="#94a3b8" size="2">30.4% Primary Encounter</font>
    </td>
    <td align="center" width="25%" style="background:#0f172a; border-radius:12px; padding:12px;">
      <font color="#4ade80" size="2"><b>AVG HOSPITAL STAY</b></font><br/>
      <font color="#22c55e" size="6"><b>4.27</b></font> <font color="#86efac">Days</font><br/>
      <font color="#94a3b8" size="2">Risk Stratification Metric</font>
    </td>
    <td align="center" width="25%" style="background:#0f172a; border-radius:12px; padding:12px;">
      <font color="#c084fc" size="2"><b>MODEL EXPLAINABILITY</b></font><br/>
      <font color="#a855f7" size="5"><b>SHAP XAI</b></font><br/>
      <font color="#94a3b8" size="2">Transparent Risk Drivers</font>
    </td>
  </tr>
</table>
</div>

---

## 💡 Problem vs. Solution

```mermaid
mindmap
  root((🏥 Readmission<br/>Predictor))
    ❌ Current Bottlenecks
      [High 30-Day Readmissions undetected at discharge]
      [Black-box ML predictions without clinical explanation]
      [Siloed data leaving analysts without population trends]
    ✅ Intelligent Solution
      (Flask App with real-time intake scoring)
      (SHAP Values breaking down top clinical biomarkers)
      (Interactive Plotly charts comparing 'What-If' treatments)
      (Balanced classification using SMOTE)
```

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

## 📁 Repository Organization

```text
├── data/
│   ├── raw/                       # De-identified UCI Diabetes 130-US Hospitals dataset
│   └── processed/                 # Feature engineered & imputed matrices
├── models/
│   ├── model.joblib               # Serialized scikit-learn classification pipeline
│   └── preprocessor.joblib        # One-hot encoders & standard scalers
├── static/
│   ├── css/                       # Presentation-matched styling & color palettes
│   └── js/                        # Form validations and async AJAX handlers
├── templates/
│   ├── index.html                 # Clinical Intelligence Dashboard with KPI cards
│   ├── predict.html               # Add Patient Form & dynamic risk calculator
│   └── results.html               # SHAP feature importance plot & recommendations
├── app.py                         # Flask server routes & application entry point
├── pipeline.py                    # Training scripts with SMOTE class balancing
├── explainability.py              # SHAP summary & force plot generation logic
├── requirements.txt               # Pinned Python package dependencies
└── README.md                      # Animated project presentation & architecture
```

---

## 🛡️ Privacy, Ethics & Regulatory Compliance

* **HIPAA Safe Harbor:** Built strictly on de-identified and synthetic benchmark cohorts (UCI repository). No personally identifiable protected health information (PHI) is processed or stored.
* **Explainability by Design:** Rather than offering black-box risk probabilities, every recommendation features transparent clinical factor weights to aid clinician decision-making.

---

<div align="center">

### 🤝 Project Information

**Track:** Project P_025 • Business Analytics • Healthcare & Pharma  
**Team Name:** Never-Mind  
**Lead Developer:** [Nandani Kumari](https://github.com/srivastavanandani190-lang)

<br/>

<a href="#-patient-health-outcome-predictor-p_025">
  <img src="https://img.shields.io/badge/Back%20To%20Top-00f2fe?style=for-the-badge&logo=quicktime&logoColor=black" alt="Back To Top"/>
</a>

</div>
