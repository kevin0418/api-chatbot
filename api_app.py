import os
from openai import OpenAI

client = OpenAI(
  api_key = os.environ["OPENAI-API-KEY"],
)


#from streamlit_chat import message

response  = client.chat.completions.create (
  model="gpt-3.5-turbo-1106",
  messages=[
      {"role":"system", "content":"You sre a helpful assistance"},
      {"role":"user", "content":"겨울에 대한 시좀 써줘. json"}
  ],
  response_format={"type": "json_object"}
) 
 
print(response.choices[0].message.content)

