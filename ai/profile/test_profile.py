from ai.profile.profile_schema import UserProfile
from ai.recommendation.engine import recommend_opportunities
from ai.knowledge_base.opportunities import OPPORTUNITIES


user = UserProfile(
    role="student",
    age=20,
    state="Haryana",
    education="B.Tech CSE",
    income=150000
)


recommendations = recommend_opportunities(
    user.to_dict(),
    OPPORTUNITIES
)


print("\nAdhikarSetu Recommendations\n")

for opportunity in recommendations:
    print(f"📌 {opportunity['title']}")
    print(f"Type: {opportunity['type']}")
    print(f"Match Score: {opportunity['score']}")

    print("Why recommended:")

    for reason in opportunity["reasons"]:
        print(f"- {reason}")

    print()