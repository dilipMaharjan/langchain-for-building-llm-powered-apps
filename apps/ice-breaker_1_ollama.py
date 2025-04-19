from urllib import response
from langchain_ollama import ChatOllama
'''
Prerequisites:
virtual environment created

pip install langchain
pip install -U langchain-ollama

'''


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
deterministic_ice_breaker= ChatOllama(temperature=0, model="llama3.2")

#invoking
response=deterministic_ice_breaker.invoke('''Facilitate a ice breaker. You are able to suggest questions to talk on based on the interests.''')

#print response
print(response)

#printing
print(response.content)
