import requests
from config import OPENAI_API_KEY

def get_activities(city, weather_description):
    prompt = f"""
    Based on the weather in {city} described as "{weather_description}", suggest 5 activities.

    Each activity should be returned in JSON format, like:
    [
        {{
            "description": "Go to a cozy café",
            "image_prompt": "Image of a quiet café with steam rising from mugs on a rainy afternoon"
        }},
        ...
    ]

    Return only the JSON array — no explanation, no headers.
    """

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "HTTP-Referer": "WeatherApp",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-tiny",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }
    try:
        # OpenRouter API endpoint
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
    