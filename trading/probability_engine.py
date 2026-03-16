class TradeProbability:

    pattern_weights = {
        "Bullish Engulfing": 75,
        "Bearish Engulfing": 75,
        "Hammer": 65,
        "Doji": 50
    }

    def calculate(self, pattern, pattern_confidence, narrative_score):

        base = self.pattern_weights.get(pattern, 50)

        pattern_score = (base * pattern_confidence) / 100

        final = pattern_score * 0.6 + narrative_score * 0.4

        if final > 80:
            action = "STRONG BUY"

        elif final > 60:
            action = "BUY"

        elif final > 40:
            action = "HOLD"

        else:
            action = "AVOID"

        return final, action
