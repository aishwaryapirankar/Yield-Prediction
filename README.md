# Robust Yield Prediction for Food Processing Farms

## Overview

This project aims to develop a robust machine learning model to predict the output of food processing farms for the next year. The model will be crucial for optimizing the supply chain management system of a fast-food chain, ensuring efficient ingredient sourcing and preventing shortages. Additionally, a strategy will be devised for sourcing a specific ingredient type, 'ing_w,' based on forecasted demand, considering a one-month lead time and the ingredient's shelf life of at least 8 months.

## Dataset Information

### `train_data.csv`

- **date:** Timestamp of yield measurement
- **farm_id:** Identifier for the food processing farm
- **ingredient_type:** Type of ingredient being produced
- **yield:** Yield of the plant in tonnes

### `farm_data.csv`

- **farm_id:** Identifier for the food processing farm
- **founding_year:** The year operations commenced on the farm and food processing plant
- **num_processing_plants:** Number of processing plants on the farm
- **farm_area:** Area of the farm in square meters
- **farming_company:** Company that owns the farms
- **deidentified_location:** Location of the farm

### `train_weather.csv`

- Weather data for each location where farms are present, provided by timestamp

### `test_data.csv` and `test_weather.csv`

- Similar to train data and weather data, provided for testing the model

## Objectives

1. **Explore and Feature Engineering:**
   - Analyze and explore the provided datasets.
   - Engineer new features that might impact yield predictions.

2. **Prediction:**
   - Build machine learning models to predict the yield for each farm during the given timestamps.

3. **Sourcing Strategy:**
   - Given the forecasted demand for 'ing_w,' devise a sourcing strategy.
   - Conditions:
      - Source the ingredient at least one month before the required date.
      - The ingredient should have a shelf life of at least 8 months.

## Implementation

1. **Data Exploration:**
   - Explore and understand the datasets, identifying patterns and potential correlations.

2. **Feature Engineering:**
   - Create new features that might enhance the predictive power of the models.

3. **Model Training:**
   - Train machine learning models to predict yields based on historical data.

4. **Evaluation:**
   - Evaluate model performance using appropriate metrics.

5. **Sourcing Strategy:**
   - Develop a sourcing strategy for 'ing_w' based on the forecasted demand, considering lead time and shelf life.
