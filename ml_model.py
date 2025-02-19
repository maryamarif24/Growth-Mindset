import openai


def get_ai_advice(spending_data):
    prompt = f"I have spent {spending_data}. Can you suggest how to improve my budgeting?"
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=100)
    return response["choices"][0]["text"]

# Example Usage
spending_summary = "200 on food, 100 on transport, 150 on shopping"
print(get_ai_advice(spending_summary))
