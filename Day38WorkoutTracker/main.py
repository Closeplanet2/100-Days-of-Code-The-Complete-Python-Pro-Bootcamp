import requests
from datetime import datetime

GENDER = "MALE"
WEIGHT_KG = 100
HEIGHT_CM = 182.88
AGE = 24

APP_ID = "0c507416"
API_KEY = "894f9f6d2274987f1ef5032dc232720d"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = YOUR SHEETY ENDPOINT
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            YOUR USERNAME,
            YOUR PASSWORD,
        )
    )

    bearer_headers = {
        "Authorization": "Bearer YOUR_TOKEN"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )