import os
import json
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

print(
    "KEY PREFIX:",
    os.getenv("GEMINI_API_KEY")[:8]
)

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def analyze_career(user_input):

    prompt = f"""
    You are Career Compass AI.

    Your purpose is to help people who feel stuck after a setback by showing alternative routes toward their goals.

    Analyze the user's situation and return ONLY valid JSON.

    Rules:

    1. goal must be maximum 5 words.
    2. original_route must be maximum 10 words.
    3. route_status must be maximum 6 words.
    4. route titles must be maximum 4 words.
    5. route descriptions must be maximum 25 words.
    6. perspective must be maximum 120 words.
    7. Be realistic, encouraging and practical.
    8. Do not use markdown.
    9. Return JSON only.

    JSON FORMAT:

    {{
        "goal": "",
        "original_route": "",
        "route_status": "",

        "route1_title": "",
        "route1_desc": "",

        "route2_title": "",
        "route2_desc": "",

        "route3_title": "",
        "route3_desc": "",

        "route4_title": "",
        "route4_desc": "",

        "perspective": ""
    }}

    User Situation:

    {user_input}
    """

    response = model.generate_content(prompt)

    cleaned = response.text.replace("```json", "")
    cleaned = cleaned.replace("```", "")

    return json.loads(cleaned)
