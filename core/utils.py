import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_tone_intent_and_suggestions(query):
    prompt = f"""
    Analyze the following input and respond in this format:
    Tone: <tone>
    Intent: <intent>
    Suggested actions:
    1. <step 1>
    2. <step 2>
    3. <step 3>

    Input: \"{query}\"
    """
    
    try:
        # Use the free model, typically 'gemini-base' or any other free-tier model
        model = genai.GenerativeModel("gemini-1.5-pro")  # Replace with the free model
        chat = model.start_chat(history=[])

        response = chat.send_message(prompt)
        content = response.text.strip()

        # Ensure the response format is correct
        if "Tone:" not in content or "Intent:" not in content or "Suggested actions:" not in content:
            raise ValueError("Unexpected response format")

        tone = content.split("Tone:")[1].split("Intent:")[0].strip()
        intent = content.split("Intent:")[1].split("Suggested actions:")[0].strip()
        suggestions = content.split("Suggested actions:")[1].strip().split("\n")

        # Format actions, ensuring they're in the correct format
        formatted_actions = [
            {"action_code": f"ACTION_{i+1}", "display_text": action.strip("0123456789. ") }
            for i, action in enumerate(suggestions) if action.strip()
        ]
        
        return tone, intent, formatted_actions[:3]

    except Exception as e:
        print(f"Error with Gemini: {e}")
        return "Unknown", "Unknown", []






# Open AI Api key


# import os
# import openai
# from dotenv import load_dotenv
# load_dotenv()

# MY_KEY = os.getenv("OPENAI_API_KEY")
# openai.api_key = MY_KEY

# def get_tone_intent_and_suggestions(query):
#     prompt = f"""
#     Analyze the following input and respond in this format:
#     Tone: <tone>
#     Intent: <intent>
#     Suggested actions:
#     1. <step 1>
#     2. <step 2>
#     3. <step 3>

#     Input: \"{query}\"
#     """

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         content = response.choices[0].message['content']

#         tone = content.split("Tone:")[1].split("Intent:")[0].strip()
#         intent = content.split("Intent:")[1].split("Suggested actions:")[0].strip()
#         suggestions = content.split("Suggested actions:")[1].strip().split("\n")

#         formatted_actions = [
#             {"action_code": f"ACTION_{i+1}", "display_text": action.strip("0123456789. ")}
#             for i, action in enumerate(suggestions) if action.strip()
#         ]
#         return tone, intent, formatted_actions[:3]
#     except Exception as e:
#         print("Error with LLM:", e)
#         return "Unknown", "Unknown", []