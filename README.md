# Content-Monetization-Modeler

🎬 Project Overview: YouTube Ad Revenue Prediction

🔹 Problem Statement
As video creators and media companies increasingly rely on platforms like YouTube for income, predicting potential ad revenue becomes essential for business planning and content strategy.
 The task is to build a Linear Regression model that can accurately estimate YouTube ad revenue for individual videos based on various performance and contextual features, and implement the results in a simple Streamlit web application.
🔹 Objective
The goal of this project is to predict YouTube ad revenue (in USD) using both numerical and categorical features derived from video performance metrics and metadata. By building a regression-based machine learning model and deploying it as a web app, the project provides a tool for estimating ad revenue given engagement statistics.
⚙️ Technical Stack
🔹 Programming Language
Python 3.9+ → Main language for data processing, modeling, and app development.



🔹 Data Handling & Analysis
Pandas → For loading, cleaning, and manipulating structured data.


NumPy → For numerical computations and efficient array operations.



🔹 Machine Learning
scikit-learn → Core library used for:


Train-test split (train_test_split)


Preprocessing (StandardScaler, OneHotEncoder, ColumnTransformer)


Modeling (LinearRegression, SVR, LinearSVR)


Evaluation (r2_score, mean_absolute_error, mean_squared_error)


Pickle → For saving and loading the trained machine learning pipeline.



🔹 Model Development Environment
Jupyter Notebook (youtube.ipynb) → Used for exploration, feature engineering, training, evaluation, and visualization during development.



🔹 Deployment
Streamlit → To build the interactive web application (model.py).


Provides input forms for video stats (views, likes, comments, etc.).


Calls the trained ML model pipeline for real-time prediction.


Displays predicted ad revenue in an intuitive UI.



🔹 Visualization (if used in Notebook)
Matplotlib / Seaborn → For exploratory data analysis, correlations, and performance plots.



🔹 Infrastructure
Local machine or cloud (can run on Anaconda / VSCode / PyCharm) for development.


Deployment-ready via Streamlit Cloud or other hosting platforms (Heroku, AWS, GCP, etc.).

