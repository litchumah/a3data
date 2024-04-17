from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import joblib

def run_pipeline():
    iris = datasets.load_iris()

    X_train, X_test, y_train, y_test = train_test_split(iris.get('data'), iris.get('target'), test_size=0.2, random_state=42)

    models = {
        'svm': SVC(),
        'random_forest': RandomForestClassifier(),
        'logistic_regression': LogisticRegression(max_iter=400),
    }

    param_grids = {
        'svm': {'C': [0.1, 1, 10], 'gamma': [0.1, 1, 10]},
        'random_forest': {'n_estimators': [50, 100, 200]},
        'logistic_regression': {'C': [0.1, 1, 10]},
    }

    best_model = {}
    for model_name, model in models.items():
        grid_search = GridSearchCV(model, param_grids[model_name], cv=5)
        grid_search.fit(X_train, y_train)
        print(f"Best parameters for {model_name}: {grid_search.best_params_}")
        print(f"Best cross-validation score for {model_name}: {grid_search.best_score_}")
        print(f"Test accuracy for {model_name}: {grid_search.score(X_test, y_test)}")
        print("*"*40)
        if best_model:
            if best_model['score'] < grid_search.best_score_:
                best_model.clear()
                best_model['model_name'] = model_name
                best_model['model'] = grid_search
                best_model['score'] = grid_search.best_score_
            else:
                pass
        else:
            best_model['model_name'] = model_name
            best_model['model'] = grid_search
            best_model['score'] = grid_search.best_score_

    joblib.dump(best_model['model'], f'{best_model["model_name"]}.pkl')
    return f'{best_model["model_name"]}.pkl'
