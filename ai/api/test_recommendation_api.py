import requests


API_URL = "http://127.0.0.1:8000/recommend"


test_users = [
    {
        "name": "Underage Student",
        "profile": {
            "role": "student",
            "age": 16,
            "state": "Haryana",
            "education": "B.Tech CSE",
            "income": 150000
        }
    },
    {
        "name": "Student",
        "profile": {
            "role": "student",
            "age": 20,
            "state": "Haryana",
            "education": "B.Tech CSE",
            "income": 150000
        }
    },
    {
        "name": "Worker",
        "profile": {
            "role": "worker",
            "age": 25,
            "state": "Haryana",
            "education": "B.Tech",
            "income": 200000
        }
    },
    {
        "name": "Student - Delhi",
        "profile": {
            "role": "student",
            "age": 21,
            "state": "Delhi",
            "education": "B.Tech CSE",
            "income": 250000
        }
    },
    {
        "name": "Incomplete Student",
        "profile": {
            "role": "student",
            "age": 20,
            "state": "Haryana"
        }
    }
]


for user in test_users:

    response = requests.post(
        API_URL,
        json=user["profile"]
    )

    print(f"\n===== {user['name']} =====")
    print(f"Status: {response.status_code}")

    data = response.json()

    for recommendation in data["recommendations"]:
        print(
            f"- {recommendation['title']} "
            f"({recommendation['type']}) "
            f"[Score: {recommendation['score']}]"
        )

    if data["missing_information"]:
        print(
            f"Missing information: "
            f"{', '.join(data['missing_information'])}"
        )