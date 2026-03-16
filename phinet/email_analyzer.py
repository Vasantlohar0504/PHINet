from .utils import count_suspicious_words, urgency_score


class EmailAnalyzer:

    def body_length(self, text):

        if not text:
            return 0

        return len(text)


    def suspicious_word_count(self, text):

        return count_suspicious_words(text)


    def urgency_score(self, text):

        return urgency_score(text)


    def attachment_risk(self, attachments):

        if not attachments:
            return 0

        risky = [".exe", ".zip", ".bat", ".scr"]

        for ext in risky:

            if ext in attachments.lower():

                return 1

        return 0


    def extract_domain(self, email):

        try:

            return email.split("@")[1]

        except:

            return "unknown"