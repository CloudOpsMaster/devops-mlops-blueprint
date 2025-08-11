import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import argparse
import joblib
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n-estimators', type=int, default=50)
    parser.add_argument('--max-depth', type=int, default=5)
    args = parser.parse_args()

    mlflow.set_experiment('iris-demo')
    with mlflow.start_run():
        data = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

        model = RandomForestClassifier(n_estimators=args.n_estimators, max_depth=args.max_depth, random_state=42)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        mlflow.log_param('n_estimators', args.n_estimators)
        mlflow.log_param('max_depth', args.max_depth)
        mlflow.log_metric('accuracy', acc)
        mlflow.sklearn.log_model(model, 'model')

        os.makedirs('results', exist_ok=True)
        joblib.dump(model, 'results/model.joblib')
        print(f"Accuracy: {acc}")

if __name__ == '__main__':
    main()
