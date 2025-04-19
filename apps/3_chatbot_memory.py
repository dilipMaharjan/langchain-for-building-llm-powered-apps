from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.globals import set_verbose
from langchain.memory import ConversationSummaryMemory
from langchain.chains import LLMChain


#load api key
load_dotenv()

#display output in verbose mode
set_verbose(True)

#creating instance of ChatOllama
chatInstance= ChatOllama(temperature=0, model="llama3.2")

#Create String template

TEMPLATE='''
You are a helpful assistant who reluctantly answers questions with sarcastic tone. If you don't know the answer, just say that you don't know, don't try to make up an answer.
{message_history}
Question: {question}
Answer:
'''
#promt template
prompt_template=PromptTemplate.from_template(template=TEMPLATE)

#setup memory
chat_memory=ConversationSummaryMemory(llm=chatInstance,memory_key="message_history",return_messages=False)

chat_memory.load_memory_variables({})

#create chain
chain=LLMChain(llm=chatInstance,prompt=prompt_template,memory=chat_memory)

#invoke
chain.invoke({"question":"Provide me an intresting fact?"})
chain.invoke({"question":"What makes you think that?"})

#Explore other memory types like ConversationSummaryBufferMemory,ConversationTokenBufferMemory
