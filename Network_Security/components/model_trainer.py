import os
import sys

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging

from Network_Security.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from Network_Security.entity.config_entity import ModelTrainerConfig

from Network_Security.utils.main_utils.utils import save_object,load_object
from Network_Security.utils.main_utils.utils import load_numpy_array_data,evaluate_models

from Network_Security.utils.ml_utils.metric.classification_metric import get_classification_score
from Network_Security.utils.ml_utils.model.estimator import NetworkModel


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (AdaBoostClassifier,RandomForestClassifier,GradientBoostingClassifier)
import mlflow


import dagshub
dagshub.init(repo_owner='Coder-Aditya05', repo_name='Network_Security', mlflow=True)

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig, data_transformation_artifact: DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def track_ml_flow(self, best_model, classification_train_metric, classification_test_metric):
        

        with mlflow.start_run():
            mlflow.log_metric("train_f1_score",        classification_train_metric.f1_score)
            mlflow.log_metric("train_precision_score", classification_train_metric.precision_score)
            mlflow.log_metric("train_recall_score",    classification_train_metric.recall_score)
            mlflow.log_metric("test_f1_score",         classification_test_metric.f1_score)
            mlflow.log_metric("test_precision_score",  classification_test_metric.precision_score)
            mlflow.log_metric("test_recall_score",     classification_test_metric.recall_score)
            mlflow.log_param("model_name", type(best_model).__name__)
            mlflow.sklearn.log_model(best_model, "model")

    def train_model(self, X_train, y_train, X_test, y_test):
        models = {
            "Random Forest":       RandomForestClassifier(verbose=1),
            "Logistic Regression": LogisticRegression(verbose=1),
            "Adaboost":            AdaBoostClassifier(),
            "Gradient Boosting":   GradientBoostingClassifier(verbose=1),
            "Decision Tree":       DecisionTreeClassifier()
        }

        params = {
            "Decision Tree":       {'criterion': ['gini', 'entropy', 'log_loss']},
            "Random Forest":       {'n_estimators': [8, 16, 32, 62, 128, 256]},
            "Gradient Boosting":   {
                'learning_rate': [.1, .01, .05, .001],
                'subsample':     [0.6, 0.7, 0.75, 0.80, 0.85, 0.90],
                'n_estimators':  [8, 16, 32, 64, 128, 256]
            },
            "Logistic Regression": {},
            "Adaboost":            {
                'learning_rate': [.1, .01, 0.5, .001],
                'n_estimators':  [8, 16, 32, 64, 128, 256]
            }
        }

        model_report: dict = evaluate_models(X_train, y_train, X_test, y_test, models=models, params=params)

        best_model_name  = max(model_report, key=model_report.get)
        best_model_score = model_report[best_model_name]
        best_model       = models[best_model_name]
        best_model.fit(X_train, y_train)

        y_train_pred = best_model.predict(X_train)
        y_test_pred  = best_model.predict(X_test)

        classification_train_metric = get_classification_score(y_true=y_train, y_pred=y_train_pred)
        classification_test_metric  = get_classification_score(y_true=y_test,  y_pred=y_test_pred)

        # ✅ Single run logs both train and test metrics together
        self.track_ml_flow(best_model, classification_train_metric, classification_test_metric)

        preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)
        model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
        os.makedirs(model_dir_path, exist_ok=True)

        Network_Model = NetworkModel(preprocessor=preprocessor, model=best_model)
        save_object(self.model_trainer_config.trained_model_file_path, obj=Network_Model)

        save_object("final_model/model.pkl",best_model)

        model_trainer_artifact = ModelTrainerArtifact(
            trained_model_file_path=self.model_trainer_config.trained_model_file_path,
            train_metric_artifact=classification_train_metric,
            test_metric_artifact=classification_test_metric
        )

        logging.info(f"Model Trainer Artifact: {model_trainer_artifact}")
        return model_trainer_artifact

    def initate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path  = self.data_transformation_artifact.transformed_test_file_path

            train_arr = load_numpy_array_data(train_file_path)
            test_arr  = load_numpy_array_data(test_file_path)

            X_train, y_train, X_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1],
            )

            return self.train_model(X_train, y_train, X_test, y_test)
        except Exception as e:
            raise NetworkSecurityException(e, sys)