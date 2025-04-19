from ollama_langchain_chat import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
import gradio as gr

def chatbot(input):
    # Initialize the Ollama model
    chat = ChatOllama(temperature=0, model="llama3.2")

    # Define the system and human messages
    system_message = SystemMessage(content="You are OneLiner.You answer in one line only.You are ablet only tell a joke or pickup line. If someone ask you multi line questions or something orther than joke or pickup, you can say I am not trained to answer that,please try again.")
    human_message = HumanMessage(content="{}.".format(input))

    # Invoke the model with the system and human messages
    response = chat.invoke([system_message, human_message])

    # Print the response
    return response.content # Extracting the 'text' from the response dictionary


if __name__ == "__main__":
    gr.Interface(fn=chatbot,
                 title="OneLiner Chatbot",
                 inputs=gr.Textbox(lines=2, label="I can tell you a joke or a pickup line"),
                 outputs=gr.Text(label="My response"),
                 live=True).launch()



