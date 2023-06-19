from pydantic import BaseModel

# Request body model
class AnalysisRequest(BaseModel):
    text: str

# Response model
class AnalysisResponse(BaseModel):
    sentiment: str

