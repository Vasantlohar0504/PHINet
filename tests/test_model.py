import pandas as pd
from phinet import PHINetBoost, PHINetFeatureEngine

df = pd.DataFrame([{
    "email_id": "scammer@fakebank.com",
    "email_body": "Verify your account immediately",
    "urls": "http://fakebank-login.com",
    "attachments": "dangerous.zip"
}])

engine = PHINetFeatureEngine()

X = engine.transform(df)

model = PHINetBoost()

model.fit(X, [1])

prediction = model.predict(X)

print(prediction)