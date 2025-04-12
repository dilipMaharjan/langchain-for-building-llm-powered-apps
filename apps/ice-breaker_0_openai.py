from urllib import response
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
'''
Prerequisites:
virtual environment created
Api key created
Configure key value in .env file

pip install langchain
pip install openai

load api key

'''
#loading api key
load_dotenv()
print("Key next line")
print(os.environ["OPENAI_API_KEY"][:5])

'''
creating instance of ChatOpenAI
temperature defines randomness of response
    0.0 - 2.0   Range
    0.0	        Deterministic (least random)
    ~0.3-0.7	Balanced (creative but relevant)
    1.0	        Very creative, more diverse
    > 1.0	    Often chaotic, less coherent
model_name defines model

'''
deterministic_ice_breaker= ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

#invoking
response=deterministic_ice_breaker.invoke("Facilitate a ice breaker conversation between 2 people")

#printing
print(response.content)
