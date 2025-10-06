from openai import OpenAI

# pip install openai

# Initialize client with your API key
client = OpenAI(
    api_key="**"  # Replace with your actual key
)

# Create a chat completion
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are person named Jidnyasa who speaks Marathi, Hindi as well as English. You are from India and is a coder. You analyze chat history and respond like Jidnyasa"},
        {"role": "user", "content": "what is coding"}
    ]
)

# Print response
print(completion.choices[0].message.content)


