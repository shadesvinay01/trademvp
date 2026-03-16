# trademvp
# 🔥 MVP Trading AI

AI-powered crypto market intelligence system that combines **social sentiment, narrative detection, influencer credibility, and technical patterns** to generate high-confidence trading signals.

---

## 🚀 Overview

Sharp Trading AI analyzes market sentiment and social narratives from crypto discussions to identify **early signals before price movement happens**.

The system combines multiple AI components:

* **Sentiment Analysis** using VADER, TextBlob, and BERT
* **Narrative Detection** using NLP clustering
* **Influencer Credibility Scoring**
* **Trade Probability Engine**
* **Visualization Dashboard**

This allows traders to understand **market psychology and momentum** rather than relying only on technical indicators.

---

## 🧠 Core Features

### 1️⃣ Sentiment Analysis Engine

Uses multiple models to analyze market sentiment:

* VADER (rule-based sentiment)
* TextBlob sentiment analysis
* BERT-based deep learning model

Ensemble scoring improves accuracy for crypto-related text.

---

### 2️⃣ Narrative Detection

Identifies dominant market narratives such as:

* "Bitcoin going to $100k"
* "Market correction incoming"
* "Whales accumulating"

Uses **TF-IDF + KMeans clustering** to detect trending discussions.

---

### 3️⃣ Influencer Credibility Scoring

Evaluates influential accounts based on:

* follower count
* engagement metrics
* historical prediction accuracy

This helps identify **which voices actually move markets**.

---

### 4️⃣ Trade Probability Engine

Combines multiple signals:

```
Final Probability = 
60% Technical Pattern
40% Market Narrative
```

Alignment between social sentiment and technical signals increases confidence.

Example output:

```
Pattern: Bullish Engulfing
Narrative Score: 82
Alignment: Bullish

Final Probability: 84%
Action: STRONG BUY
```

---

## 📊 AI Components

| Component            | Purpose                            |
| -------------------- | ---------------------------------- |
| Sentiment AI         | Detect bullish / bearish sentiment |
| Narrative Clustering | Identify market narratives         |
| Influencer Scoring   | Find high-impact traders           |
| Probability Engine   | Generate trading signals           |

---

## 🏗 Project Structure

```
sharp-trading-ai/


│   ── trade_ai_clean.ipynb
│
├── models/
│   ├── sentiment.py
│   ├── narrative.py
│   ├── influencer.py
│
├── trading/
│   └── probability_engine.py
│
├── api/
│   └── twitter_stream.py
│
├── dashboard/
│   └── app.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/trading-ai.git
cd trading-ai
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the System

Run the main pipeline:

```
python main.py
```

Run the dashboard:

```
streamlit run dashboard/app.py
```

---

## 📊 Example Output

```
Tweet: "Bitcoin going to the moon!"

Sentiment: Bullish
Narrative Score: 78
Pattern: Bullish Engulfing

Final Probability: 81%
Action: STRONG BUY
```

---

## 🔮 Future Improvements

Planned upgrades:

* Real-time Twitter/X data streaming
* Reddit sentiment integration
* Crypto news sentiment analysis
* Whale wallet tracking
* On-chain analytics
* Telegram trading alerts
* AI trading assistant

---

## 🎯 Potential Use Cases

* Crypto traders
* Hedge funds
* Market research platforms
* Trading bots
* Quantitative trading strategies

---

## 👨‍💻 Author

**Sarveshwar Mandal**

AI / ML / Data Science


