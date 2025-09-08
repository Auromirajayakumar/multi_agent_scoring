import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Validate API key presence
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

def feedback_agent(transcript: str, score: float) -> str:
    prompt = f"""
    You are an expert evaluator. Given the following transcript and score, generate constructive feedback:

    Transcript: "{transcript}"
    Score: {score}

    Provide feedback that is clear, helpful, and tailored to the response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating feedback: {str(e)}"