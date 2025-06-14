from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

wikipedia_api=WikipediaAPIWrapper()
response=wikipedia_api.run("Python (programming language)")
# print(response)

wikipedia_tool=WikipediaQueryRun(api_wrapper=wikipedia_api)
# print(wikipedia_tool.name)
# print(wikipedia_tool.description)
# print(wikipedia_tool.args)

#Tools are runnable, so we can invoke them directly
response=wikipedia_tool.invoke({"query":"Python (programming language)"})
# print(response)
#we can also invoke them with a string
response=wikipedia_tool.invoke("Python (programming language)")
# print(response)

#Template for the prompt
TEMPLATE = """
Turn the following user input into a Wikipedia search query. Don't answer the question, just return the query:
{input}
"""
prompt_template = PromptTemplate.from_template(template=TEMPLATE)
# print(prompt_template.template)

#Chat model
chat = ChatOllama(temperature=0, model="llama3.2")

#chain when invoked turns the query into a Wikipedia search query
# chain=prompt_template | chat | StrOutputParser()

chain=prompt_template | chat | StrOutputParser()| wikipedia_tool

#run the chain
response = chain.invoke({"input":"Who is the creator of Python?"})
#Query modified by the chain to be used in the Wikipedia search
print(response)
