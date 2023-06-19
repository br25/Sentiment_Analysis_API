from fastapi import FastAPI, HTTPException
from analysis.models import AnalysisRequest, AnalysisResponse
from analysis.services import perform_sentiment_analysis
from handlers.exceptions import http_exception_handler, generic_exception_handler

# Connect FastAPI
app = FastAPI()

# Import and pass the `app` object to exception handlers
http_exception_handler(app)
generic_exception_handler(app)

# Endpoint for sentiment analysis
@app.post("/analyze")
def analyze_sentiment(request: AnalysisRequest):
    # Input text
    text = request.text

    # If not text, raise an error
    if not text:
        raise HTTPException(status_code=422, detail="Invalid request: Text is missing")

    # Perform sentiment analysis on the text
    sentiment = perform_sentiment_analysis(text)
    return AnalysisResponse(sentiment=sentiment)



# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
