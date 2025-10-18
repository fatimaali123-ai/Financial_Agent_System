from textblob import TextBlob

class AnalysisAgent:
    def analyze_sentiment(self, text_list):
        sentiments = []
        for text in text_list:
            blob = TextBlob(text)
            sentiments.append(blob.sentiment.polarity)
        avg = sum(sentiments)/len(sentiments) if sentiments else 0
        if avg > 0:
            return "Overall Positive Sentiment 😊"
        elif avg < 0:
            return "Overall Negative Sentiment 😞"
        else:
            return "Neutral Sentiment 😐"
