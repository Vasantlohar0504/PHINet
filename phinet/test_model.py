import pandas as pd

from phinet import PHINetBoost, PHINetFeatureEngine


def test_prediction():

    df = pd.DataFrame([{

        "email_id": "scammer@fakebank.com",

        "email_body": "Urgent verify your bank account immediately",

        "urls": "http://fakebank-login.com",

        "attachments": "dangerous.zip"
    }])

    engine = PHINetFeatureEngine()

    X = engine.transform(df)

    model = PHINetBoost()

    model.fit(X, [1])

    prediction = model.predict(X)

    assert prediction[0] == 1