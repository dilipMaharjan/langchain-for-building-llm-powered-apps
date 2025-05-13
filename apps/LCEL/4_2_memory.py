from operator import itemgetter
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.globals import set_verbose
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationSummaryMemory
from langchain_core.runnables import RunnablePassthrough,RunnableLambda
from ollama import chat


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


question="Can give me a summary of Jesus's life"


dictionary_output=RunnablePassthrough.assign(
    message_history=RunnableLambda(chat_memory.load_memory_variables) | itemgetter("message_history")
    ).invoke({'question':question})

prompt_value_output=prompt_template.invoke(dictionary_output)
print(prompt_value_output, end="\n\n")

chat_response=chatInstance.invoke(prompt_value_output)
print(chat_response,end="\n\n")

string_response=StrOutputParser().invoke(chat_response)
print("String response is: \n",string_response)

#save response to context
chat_memory.save_context({"input":question},{"output":string_response})
chat_memory.load_memory_variables({})

chain1=(
    RunnablePassthrough.assign(message_history=RunnableLambda(chat_memory.load_memory_variables) | itemgetter("message_history"))
    | prompt_template
    | chatInstance
    | StrOutputParser()
)
chain1.invoke({'question':question})
