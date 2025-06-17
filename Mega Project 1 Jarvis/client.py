from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)

import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is coding?")
print(response.text)
