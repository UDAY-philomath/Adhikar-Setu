def check_eligibility(user, opportunity):
    reasons = []
    missing_information = []

    # Check role
    if not user.get("role"):
        missing_information.append("role")
    elif "roles" in opportunity:
        if user["role"] not in opportunity["roles"]:
            reasons.append("Role does not match the opportunity.")

    # Check age
    if user.get("age") is None:
        missing_information.append("age")
    else:
        if "min_age" in opportunity and user["age"] < opportunity["min_age"]:
            reasons.append("Age is below the minimum requirement.")

        if "max_age" in opportunity and user["age"] > opportunity["max_age"]:
            reasons.append("Age is above the maximum requirement.")

    # Check state
    if not user.get("state"):
        missing_information.append("state")
    elif "states" in opportunity:
        if user["state"] not in opportunity["states"]:
            reasons.append("State does not match the opportunity.")

    # Check education
    if not user.get("education"):
        missing_information.append("education")
    elif "education" in opportunity:
        if user["education"] not in opportunity["education"]:
            reasons.append("Education does not match the opportunity.")

    # Check income
    if user.get("income") is None:
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