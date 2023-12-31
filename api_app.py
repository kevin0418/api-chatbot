import os
from openai import OpenAI

client = OpenAI(
  api_key = os.environ["OPENAI-API-KEY"],
)


from streamlit_chat import message

response  = client.completions.create (
  model="text-davinci-003",
  prompt="겨울에 대한 시좀 써줘"  ,
  max_tokens=150  
)      
 
print(response.choices[0].text)

