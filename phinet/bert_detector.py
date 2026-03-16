from transformers import BertTokenizer, BertForSequenceClassification
import torch


class BERTPhishingDetector:

    def __init__(self):

        self.tokenizer = BertTokenizer.from_pretrained(
            "bert-base-uncased"
        )

        self.model = BertForSequenceClassification.from_pretrained(
            "bert-base-uncased",
            num_labels=2
        )

        self.model.eval()


    def preprocess(self, text):

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=256
        )

        return inputs


    def predict(self, text):

        inputs = self.preprocess(text)

        with torch.no_grad():

            outputs = self.model(**inputs)

        logits = outputs.logits

        prediction = torch.argmax(logits, dim=1).item()

        return prediction