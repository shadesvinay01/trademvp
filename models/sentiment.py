from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

class SentimentAnalyzer:

    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()

        try:
            self.bert = pipeline(
                "sentiment-analysis",
                model="finiteautomata/bertweet-base-sentiment-analysis"
            )
        except:
            self.bert = None

    def vader_analysis(self, text):
        score = self.vader.polarity_scores(text)["compound"]

        if score > 0.05:
            return "bullish"
        elif score < -0.05:
            return "bearish"

        return "neutral"

    def textblob_analysis(self, text):

        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0.1:
            return "bullish"

        if polarity < -0.1:
            return "bearish"

        return "neutral"

    def bert_analysis(self, text):

        if not self.bert:
            return "neutral"

        result = self.bert(text)[0]

        if result["label"] == "POS":
            return "bullish"

        if result["label"] == "NEG":
            return "bearish"

        return "neutral"

    def ensemble(self, text):

        votes = [
            self.vader_analysis(text),
            self.textblob_analysis(text),
            self.bert_analysis(text)
        ]

        return max(set(votes), key=votes.count)
