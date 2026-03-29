# CodeAlpha_SalesPrediction
CodeAlpha Internship Project - Sales Prediction using Machine Learning
# 📊 Sales Prediction using Machine Learning - CodeAlpha

This project is developed as part of the CodeAlpha Internship.  
It predicts product sales based on advertising budget using Machine Learning techniques.

## 📌 Project Overview
The goal of this project is to build a regression model that predicts sales based on advertising expenditure on different platforms.

### Input Features:
- TV Advertising Budget  
- Radio Advertising Budget  
- Newspaper Advertising Budget  

### Output:
- Predicted Sales  

## ⚙️ Features
- Data preprocessing and cleaning  
- Regression model using Linear Regression  
- Model evaluation using R² score and MAE  
- Visualization of actual vs predicted sales  
- Analysis of feature impact on sales  
- Manual input prediction for real-time results  

## 🧠 Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  
## 📂 Dataset
The dataset contains:
- TV advertising budget  
- Radio advertising budget  
- Newspaper advertising budget  
- Sales  

## 🚀 How to Run

1. Install required libraries:

pip install pandas scikit-learn matplotlib

2. Place dataset file:

Advertising.csv

3. Run the program:

python Sales_Prediction.py


## 📊 Model Used
Linear Regression
##output
First 5 rows:
    Unnamed: 0     TV  Radio  Newspaper  Sales
0           1  230.1   37.8       69.2   22.1
1           2   44.5   39.3       45.1   10.4
2           3   17.2   45.9       69.3    9.3
3           4  151.5   41.3       58.5   18.5
4           5  180.8   10.8       58.4   12.9

Columns:
 Index(['Unnamed: 0', 'TV', 'Radio', 'Newspaper', 'Sales'], dtype='str')

Model Performance:
Accuracy (R2): 89.94%
MAE: 1.4607567168117603

Sample Predictions:
Actual: 16.9 Predicted: 16.41
Actual: 22.4 Predicted: 20.89
Actual: 21.4 Predicted: 21.55
Actual: 7.3 Predicted: 10.61
Actual: 24.7 Predicted: 22.11

--- Predict New Sales ---
Enter TV advertising budget: 300
Enter Radio advertising budget: 200
Enter Newspaper advertising budget: 200

📈 Predicted Sales: 54.79 

