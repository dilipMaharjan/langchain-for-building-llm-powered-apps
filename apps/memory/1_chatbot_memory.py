from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.prompts.chat import HumanMessagePromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.globals import set_verbose
from langchain.schema import SystemMessage
from langchain.memory import ConversationBufferWindowMemory

#load api key
load_dotenv()

#display output in verbose mode
set_verbose(True)

#creating instance of ChatOllama
chatInstance= ChatOllama(temperature=0, model="llama3.2")

#Messages

systemMessage=SystemMessage(content="You are a helpful assistant who reluctantly answers questions with sarcastic tone. If you don't know the answer, just say that you don't know, don't try to make up an answer.")
messageHumanTemplate=HumanMessagePromptTemplate.from_template('''{question}''')

#Keep track of message history

messageHistory=MessagesPlaceholder(variable_name="message_history")

#chat template

chatPromptTemplate=ChatPromptTemplate.from_messages([systemMessage,messageHistory,messageHumanTemplate])


chatHistory=ChatMessageHistory()

#adding message to history
chatHistory.add_user_message("Hi")
chatHistory.add_ai_message("You really know how to make an entrace, don't you?")

#creating memory and connecting chat history
chatMemory=ConversationBufferWindowMemory(memory_key="message_history",chat_memory=chatHistory,return_messages=True,k=2) #set it as False to get formatted output


print(chatMemory.load_memory_variables({})['message_history'])


#create chain 

chat=LLMChain(llm=chatInstance,prompt=chatPromptTemplate,memory=chatMemory)

#invoke chain
response1=chat.invoke({"question":"Provide me an intresting fact?"})
response2=chat.invoke({"question":"What were the names?"})
response3=chat.invoke({"question":"who should have won the war?"})



print(response1['text'])
print(response2['text'])
print(response3['text'])
