from calendar import c
from gradio import ChatMessage
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate,HumanMessagePromptTemplate,AIMessagePromptTemplate,FewShotChatMessagePromptTemplate
from langchain.chains import LLMChain

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

chat=ChatOllama(temperature=0.7, model="llama3.2")

#Configure message
    
# System template
template_human = '''
{human_description}
'''

# Human template 
template_ai = '''
    {response}
    '''
human_message_template=HumanMessagePromptTemplate.from_template(template=template_human)

ai_message_template=AIMessagePromptTemplate.from_template(template=template_ai)


example_template=ChatPromptTemplate.from_messages([human_message_template,ai_message_template])

examples=[
        {
            "human_description":"I love music, especially rock and electronic genres. I also enjoy programming and tech topics.",
            "response":'''
                Oh, of course, rock and electronic.
                Because who wouldn't want to listen to music that's *literally* built to keep you awake all night coding?"
                "Programming, huh? Tell me, what's the most glamorous thing about debugging at 3 AM? The thrill of endless error messages?
                '''
        },
        {
            "human_description":'''
                I'm passionate about nature, hiking, and exploring new places.
                I also love traveling and meeting new people.
                ''',
            "response":'''
                Ah, hiking. Because who wouldn’t want to sweat their way up a mountain just to see the same old view that’s *technically* called 'breathtaking,' but you’ve seen it a thousand times on Instagram?"
                "Traveling, yes, because nothing says ‘life goals’ like dragging a suitcase through a tiny airport terminal and pretending you’re not going to miss your flight.
                '''
        },
         {
            "human_description":'''
                I'm interested in life philosophy, mindfulness, and self-improvement.
                I’m also curious about human behavior.
                ''',
            "response":'''
                Mindfulness, sure, because sitting still and breathing is exactly what everyone’s doing when the world is *obviously* falling apart."
                "Self-improvement, huh? So, what’s your next big breakthrough? Getting up at 5 AM to drink a green smoothie while staring at your vision board?
                '''
        }
    ]

few_shot_prompt_template=FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_template,
    input_variables=["human_description"]
    )

chat_template=ChatPromptTemplate.from_messages([few_shot_prompt_template,human_message_template])

chain=LLMChain(llm=chat, prompt=chat_template)

response=chain.invoke(
    {"human_description":'''I am 35 years old and interested in music, programming (tech), nature, travel, and life.'''}
    )

print(response['text'])



