import openai
openai.api_key= "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"

def generate_response(prompt):
    response = openai.Completion.create(
      engine="davinci", 
      prompt=prompt,
      max_tokens=100, 
      n=1,
      stop=None,
      temperature=1,
    )

    return response.choices[0].text

user_input = input("What issues are you experiencing?: ")
response = generate_response(user_input)
print(response)