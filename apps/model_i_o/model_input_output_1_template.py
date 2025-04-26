from urllib import response
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import PromptTemplate



'''
Prerequisites:
virtual environment created

pip install langchain
pip install -U langchain-ollama

'''


'''
creating instance of ChatOpenAI,model and temperature selection
temperature defines randomness of response
    0.0 - 2.0   Range
    0.0	        Deterministic (least random)
    ~0.3-0.7	Balanced (creative but relevant)
    1.0	        Very creative, more diverse
    > 1.0	    Often chaotic, less coherent
model_name defines model

'''

deterministic_ice_breaker= ChatOllama(temperature=0.7, model="llama3.2")

#Templating for reusability
TEMPLATE='''
System: {system_message}

Human: {human_message}

'''

# Configure messages
system_message = SystemMessage(content='''You are an excellent icebreaker facilitator. 
The user has already shared their interests, and your task is to suggest engaging and personalized icebreaker questions based on those interests. 
Do not ask the user for any additional information. The user is interested in music, programming (tech), nature, travel, and life in general. 
Tailor your questions around these topics and make sure they are friendly, natural, and relevant. Avoid generic or open-ended questions asking for more details.
''')


# Human message with the user's interests
human_message = HumanMessage(
    content='''I am 35 years old and interested in music, programming (tech), nature, travel, and life.
    I’m looking for thoughtful icebreaker questions or topics for conversation based on these interests.
    Can you suggest some?'''
)


prompt_template=PromptTemplate.from_template(template=TEMPLATE)

prompt_value=prompt_template.invoke(input={"system_message":system_message,"human_message":human_message})
# print("Prompt response")
# print(prompt_value.text)

prompt_response=deterministic_ice_breaker.invoke(prompt_value)
print(prompt_response.content)


