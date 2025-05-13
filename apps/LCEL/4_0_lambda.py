from langchain_core.runnables import RunnableLambda

find_sum=lambda x: sum(x) #nameless/anonymous function
print(find_sum([1,2,3,4,5]))

find_square=lambda x: x**2
print(find_square(15))

#cannot pipe them into chain as they are not runnables

#seemless way to create runnables from lambdas

runnable_sum1=RunnableLambda(find_sum)
runnable_square1=RunnableLambda(find_square)

#Since lambda functions are anonymous, storing them in variables defeats the purpose of creating lambda

runnable_sum2=RunnableLambda(lambda x: sum(x))
runnable_square2=RunnableLambda(lambda x: x**2)

print(runnable_sum1.invoke([1,2,3,4,5])) #can be piped into chain        
print(runnable_square1.invoke(15))       #can be piped into chain

print(runnable_sum2.invoke([1,2,3,4,5])) #can be piped into chain        
print(runnable_square2.invoke(15))       #can be piped into chain


chain = runnable_sum2 | runnable_square2

print("After piping into chain :",chain.invoke([1,2,3,4,5]))

chain.get_graph().print_ascii()

#Runnable lambda can be convert an ordinary function to a Runnable that we can invoke and enter as a chain component.
