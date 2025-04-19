from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.globals import set_verbose
from langchain.memory import ConversationSummaryMemory,ConversationBufferMemory,CombinedMemory
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

Past conversation:
{message_buffer_history}

Conversation summary:
{message_summary_history}

Human: {question}

Answer:
'''
#promt template
prompt_template=PromptTemplate.from_template(template=TEMPLATE)

#setup memory
message_buffer_history_memory=ConversationBufferMemory(memory_key="message_buffer_history",input_key="question",return_messages=False)
message_summary_history_memory=ConversationSummaryMemory(llm=chatInstance,memory_key="message_summary_history",input_key="question",return_messages=False)
combined_memory=CombinedMemory(memories=[message_buffer_history_memory,message_summary_history_memory])

#create chain
chain=LLMChain(llm=chatInstance,prompt=prompt_template,memory=combined_memory)


#invoke
chain.invoke({"question":"Tell me few facts about Nepal."})
chain.invoke({"question":"Choose 2 from these"})
chain.invoke({"question":"k, what do you reccommend ?"})

