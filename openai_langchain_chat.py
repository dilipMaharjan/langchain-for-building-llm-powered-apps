from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
Dilip Maharjan is the founder of Everything Digital, a company focused on providing innovative digital solutions, including web development, digital marketing, and IT consulting. With a vision to bridge the gap between businesses and technology, he has led the company to help numerous clients establish a strong digital presence. Under his leadership, Everything Digital has grown into a trusted name in the industry, offering cutting-edge services tailored to modern business needs.
"""

if __name__ == "__main__":
    template = """
    Given the information {information} about a person, create: 
    1. A short summary
    2. Two interesting facts about them
    """

    prompt = PromptTemplate(input_variables=["information"], template=template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = prompt | llm

    result = chain.invoke(input={"information": information})
    print(result)
