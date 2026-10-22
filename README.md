# Machine Learning Algorithms

This repository contains machine learning implementations developed in Python using Jupyter notebooks. It covers regression, classification, clustering, and natural language processing (NLP), with each algorithm evaluated using appropriate performance metrics.

## Implemented Algorithms

### 1. Regression
Time-series modelling and prediction using:
- Linear Regression
- Polynomial Regression

### 2. Classification
Supervised learning algorithms for classification tasks:
- Logistic Regression
- Decision Tree
- Random Forest Classifier
- Support Vector Machine (SVM)
- AdaBoost

### 3. Clustering
Unsupervised learning algorithms for identifying patterns and groups in data:
- K-Means
- DBSCAN

### 4. Natural Language Processing (NLP)
Text analysis and sentiment classification using:
- TextBlob for sentiment analysis
- Logistic Regression
- Neural Networks

## Getting Started

The notebooks can be executed directly in Google Colab or in a locally configured Python environment.

### Option 1: Google Colab

1. Open the desired `.ipynb` notebook in Google Colab.
2. Upload the required datasets, if applicable.
3. Install any additional dependencies specified in the notebook.
4. Run the notebook cells sequentially.

### Option 2: Local Python Environment

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install the required dependencies.
4. Launch Jupyter Notebook or JupyterLab.
5. Open the desired notebook and execute the cells.

Example setup:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

Activate the environment on Linux:

```bash
source .venv/bin/activate
```

Install the core libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter textblob
```

Additional libraries may be required depending on the notebook, particularly for neural network implementations.

Launch Jupyter Notebook:

```bash
jupyter notebook
```

## Model Evaluation

Each algorithm is evaluated using methods appropriate to its task, which may include:

- **Regression:** MAE, MSE, RMSE and \(R^2\).
- **Classification:** Accuracy, precision, recall, F1-score and confusion matrices.
- **Clustering:** Silhouette score and other suitable clustering evaluation methods.
- **NLP and sentiment analysis:** Classification metrics and sentiment prediction analysis, where applicable.

The evaluation methods used depend on the algorithm, dataset and problem being addressed.

## Technologies

- Python
- Jupyter Notebook
- Google Colab
- NumPy and Pandas
- Matplotlib and Seaborn
- Scikit-learn
- TextBlob
- Neural network frameworks, where required
