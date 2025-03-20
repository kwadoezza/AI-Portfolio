AI Chatbot Code (chatbot.py)

import openai
import nltk
import os

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"

def chatbot_response(user_input):
    """Generate a response from OpenAI's GPT model."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

if _name_ == "_main_":
    print("AI Chatbot: Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
