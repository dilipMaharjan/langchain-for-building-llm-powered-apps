from itertools import chain
from tracemalloc import start
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


#creating instance of ChatOllama
chatInstance= ChatOllama(temperature=0, model="llama3.2")


#Parser
string_parser=StrOutputParser()

#create chains

chain_books = chat_template_books | chatInstance | string_parser 
chain_projects = chat_template_projects | chatInstance | string_parser


#RuunnableParallel
parallel_chain = RunnableParallel({"books": chain_books, "projects": chain_projects})

#visualize chain 
parallel_chain.get_graph().print_ascii()

#invoke
start_time=time.time()
chain_books.invoke({"programming_language":"python"})


chain_projects.invoke({"programming_language":"python"})
end_time=time.time()

print("Time taken for non pararallel invocation",end_time-start_time)

start_time=time.time()
response=parallel_chain.invoke({"programming_language":"python"})
end_time=time.time()

print("Time taken for parallel invocation",end_time-start_time)

print(response)


