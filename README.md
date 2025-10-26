# honey-production-analysis
Analyzing the decline of US honey production with machine learning - forecasting future trends using linear regression.

*honey-production-analysis*

Analyzing the decline of US honey production with machine learning - forecasting future trends using linear regression.
 Honey Production Trend Analysis & Future Prediction

 *Project Overview*
This project analyzes historical honey production data in the United States and uses a linear regression model to forecast future production trends. The analysis reveals a significant decline in honey production over time and projects this trend into the future, offering a data-driven perspective on a critical agricultural and environmental issue.

 *Objectives*
- To explore and visualize the historical trend of honey production in the U.S.
- To build a simple linear regression model that captures this trend.
- To use the model to predict future honey production levels from 2013 to 2050.

 *Tools & Technologies*
- Language: Python
- Libraries: Pandas, NumPy, Matplotlib, Scikit-learn
- Methodology: Linear Regression, Data Visualization

 *Key Steps*
1.  Data Loading & Exploration: Loaded and inspected the honey production dataset.
2.  Data Preparation: Aggregated the data to find the mean total production per year.
3.  Visualization: Created a scatter plot to visualize the clear downward trend.
4.  Model Building: Implemented a Linear Regression model from Scikit-learn.
5.  Model Evaluation: Plotted the regression line against historical data to validate the model's fit.
6.  Future Prediction: Generated and visualized predictions for honey production up to the year 2050.

 *Results & Conclusion*
The linear regression model identified a strong negative trend in honey production. The analysis leads to a concerning conclusion:

If the historical rate of decline continues, honey production in the United States is projected to fall to critically low levels by 2050.

This project serves as a demonstration of using basic machine learning for time-series forecasting and sheds light on an important real-world problem that may be linked to factors such as colony collapse disorder, pesticide use, and habitat loss.

 *How to Run*
1.  Ensure you have the required libraries installed:
    ```bash
    pip install pandas numpy matplotlib scikit-learn
    ```
2.  Clone this repository and run the `honey_production_analysis.py` script.
3.  The script will generate three plots:
    - A scatter plot of historical data.
    - A scatter plot with the linear regression line.
    - A line plot of future predictions.

 *Dataset*
The dataset `honeyproduction.csv` was provided by Codecademy and contains historical records of honey production by state in the U.S.

