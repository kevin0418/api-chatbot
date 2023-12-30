import os
import openai
 
openai.api_key = os.getenv("OPENAI-API-KEY")

print ("OPENAI-API-KEY :", "OPENAI-API-KEY")
print ("openai.api_key :", openai.api_key)

#from openai import OpenAI

from streamlit_chat import message

response  = openai.Completion.create (
  model="text-davinci-003",
  prompt="겨울에 대한 시좀 써줘"  ,
  max_tokens=150  
)      
 
print(response.choices[0].text)