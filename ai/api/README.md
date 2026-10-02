# AdhikarSetu Intelligence API

## Endpoint

POST `/recommend`

Local development:

`http://127.0.0.1:8000/recommend`

## Request

Send the user's profile as JSON.

```json
{
  "role": "student",
  "age": 20,
  "state": "Haryana",
  "education": "B.Tech CSE",
  "income": 150000
}