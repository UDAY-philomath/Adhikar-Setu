def check_eligibility(user, opportunity):
    reasons = []
    missing_information = []

    # Check age
    if "age" not in user:
        missing_information.append("age")
    else:
        if "min_age" in opportunity and user["age"] < opportunity["min_age"]:
            reasons.append("Age is below the minimum requirement.")

        if "max_age" in opportunity and user["age"] > opportunity["max_age"]:
            reasons.append("Age is above the maximum requirement.")

    # Check state
    if "state" not in user:
        missing_information.append("state")
    elif "states" in opportunity:
        if user["state"] not in opportunity["states"]:
            reasons.append("State does not match the opportunity.")

    # Check education
    if "education" not in user:
        missing_information.append("education")
    elif "education" in opportunity:
        if user["education"] not in opportunity["education"]:
            reasons.append("Education does not match the opportunity.")

    # Check income
    if "income" not in user:
        missing_information.append("income")
    elif "income_limit" in opportunity:
        if user["income"] > opportunity["income_limit"]:
            reasons.append("Income is above the allowed limit.")

    # Determine final status
    if missing_information:
        status = "MORE_INFORMATION_REQUIRED"
    elif reasons:
        status = "NOT_ELIGIBLE"
    else:
        status = "ELIGIBLE"

    return {
        "status": status,
        "reasons": reasons,
        "missing_information": missing_information
    }
from ai.eligibility.engine import check_eligibility


def recommend_opportunities(user, opportunities):
    recommendations = []

    for opportunity in opportunities:

        # Check eligibility first
        eligibility = check_eligibility(user, opportunity)

        if eligibility["status"] != "ELIGIBLE":
            continue

        score = 0
        reasons = []

        # Role match
        if user.get("role") in opportunity.get("roles", []):
            score += 3
            reasons.append("Your role matches this opportunity.")

        # State match
        if user.get("state") in opportunity.get("states", []):
            score += 2
            reasons.append("This opportunity is available in your state.")

        # Education match
        if user.get("education") in opportunity.get("education", []):
            score += 3
            reasons.append("Your education matches the requirement.")

        recommendations.append({
            "id": opportunity["id"],
            "title": opportunity["title"],
            "type": opportunity["type"],
            "score": score,
            "reasons": reasons
        })

    # Highest score first
    recommendations.sort(
        key=lambda opportunity: opportunity["score"],
        reverse=True
    )

    return recommendations