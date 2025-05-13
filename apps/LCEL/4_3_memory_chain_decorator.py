from langchain_core.runnables import chain
from operator import itemgetter
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.globals import set_verbose
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationSummaryMemory
from langchain_core.runnables import RunnablePassthrough,RunnableLambda


#load api key
load_dotenv()

#display output in verbose mode
set_verbose(True)

#creating instance of ChatOllama
chatInstance= ChatOllama(temperature=0, model="llama3.2")

#Create String template

TEMPLATE='''
The following is a friendly conversation between a human and an AI.
The AI is talkative and provides lots of specific details from its context.
If the AI does not know the answer to a question, it truthfully says it does not know.

Current Conversation:
{message_history}

Human: 
{question}

AI:
'''
#promt template
prompt_template=PromptTemplate.from_template(template=TEMPLATE)


#setup memory
chat_memory=ConversationSummaryMemory(llm=chatInstance,memory_key="message_history")

def load_memory_vars(input):
    return chat_memory.load_memory_variables(input)
@chain
def memory_chain(question):
    #create chain 
    chain1=(
        RunnablePassthrough.assign(message_history=RunnableLambda(load_memory_vars) | itemgetter("message_history"))
        | prompt_template
        | chatInstance
        | StrOutputParser()
    )
    chain1.get_graph().print_ascii()
    response = chain1.invoke({'question':question})
    chat_memory.save_context(inputs={"input":question},outputs={"output":response})
    return response

memory_chain.invoke("Provide me an intresting fact?")
memory_chain.invoke("Can you elaborate a bit more on this fact?")
