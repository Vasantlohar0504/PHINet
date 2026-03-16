from urllib.parse import urlparse
from .utils import contains_ip


class URLAnalyzer:

    def url_count(self, urls):

        if not urls:
            return 0

        return len(urls.split())


    def https_count(self, urls):

        if not urls:
            return 0

        return urls.count("https")


    def suspicious_pattern_score(self, urls):

        if not urls:
            return 0

        patterns = [
            "login",
            "verify",
            "secure",
            "update",
            "bank"
        ]

        score = 0

        for p in patterns:

            if p in urls.lower():

                score += 1

        return score


    def has_ip_address(self, urls):

        return contains_ip(urls)


    def extract_domain(self, url):

        try:

            parsed = urlparse(url)

            return parsed.netloc

        except:

            return "unknown"