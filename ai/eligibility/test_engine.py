from engine import check_eligibility


user = {
    "age": 20,
    "state": "Haryana",
    "education": "B.Tech",
    "income": 500000
}


opportunity = {
    "min_age": 18,
    "max_age": 25,
    "states": ["Haryana"],
    "education": ["B.Tech"],
    "income_limit": 300000
}


result = check_eligibility(user, opportunity)

print(result)