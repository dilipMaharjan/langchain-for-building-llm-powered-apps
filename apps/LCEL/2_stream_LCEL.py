#prompt,model,output parser

from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.prompts.chat import ChatPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

#load api key
load_dotenv()


#chat prompt template

chatPromptTemplate=ChatPromptTemplate.from_messages([
    ("human", "I am crrently researching on {topic}. Please provide me answer in {lines}"),
])

#creating instance of ChatOllama
chatInstance= ChatOllama(temperature=0, model="llama3.2")

chain = chatPromptTemplate | chatInstance

#chain batch
response=chain.stream({"topic":"Langchain Expression Language (LCEL)", "lines":20})

print(response) #generator

for res in response:
    print(res.content,end=" ")
