from ai.eligibility.engine import check_eligibility


def recommend_opportunities(user, opportunities):
    recommendations = []
    missing_information = set()

    for opportunity in opportunities:
        eligibility = check_eligibility(user, opportunity)

        if eligibility["status"] == "MORE_INFORMATION_REQUIRED":
            missing_information.update(
                eligibility["missing_information"]
            )
            continue

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
            reasons.append(
                "This opportunity is available in your state."
            )

        # Education match
        if user.get("education") in opportunity.get("education", []):
            score += 3
            reasons.append(
                "Your education matches the requirement."
            )

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

    return {
        "recommendations": recommendations,
        "missing_information": sorted(missing_information)
    }