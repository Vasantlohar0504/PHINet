import numpy as np
import joblib

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier

from .bert_detector import BERTPhishingDetector


class PHINetBoost:

    def __init__(self, n_estimators=150):

        # Traditional ML models
        self.model1 = GradientBoostingClassifier(
            n_estimators=n_estimators
        )

        self.model2 = RandomForestClassifier(
            n_estimators=n_estimators
        )

        # AI Deep Learning Model
        self.bert = BERTPhishingDetector()

        self.is_trained = False


    # -----------------------------
    # Train ML Models
    # -----------------------------
    def fit(self, X, y):

        self.model1.fit(X, y)

        self.model2.fit(X, y)

        self.is_trained = True


    # -----------------------------
    # Basic Ensemble Prediction
    # -----------------------------
    def predict(self, X):

        if not self.is_trained:

            raise Exception("Model must be trained before prediction")

        p1 = self.model1.predict(X)

        p2 = self.model2.predict(X)

        final_predictions = []

        for i in range(len(p1)):

            if p1[i] + p2[i] >= 1:

                final_predictions.append(1)

            else:

                final_predictions.append(0)

        return np.array(final_predictions)


    # -----------------------------
    # Prediction Probability
    # -----------------------------
    def predict_proba(self, X):

        prob1 = self.model1.predict_proba(X)

        prob2 = self.model2.predict_proba(X)

        final_prob = (prob1 + prob2) / 2

        return final_prob


    # -----------------------------
    # AI Enhanced Prediction
    # -----------------------------
    def predict_with_ai(self, X, email_text):

        if not self.is_trained:

            raise Exception("Model must be trained before prediction")

        ml_prediction = self.predict(X)[0]

        bert_prediction = self.bert.predict(email_text)

        # Ensemble decision
        if ml_prediction + bert_prediction >= 1:

            return 1

        return 0


    # -----------------------------
    # Save Model
    # -----------------------------
    def save(self, path="phinet_model.pkl"):

        joblib.dump(
            {
                "model1": self.model1,
                "model2": self.model2
            },
            path
        )


    # -----------------------------
    # Load Model
    # -----------------------------
    def load(self, path="phinet_model.pkl"):

        data = joblib.load(path)

        self.model1 = data["model1"]

        self.model2 = data["model2"]

        self.is_trained = True