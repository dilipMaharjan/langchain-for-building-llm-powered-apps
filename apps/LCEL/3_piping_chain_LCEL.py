from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

#load api key
load_dotenv()


#chat template for tools

chat_template_tools=ChatPromptTemplate.from_template(
    '''
    What are the five most important tools for a {job_title} needs?
    Answer only by listing the tools.
    '''
)

#chat template for strategy

chat_template_strategy=ChatPromptTemplate.from_template(
    '''
    Considering the tools provided, develop a strategy for effective learning and masteering them : {tools}
    '''
)


#creating instance of ChatOllama
chatInstance= ChatOllama(temperature=0, model="llama3.2")


#Parser
string_parser=StrOutputParser()

#create chains

chain_tools = chat_template_tools | chatInstance | string_parser | {'tools':RunnablePassthrough()}
chain_strategy = chat_template_strategy | chatInstance | string_parser


#invoke tool chain 
tools=chain_tools.invoke({"job_title":"Data Scientist"})

print(tools)



#invoke strategy chain 
strategy=chain_strategy.stream({"tools":tools})

for res in strategy:
    print(res,end="", flush=True)

