import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for cake "}])
print(completion.choices[0].message.content)