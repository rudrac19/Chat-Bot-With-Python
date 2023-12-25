import openai

openai.api_key = "API KEY"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "  MESSAGE  "}])
print(completion.choices[0].message.content)
