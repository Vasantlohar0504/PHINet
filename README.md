PHINet – Phishing Email Detection Framework 🛡️
![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)





PHINet is a Python-based phishing email detection framework designed to identify malicious emails using machine learning, feature engineering, and cybersecurity analysis techniques.

The framework analyzes email content, URLs, attachments, and sender information to detect phishing attempts and classify emails as Phishing or Legitimate.

PHINet demonstrates how machine learning and cybersecurity techniques can be combined to build an intelligent phishing detection system.

🚀 Project Overview

Phishing attacks are one of the most common cybersecurity threats. Attackers use deceptive emails to steal credentials, financial information, or sensitive data.

PHINet addresses this problem by building a lightweight phishing detection engine that processes email data and extracts features used by machine learning models to detect suspicious patterns.

The project includes:

• Email content analysis
• URL risk analysis
• Attachment risk detection
• Feature engineering for phishing indicators
• Machine learning classification model
• Modular package architecture

📊 Key Features

The PHINet framework provides:

✔ Email body analysis for suspicious keywords
✔ URL analysis to detect phishing domains
✔ Attachment risk detection
✔ Custom machine learning phishing classifier
✔ Feature engineering pipeline for email data
✔ Modular Python package design
✔ Easy integration into security tools and pipelines

🛠 Technologies Used
Technology	Purpose
Python	Core programming language
Pandas	Data processing
NumPy	Numerical operations
Scikit-learn	Machine learning model
Transformers	NLP based email analysis
PyTorch	Deep learning support
Joblib	Model serialization
⚙ Installation

Clone the repository

git clone https://github.com/Vasantlohar0504/PHINet.git

Navigate to the project folder

cd PHINet

Install dependencies

pip install -r requirements.txt

Install the package locally

pip install -e .
▶ Usage Example
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

print("Phishing" if prediction[0] else "Legitimate")
🔍 Detection Capabilities

PHINet evaluates several indicators to detect phishing attempts:

• Suspicious email keywords
• Untrusted or malicious URLs
• Risky attachment file types
• Sender domain analysis
• Email structure anomalies

These features are combined into a machine learning classification model to predict phishing probability.

🎯 Use Cases

PHINet can be used for:
• Email security systems
• Cybersecurity research
• Machine learning experimentation
• Phishing detection tools
• Educational projects in AI security



👨‍💻 Author

Vasant Lohar
Python Developer | Data Analyst | Machine Learning Enthusiast

GitHub
https://github.com/Vasantlohar0504
