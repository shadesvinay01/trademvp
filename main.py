from models.sentiment import SentimentAnalyzer

tweets = [
    "Bitcoin to the moon!",
    "BTC looks weak today",
    "Ethereum consolidating"
]

model = SentimentAnalyzer()

for t in tweets:

    print(t, "->", model.ensemble(t))
