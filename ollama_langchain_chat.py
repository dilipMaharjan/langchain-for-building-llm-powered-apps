from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama



INFORMATION = """
Dilip Maharjan is the founder of Everything Digital, a company focused on providing innovative digital solutions, including web development, digital marketing, and IT consulting. With a vision to bridge the gap between businesses and technology, he has led the company to help numerous clients establish a strong digital presence. Under his leadership, Everything Digital has grown into a trusted name in the industry, offering cutting-edge services tailored to modern business needs.
"""

if __name__ == "__main__":
    template = """
    Given the information {information} about a person, create: 
    who is dilip maharjan in one word.
    """

    prompt = PromptTemplate(input_variables=["information"], template=template)

    llm = ChatOllama(temperature=0, model="llama3.2")

    chain = prompt | llm | StrOutputParser()
    
    result = chain.invoke(input={"information": INFORMATION})
    print(result)
