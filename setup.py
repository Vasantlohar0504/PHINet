from setuptools import setup, find_packages

setup(
    name="phinet",
    version="1.0.0",
    description="Advanced phishing email detection package using ML and AI",
    author="Vasant Lohar",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "transformers",
        "torch",
        "joblib"
    ],
    entry_points={
        "console_scripts": [
            "phinet-scan=phinet.cli:main"
        ]
    },
    python_requires=">=3.8",
)