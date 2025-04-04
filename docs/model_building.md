# Model Building

This page explains how the LightGBM model was trained for the Titanic survival prediction task.

-------

## Dataset
The model is trained on the classic [Titanic dataset](https://www.kaggle.com/c/titanic), 
which contains information about passengers from the Titanic and whether they survived or not.

Here is a small sample of the dataset:

![image](/img/DatasetSample.png)

### Features used for training

- `Pclass` – Passenger class (1 = first, 2 = second, 3 = third)
- `Sex` – Gender (where 0 = male, 1 = female)
- `Age` – Passenger's age in years
- `Fare` – Ticket fare

### Target

#### Target during training
- `Survived` – Survival status (0 = No, 1 = Yes)

#### Target predicted by the model
- `Survival probability` – Probability value (0 to 1)'

-------

## Preprocessing
The preprocessing steps include:

- Converted `Sex` from string to integer (`male` → `0`, `female` → `1`)
- Removed rows with missing values in selected columns

-------

## Model Training
This model is trained on selected Titanic features, using [`LightGBM classifier](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMClassifier.html),
and later used in a FastAPI app for real-time prediction.

=== "Python"
    ```python
    from lightgbm import LGBMClassifier
    
    model = LGBMClassifier()
    model.fit(X_train, y_train)
    ```

------

## Saving and Loading the Model
To reuse the trained model in the API, it is serialized and saved as a pickle file to disk using the 
[`joblib`](https://joblib.readthedocs.io/en/latest/index.html) library:

#### Save the Model
=== "Python"
    ```python
    import joblib
    
    joblib.dump(model, 'model.pkl')
    ```

#### Load the Model
Once saved, the model can be loaded in the FastAPI application like this:

=== "Python"

    ```python
    import joblib
    
    model = joblib.load('model.pkl')
    ```
This allows the API to use the trained model for making predictions without needing to retrain it each time.
