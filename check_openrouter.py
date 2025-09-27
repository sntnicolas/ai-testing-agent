import os

import requests
import json
from dotenv import load_dotenv
load_dotenv()
def call_openrouter_api(user_message, model_name="google/gemini-2.5-flash", api_key=os.getenv("OPENROUTER_API_KEY")):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )
    return response.json()

# Теперь ты можешь вызывать так:
result = call_openrouter_api("Привет, как дела?")
print(result)

# # Или, если захочешь использовать другую модель:
# result_other_model = call_openrouter_api("Напиши короткий стих", model_name="anthropic/claude-3-haiku")
# print(result_other_model)