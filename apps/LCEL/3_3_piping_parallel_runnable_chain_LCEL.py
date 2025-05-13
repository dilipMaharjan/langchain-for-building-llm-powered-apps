from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
import time

#load api key
load_dotenv()


#chat template for books

chat_template_books=ChatPromptTemplate.from_template(
    '''
    What are the 3 most important books to master {programming_language}?
    Answer only by listing the books.
    '''
)

#chat template for projects

chat_template_projects=ChatPromptTemplate.from_template(
    '''
    What are the 3 most important projects to master {programming_language}?
    Answer only by listing the projects.
    '''
)

chat_template_duration=ChatPromptTemplate.from_template(
    '''
    I am an intermediate software engineer. 
    Consider following resources:
    {books} and {projects}
    Roughly how much time will it take me to complete these books and projects?
    '''
)

#creating instance of ChatOllama
chatInstance= ChatOllama(temperature=0, model="llama3.2")


#Parser
string_parser=StrOutputParser()

#create chains

chain_books = chat_template_books | chatInstance | string_parser 
chain_projects = chat_template_projects | chatInstance | string_parser


#RuunnableParallel
parallel_chain = RunnableParallel({"books": chain_books, "projects": chain_projects})

#chain runnable and runnable parallel
#method 1 
# chain_duration=parallel_chain | chat_template_duration | chatInstance | string_parser 

#method 2, make sure to comment RuunnableParallel and chain_duration when testing this method
# chain_duration=RunnableParallel({"books": chain_books, "projects": chain_projects}) | chat_template_duration | chatInstance | string_parser 

#method 3, make sure to comment chain_duration when testing this method, it automatically converts to parallel
chain_duration=({"books": chain_books, "projects": chain_projects}) | chat_template_duration | chatInstance | string_parser 


#visualize chain 
chain_duration.get_graph().print_ascii()

#invocation
response = chain_duration.invoke({"programming_language":"python"})

print(response)




