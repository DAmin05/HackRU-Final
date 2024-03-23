from openai import OpenAI
#import time

client = OpenAI(api_key="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")

def get_responses(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user" , "content":"What is AI"}]
    )
    #time.sleep(100)
    return response.choices[0].message.content.strip()

print("Chatbox: " , get_responses(""))