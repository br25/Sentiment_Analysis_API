# Sentiment Analysis API

This project implements a web API for performing sentiment analysis on text inputs. It utilizes a pre-trained model to predict the sentiment of the provided text, categorizing it as positive, negative, or neutral.

## Prerequisites

- Python 3.6 or higher
- Virtual environment tool (e.g., virtualenv)

## Installation
1. Create a virtual environment:
   - `virtualenv venv`
   - `source venv/bin/activate`

2. Install packages:
   - `pip install -r requirements.txt`

## Usage
3. Run the web server:
   - `uvicorn main:app --reload`

4. Open your Browser and put this link:
   - [http://127.0.0.1:8000/docs#/]

5. Type your Text in this format:
   ```json
   {
     "text": "Your input text goes here"
   }

# Output
6. The Output is:
    {
      "sentiment": "positive/negative/neutral"
    }