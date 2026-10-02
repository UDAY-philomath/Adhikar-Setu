from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from ai.recommendation.engine import recommend_opportunities
from ai.knowledge_base.opportunities import OPPORTUNITIES


app = FastAPI(
    title="AdhikarSetu Intelligence API",
    description="Recommendation service for AdhikarSetu",
    version="0.1.0"
)


class UserProfileRequest(BaseModel):
    role: Optional[str] = None
    age: Optional[int] = None
    state: Optional[str] = None
    education: Optional[str] = None
    income: Optional[float] = None


@app.get("/")
def root():
    return {
        "message": "AdhikarSetu Intelligence API is running"
    }


@app.post("/recommend")
def recommend(profile: UserProfileRequest):
    result = recommend_opportunities(
        profile.model_dump(),
        OPPORTUNITIES,
    )

    return result