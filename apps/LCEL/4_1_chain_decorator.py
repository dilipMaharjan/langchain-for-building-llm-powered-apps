from langchain_core.runnables import RunnableLambda, chain

def find_sum(x):
    return sum(x)

def find_square(x):
    return x**2

chain1=RunnableLambda(find_sum) | RunnableLambda(find_square)
print(chain1.invoke([1,2,3,4,5]))


#decorator is simple a function 
@chain
def runnable_sum(x):
    return sum(x)

@chain
def runnable_square(x):
    return x**2

chain2=runnable_sum | runnable_square
print(chain2.invoke([1,2,3,4,5]))

# Note : Do not use chain as variable name as it confuses the interpreter

