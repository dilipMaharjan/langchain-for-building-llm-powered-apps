from langchain_ollama import ChatOllama
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate 

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

# Configure messages

# System template
template_system = '''
{system_description}
'''


# Human template 
template_human = '''
    {human_description}
    '''

# Create prompt templates
prompt_template_system = SystemMessagePromptTemplate.from_template(template_system)
prompt_template_human = HumanMessagePromptTemplate.from_template(template_human)


# Create chat prompt template
chat_prompt_template = ChatPromptTemplate.from_messages([prompt_template_system, prompt_template_human])

# print(chat_prompt_template)

system_description = '''You are an excellent icebreaker facilitator. 
The user has already shared their interests, and your task is to suggest engaging and personalized icebreaker questions based on those interests. 
Do not ask the user for any additional information. The user is interested in music, programming (tech), nature, travel, and life in general. 
Tailor your questions around these topics and make sure they are friendly, natural, and relevant. Avoid generic or open-ended questions asking for more details.
'''


# Human message with the user's interests
human_description = '''I am 35 years old and interested in music, programming (tech), nature, travel, and life.
    I’m looking for thoughtful icebreaker questions or topics for conversation based on these interests.
    Can you suggest some?
    '''

chat_value=chat_prompt_template.invoke({"system_description":system_description,"human_description":human_description})

response=deterministic_ice_breaker.invoke(chat_value)

print(response.content)
