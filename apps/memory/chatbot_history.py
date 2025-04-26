from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.prompts.chat import HumanMessagePromptTemplate,ChatPromptTemplate
from langchain.chains import LLMChain

#load api key
load_dotenv()

#creating instance of ChatOllama
chatInstance= ChatOllama(temperature=0, model="llama3.2")

#Chat history 
chatMessageHistory=ChatMessageHistory()


#adding message to history
chatMessageHistory.add_user_message("Would you rather be a cat or a dog?")
chatMessageHistory.add_ai_message("I would rather be a dog.")

#chat history
print(chatMessageHistory.messages)


#why use chat history instead of normal list

print(chatMessageHistory.model_dump_json())
print(chatMessageHistory.model_json_schema())

# print(chatMessageHistory.clear())


#creating human message template

humanMessageTemplate=HumanMessagePromptTemplate.from_template("{question}")

chatTemplate=ChatPromptTemplate.from_messages(chatMessageHistory.messages + [humanMessageTemplate])

#print chat template
print(chatTemplate.pretty_print())


#chain 
chain =LLMChain(llm=chatInstance, prompt=chatTemplate)

#invoking
response=chain.invoke({"question":"Would rather be a sky or the sea?"})
#this is keeping track of history but it doesn't remember anything, hence the need for memory




#print response
print(response["text"])
