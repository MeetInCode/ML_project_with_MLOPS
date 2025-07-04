

## Project Overview

This end-to-end machine learning project predicts student performance based on various demographic and academic factors. The project implements a complete MLOps pipeline including data processing, model training, API development, containerization, and automated deployment.

## 🏗️ Detailed Project Architecture

```mermaid
graph TD
    A[Student Performance Data] -->|Data Ingestion Pipeline| B[Raw Data Processing]
    B -->|Data Validation| C[Data Cleaning]
    C -->|Feature Engineering| D[Data Transformation]

    subgraph Data Processing Layer
    B --> |Missing Value Handling| C1[Clean Dataset]
    C1 --> |Feature Scaling| C2[Standardized Features]
    C2 --> |Encoding| C3[Processed Features]
    end

    subgraph Model Training Layer
    D --> E[Train-Test Split]
    E --> |Training Data| F1[Model Training]
    E --> |Test Data| F2[Model Evaluation]
    F1 --> |CatBoost & XGBoost| G1[Model Selection]
    F2 --> |Metrics Evaluation| G1
    G1 --> |Best Model| H[Model Artifacts]
    end

    subgraph Application Layer
    H --> |Load Model| I[Flask Application]
    I --> |Web Routes| J1[Home Page]
    I --> |API Endpoint| J2[Prediction API]
    J1 --> |User Interface| K1[Input Form]
    J2 --> |REST API| K2[JSON Response]
    K1 --> |Form Submission| L[Prediction Pipeline]
    K2 --> L
    L --> |Model Inference| M[Predictions]
    end

    subgraph MLOps Components
    N1[Logger] --> |Log Events| N2[Log Files]
    O1[Exception Handler] --> |Error Tracking| O2[Error Logs]
    P1[Model Monitor] --> |Performance Metrics| P2[Monitoring Dashboard]
    end

    style Data Processing Layer fill:#e6ffe6,stroke:#333,stroke-width:2px
    style Model Training Layer fill:#e6f3ff,stroke:#333,stroke-width:2px
    style Application Layer fill:#ffe6e6,stroke:#333,stroke-width:2px
    style MLOps Components fill:#fff5e6,stroke:#333,stroke-width:2px
```

### Detailed Architecture Components:

1. **Data Processing Layer**:

   - Raw data ingestion from student performance dataset
   - Automated data validation and cleaning
   - Feature scaling and standardization
   - Categorical variable encoding
   - Missing value handling and outlier detection

2. **Model Training Layer**:

   - Automated train-test split with stratification
   - Multiple model training (CatBoost, XGBoost)
   - Hyperparameter optimization
   - Model evaluation and selection
   - Model artifact generation and storage

3. **Application Layer**:

   - Flask web application with responsive UI
   - RESTful API endpoints for predictions
   - Form-based user input collection
   - Real-time prediction pipeline
   - Result visualization and display

4. **MLOps Components**:
   - Comprehensive logging system
   - Custom exception handling
   - Performance monitoring
   - Model versioning
   - Automated testing

## 🌟 Features

- Automated data ingestion and preprocessing
- Model training with multiple algorithms
- Interactive web interface for predictions
- Containerized application for consistent deployment
- Automated CI/CD pipeline with GitHub Actions
- Continuous deployment to Render

## 🛠️ Tech Stack

- **Python** - Primary programming language
- **Scikit-learn** - Machine learning library
- **CatBoost & XGBoost** - Gradient boosting frameworks
- **Flask** - Web application framework
- **Docker** - Containerization
- **GitHub Actions** - CI/CD pipeline
- **Render** - Cloud deployment platform
- **Docker Hub** - Container registry

## 📁 Project Structure

```
├── artifacts/               # Trained models and data files
├── notebook/               # Jupyter notebooks for EDA and model development
│   ├── data/
│   └── EDA & Model Training notebooks
├── src/                    # Source code
│   ├── components/         # Core ML components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipelines/         # Training and prediction pipelines
│   └── utils.py           # Utility functions
├── templates/             # HTML templates for web interface
├── application.py         # Flask application
├── Dockerfile            # Container configuration
├── requirements.txt      # Python dependencies
└── setup.py             # Project setup configuration
```

