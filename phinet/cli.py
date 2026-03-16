import argparse
import pandas as pd

from phinet import PHINetBoost, PHINetFeatureEngine


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--email_body", required=True)

    parser.add_argument("--url", default="")

    parser.add_argument("--attachment", default="")

    parser.add_argument("--email_id", default="")

    args = parser.parse_args()

    df = pd.DataFrame([{
        "email_id": args.email_id,
        "email_body": args.email_body,
        "urls": args.url,
        "attachments": args.attachment
    }])

    engine = PHINetFeatureEngine()

    X = engine.transform(df)

    model = PHINetBoost()

    model.fit(X, [1])

    prediction = model.predict(X)

    if prediction[0] == 1:

        print("⚠ Phishing Email Detected")

    else:

        print("✓ Legitimate Email")