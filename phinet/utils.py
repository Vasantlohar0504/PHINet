import re

SUSPICIOUS_WORDS = [
    "login", "verify", "update", "secure",
    "bank", "account", "password", "click", "confirm"
]

URGENCY_WORDS = [
    "urgent", "immediately", "action required",
    "verify now", "suspend"
]


def count_suspicious_words(text):

    if not text:
        return 0

    text = text.lower()

    return sum(word in text for word in SUSPICIOUS_WORDS)


def urgency_score(text):

    if not text:
        return 0

    text = text.lower()

    return sum(word in text for word in URGENCY_WORDS)


def contains_ip(url):

    if not url:
        return 0

    pattern = r'\d+\.\d+\.\d+\.\d+'

    return 1 if re.search(pattern, url) else 0