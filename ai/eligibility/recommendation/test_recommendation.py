from ai.eligibility.recommendation.engine import recommend_opportunities
from ai.knowledge_base.opportunities import OPPORTUNITIES


user = {
    "role": "student",
    "age": 20,
    "state": "Haryana",
    "education": "B.Tech CSE",
    "income": 150000
}


recommendations = recommend_opportunities(
    user,
    OPPORTUNITIES
)


print("\nRecommended Opportunities:\n")

for opportunity in recommendations:
    print(f"{opportunity['title']} ({opportunity['type']})")
    print(f"Match Score: {opportunity['score']}")

    for reason in opportunity["reasons"]:
        print(f"- {reason}")

    print()
    