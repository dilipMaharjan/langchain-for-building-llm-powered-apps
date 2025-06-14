from urllib import response
from langchain_core.tools import tool
from platform import python_version 
@tool
def get_python_version()->str:
    '''Get the current Python version.
    Returns:
        str: The version of Python currently in use.
    '''
    return python_version()

# print(get_python_version)

response = get_python_version.invoke({})
print(response)
