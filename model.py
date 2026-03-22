from transformers import pipeline

chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def get_response(user_input):
    response = chatbot(user_input, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']
