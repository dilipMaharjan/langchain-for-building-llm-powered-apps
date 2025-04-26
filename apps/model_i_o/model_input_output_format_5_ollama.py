import json
from sqlite3 import Date
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser,CommaSeparatedListOutputParser,JsonOutputParser
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

human_message = HumanMessage(content='''Facilitate a ice breaker. You are able to suggest questions to talk on based on the interests.''')

#invoking
response=deterministic_ice_breaker.invoke([human_message])

#Format into string
str_output_parsers=StrOutputParser()
print(str_output_parsers.invoke(response))

#format into comma separated list
list_str_output_parsers=CommaSeparatedListOutputParser()

human_message = HumanMessage(content=f'''Facilitate a ice breaker. You are able to suggest questions to talk on based on the interests.
                             {list_str_output_parsers.get_format_instructions()}
                             ''')
list_response=deterministic_ice_breaker.invoke([human_message])
print(str_output_parsers.invoke(list_response))

#format into datetime
json_output_parser=JsonOutputParser()
human_message = HumanMessage(content=f'''You are a helpful assistant that creates icebreaker questions and returns the result in JSON format only.
                             Return exactly one valid JSON object, without extra text or code.
                             Do NOT explain or include code examples.
                             {json_output_parser.get_format_instructions()}
                             ''')
json_response=deterministic_ice_breaker.invoke([human_message])


print(json_output_parser.invoke(json_response))
