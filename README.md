# Auto MPG Fuel Efficiency Predictor 

A modular, production-ready machine learning pipeline designed to predict vehicle fuel consumption (**Miles Per Gallon - MPG**) based on structural and performance attributes. This project migrates experimental analytics from a Jupyter Notebook workflow into decoupled, testable Python core scripts.

---
# Project Directory Structure:

```
text
auto_mpg/
├── data/
│   └── auto_mpg.py           # Core dataset ingestion utility
├── notebook/
│   └── eda.ipynb             # Exploratory Data Analysis & data profiling
└── src/
    ├── data_preprocessing.py # Functional data cleaning & transformation 
    └── model.py              # Scaling, model training, and metrics pipeline
```

---
# Pipeline Architecture & Implementation:

## 1. Exploratory Data Analysis 
### (notebook/eda.ipynb)
Initial data mining revealed that the dataset consists of 398 entries mapping 9 features. Data profiling identified:

Feature Filtering: Categorical string descriptors (like car_name) were identified as non-contributing dimensions to standard linear baselines and slated for extraction.

Data Integrity: Discovered 6 null records isolated within the horsepower feature index.

## 2. Isolated Transformation Layer 
### (src/data_preprocessing.py)
Encapsulates functional modifications to maintain downstream feature consistency:

Dtype Cleanup: Dynamically drops all text column boundaries (str data types) from the data frame matrix.

Robust Imputation: Uses a Scikit-Learn SimpleImputer leveraging a column based mean calculation strategy to resolve missing fields.

Array Split: Separates the predictive independent matrix (X) from the target feature array (y or mpg).

## 3. Training & Scaling Sequence 
### (src/model.py)
An entry point executable that loads, partitions, targets, and models input parameters:

Data Partitioning: Splits the array structures via an 80/20 train-test configuration anchored to a static random state parameter (42).

Feature Standardization: Fits a StandardScaler strictly onto the X_train structure to compute tracking distribution weights before applying a data transformation to both the train and test subsets. This shields the validation dataset from arbitrary data leakage.

Regression Analysis: Initializes and fits an ordinary least squares LinearRegression baseline.

---
# Model Evaluation & Metrics

The pipeline evaluates performance against test configurations containing 318 training instances across 7 standardized input variables.

## Performance Summary

| Metric Framework | Baseline Score | Practical Significance |
| :--- | :--- | :--- |
| **Coefficient of Determination ($R^2$)** | `0.8476` | The inputs account for ~84.8% of variance in vehicle fuel mileage. |
| **Mean Absolute Error (MAE)** | `2.2534` | The average expected variation between target values and predictions is ±2.25 MPG. |
| **Mean Squared Error (MSE)** | `8.1955` | Average squared prediction discrepancy; emphasizes outlier variance weightings. |
| **Root Mean Squared Error (RMSE)** | `2.8628` | Quantifiable standard deviation of residuals mapped back to the default MPG scale. |

---
# Getting Started & Execution
## 1. Cloning Github Repo:
Clone this repository to a local machine:

```bash
git clone https://github.com/itshowrohitworks/auto_mpg.git
cd auto_mpg
```

## 2. Enviornment Setup and Installing dependencies:
Install uv virtual env and install required dependencies:

```bash
uv venv

source .venv/bin/activate

uv pip install -r requirements.txt
```

## 3. Execute the Pipeline Script
To run the automated module sequence from ingestion to logging final metrics, run the following statement from the root directory:

```bash
python -m src.model
```
---