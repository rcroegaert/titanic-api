import lightgbm as lgb
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split


df_train = (pd.read_csv('../data/train.csv'))
df_train['Sex'] = df_train['Sex'].map({'male': 0, 'female': 1})
df_train.drop(["PassengerId","Cabin","Ticket","Name"],inplace=True,axis=1)
df_train = df_train[["Pclass", "Sex", "Age", "Fare", "Survived"]].dropna()

X = df_train.drop('Survived', axis=1)
y = df_train['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = lgb.LGBMClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
print("Model trained and saved to app/model.pkl")