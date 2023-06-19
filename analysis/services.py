from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the pre-trained tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
model = AutoModelForSequenceClassification.from_pretrained("StatsGary/setfit-ft-sentinent-eval")

# Perform sentiment analysis on the text
def perform_sentiment_analysis(text):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    outputs = model(**inputs)
    predictions = outputs.logits.argmax(dim=1)
    sentiment_labels = ["positive", "negative", "neutral"]
    sentiment = sentiment_labels[predictions.item()]
    return sentiment