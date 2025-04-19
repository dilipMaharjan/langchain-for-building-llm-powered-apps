from ollama_langchain_chat import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
import gradio as gr

def chatbot(input):
    # Initialize the Ollama model
    chat = ChatOllama(temperature=0, model="llama3.2")

    # Define the system and human messages
    system_message = SystemMessage(content="You are an expert in langchian library.You only answer quesiton in regard to langchian and langchain eco system.If you are asked about anything else, just reply saying you are only capable to answer about langchain and langchain eco system.")
    human_message = HumanMessage(content="{}.".format(input))

    # Invoke the model with the system and human messages
    response = chat.invoke([system_message, human_message])

    # Print the response
    return response.content # Extracting the 'text' from the response dictionary


if __name__ == "__main__":
    gr.Interface(fn=chatbot,
                 title="Langchain Expert Chatbot",
                 inputs=gr.Textbox(lines=2, label="I am expert in langchain library,and I can answer questions in regard to langchain and langchain eco system."),
                 outputs=gr.Text(label="My response"),
                 live=True).launch()



