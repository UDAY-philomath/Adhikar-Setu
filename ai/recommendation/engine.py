from ai.eligibility.engine import check_eligibility


def recommend_opportunities(user, opportunities):
    recommendations = []

    for opportunity in opportunities:
        eligibility = check_eligibility(user, opportunity)

        if eligibility["status"] != "ELIGIBLE":
            continue

        score = 0
        reasons = []

        if user.get("role") in opportunity.get("roles", []):
            score += 3
            reasons.append("Your role matches this opportunity.")

        if user.get("state") in opportunity.get("states", []):
            score += 2
            reasons.append("This opportunity is available in your state.")

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

    recommendations.sort(
        key=lambda opportunity: opportunity["score"],
        reverse=True
    )

    return recommendations