import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

from .url_analyzer import URLAnalyzer
from .email_analyzer import EmailAnalyzer


class PHINetFeatureEngine:

    def __init__(self):

        self.url_analyzer = URLAnalyzer()

        self.email_analyzer = EmailAnalyzer()

        self.domain_encoder = LabelEncoder()

        self.vectorizer = TfidfVectorizer(
            max_features=200,
            stop_words="english"
        )


    def transform(self, df):

        features = []

        domains = []

        for _, row in df.iterrows():

            email_body = row.get("email_body", "")

            urls = row.get("urls", "")

            attachments = row.get("attachments", "")

            email_id = row.get("email_id", "")

            domain = self.email_analyzer.extract_domain(email_id)

            domains.append(domain)

            feature_row = {

                "body_length": self.email_analyzer.body_length(email_body),

                "suspicious_words": self.email_analyzer.suspicious_word_count(email_body),

                "urgency_score": self.email_analyzer.urgency_score(email_body),

                "url_count": self.url_analyzer.url_count(urls),

                "https_count": self.url_analyzer.https_count(urls),

                "url_suspicious": self.url_analyzer.suspicious_pattern_score(urls),

                "has_ip": self.url_analyzer.has_ip_address(urls),

                "attachment_risk": self.email_analyzer.attachment_risk(attachments)
            }

            features.append(feature_row)

        feature_df = pd.DataFrame(features)

        feature_df["sender_domain"] = self.domain_encoder.fit_transform(domains)

        text_data = df["email_body"].fillna("")

        tfidf_matrix = self.vectorizer.fit_transform(text_data)

        tfidf_df = pd.DataFrame(

            tfidf_matrix.toarray(),

            columns=self.vectorizer.get_feature_names_out()
        )

        final_features = pd.concat([feature_df, tfidf_df], axis=1)

        return final_features