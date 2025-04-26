#prompt,model,output parser

from click import clear
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.prompts.chat import ChatPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from regex import template

#load api key
load_dotenv()


#instruction list 

list_instructions=CommaSeparatedListOutputParser().get_format_instructions()

#chat prompt template

chatPromptTemplate=ChatPromptTemplate.from_messages([
    ("human", "I am crrently researching on {topic}. Please provide me answer in {lines} \n " + list_instructions),
])

#creating instance of ChatOllama
chatInstance= ChatOllama(temperature=0, model="llama3.2")


#output parser
output_parser=CommaSeparatedListOutputParser()


chain = chatPromptTemplate | chatInstance | output_parser

#chain batch
response=chain.batch([{"topic":"Lanchain Expression Language", "lines":2},{"topic":"Lanchain Memory", "lines":3}])

print(response)

