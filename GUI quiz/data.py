import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")
response.raise_for_status()
full_data = response.json()["results"]

question_data = []

for i in range(len(full_data)):
    question_data.append({"question":full_data[i]['question'], "answer":full_data[i]['correct_answer']})