## 🚀 Detailed CI/CD Pipeline

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'fontFamily': 'arial' }}}%%
graph TD
    A["Developer"] -->|"1. Git Push"| B["GitHub Repository"]

    subgraph Stage1["CI Pipeline"]
        B --> C["Initialize and Checkout"]
        C --> D["Install Dependencies"]
        D --> E["Tests Pass"]
    end

    subgraph Stage2["Docker Build"]
        E --> F["Build Docker Image"]
        F --> G["Login to Docker Hub"]
        G --> H["Push to Registry"]
    end

    subgraph Stage3["Deployment"]
        H --> I["Trigger Webhook"]
        I --> J["Initialize Deploy"]
        J --> K["Health Checks"]
        K --> L["Route Traffic"]
    end

    subgraph Stage4["Monitoring"]
        L --> M["Monitor App"]
        M --> N{"Status Check"}
        N --> |"Issues"| O["Start Rollback"]
        O --> P["Previous Version"]
        N --> |"Success"| Q["Deployment Done"]
    end

    %% Dark theme styling
    classDef default fill:#2d2d2d,stroke:#7f7f7f,stroke-width:2px,color:#fff
    classDef stage1 fill:#1a365d,stroke:#4299e1,stroke-width:2px,color:#fff
    classDef stage2 fill:#1c4532,stroke:#48bb78,stroke-width:2px,color:#fff
    classDef stage3 fill:#553c9a,stroke:#9f7aea,stroke-width:2px,color:#fff
    classDef stage4 fill:#744210,stroke:#ecc94b,stroke-width:2px,color:#fff

    class Stage1 stage1
    class Stage2 stage2
    class Stage3 stage3
    class Stage4 stage4
```

### Detailed CI/CD Workflow:

1. **Stage 1: Continuous Integration**

   - Automated code checkout from GitHub
   - Python environment setup
   - Dependencies installation
   - Test suite execution
   - Code quality verification

2. **Stage 2: Docker Image Build**

   - Multi-stage Docker build process
   - Image optimization and tagging
   - Secure Docker Hub authentication
   - Image push to registry

3. **Stage 3: Render Deployment**

   - Automated webhook triggering
   - Latest image pulling
   - Container initialization
   - Health check verification
   - Zero-downtime traffic routing

4. **Stage 4: Monitoring & Rollback**
   - Continuous application monitoring
   - Performance metrics tracking
   - Automated failure detection
   - Instant rollback capability
   - Version management

### Security Measures:

- Secure environment variables
- Docker Hub authentication
- Protected deployment hooks
- Automated vulnerability scanning

### Rollback Strategy:

- Automated failure detection
- Immediate rollback trigger
- Previous version restoration
- Zero-downtime version switching

## 🔧 Setup & Installation

### Local Development

1. Clone the repository

```bash
git clone https://github.com/yourusername/student-performance-prediction.git
cd student-performance-prediction
```

2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python application.py
```

### Docker Deployment

1. Build the Docker image

```bash
docker build -t student-performance-app .
```

2. Run the container

```bash
docker run -p 5000:5000 student-performance-app
```

## 🌐 API Reference

### Prediction Endpoint

- **URL**: `/predictdata`
- **Method**: `POST`
- **Input Fields**:
  - gender
  - race_ethnicity
  - parental_level_of_education
  - lunch
  - test_preparation_course
  - reading_score
  - writing_score

## 📧 Contact

- Author: MeetInCode
- Email: mehtameet115@gmail.com

## 🐳 Docker Hub

You can also find the pre-built Docker image for this project on Docker Hub:

[https://hub.docker.com/r/thisismeet/end_to_end_mlproject](https://hub.docker.com/r/thisismeet/end_to_end_mlproject)

To pull and run the image directly, follow these steps:

1. Pull the image from Docker Hub:

   ```bash
   docker pull thisismeet/end_to_end_mlproject:latest
   ```

2. Run the container:
   ```bash
    docker run -p 5000:5000 -e PORT=5000 thisismeet/end_to_end_mlproject:latest
   ```

This will start the application and make it accessible at `http://localhost:5000`.



https://github.com/user-attachments/assets/af414ec5-b2c3-45a2-86ba-01f477d2a151



https://github.com/user-attachments/assets/5dbeacc8-fc74-4750-9db6-3c6279734322




https://github.com/user-attachments/assets/fc5dcb5f-b33e-4060-bc2d-d0f38a6e548c




