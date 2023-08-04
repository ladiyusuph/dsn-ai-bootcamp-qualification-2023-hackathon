# DSN AI Bootcamp Qualification 2023 - Hackathon

## Date: August 4, 2023

## Project Overview:
In response to a challenge posed by DSN about Wazobia Real Estate Limited, the leading real estate company in Nigeria, this project aimed to tackle the crucial task of accurately predicting house prices in the current market. The mission was to develop a powerful and accurate predictive model that could estimate house prices in Nigeria, enabling Wazobia Real Estate Limited to provide competitive and precise pricing for its customers.

## Objective:
The primary objective of this hackathon was to create a robust predictive model using the provided dataset. The goal was to analyze various factors influencing house prices, uncover meaningful patterns, and construct a model capable of generating reliable price predictions. By accomplishing this, the project sought to empower Wazobia Real Estate Limited with data-driven insights, allowing the company to make informed pricing decisions, enhance its competitive position in the market, and deliver superior value to its customers.

## Key Findings:
### Data Preprocessing:
The initial dataset required preprocessing steps to handle missing values, encode categorical variables, and normalize numerical features. We split the data into training and testing sets to evaluate the model's performance effectively.

### Model Selection:
Several regression models were evaluated for this task, including Linear Regression, Support Vector Regression (SVR), XGBoost, LightGBM, and a Neural Network. GridSearchCV was used to tune hyperparameters for SVR, XGBoost, and LightGBM to improve their performance.

### Model Performance:
- Linear Regression: The initial baseline model achieved a Root Mean Squared Error (RMSE) of 593035.867 on the test set.
- SVR: After hyperparameter tuning, the best SVR model achieved an RMSE of 1051507.154 on the test set, outperforming the linear regression model.
- XGBoost: The best XGBoost model, with optimized hyperparameters, achieved an RMSE of 582000.141 on the test set, showing further improvement over both linear regression and SVR.
- LightGBM: The best LightGBM model obtained an RMSE of 580830.0696 on the test set, demonstrating the best performance among all evaluated models.
- Neural Network: The Neural Network model achieved an RMSE of 572593.245 on the test set, showing competitive performance compared to other models.

## Conclusion:
In conclusion, the predictive model using the Neural Network algorithm outperformed the other models slightly, including XGBoost, and provided the most accurate estimates of house prices in Nigeria. The LightGBM algorithm with an RMSE of 580830.0696, showed promise as a viable alternative to the Neural Network model for this prediction task.

## Recommendations:
To further enhance the model's performance, additional data could be incorporated, such as economic indicators, crime rates, and proximity to amenities. Moreover, further tuning of the Neural Network architecture and hyperparameters could potentially improve its predictive accuracy.

## Limitations:
While the models achieved promising results, there are still limitations to consider. The accuracy of the predictions may vary based on fluctuations in the real estate market and other external factors not accounted for in the dataset.

## Future Work:
For future work, the models could be deployed in a real-world environment, and their performance can be continuously monitored and fine-tuned. Additionally, gathering more recent data and experimenting with different Neural Network architectures could further improve predictive performance.
