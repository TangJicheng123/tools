import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

db = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

model = mlflow.sklearn.load_model("runs:/0/3a3989086ad544cb9302852955a53c8c/artifacts/model/model.pkl")
predictions = model.predict(X_test)
print(predictions)