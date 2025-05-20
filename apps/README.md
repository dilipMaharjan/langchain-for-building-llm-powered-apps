# Langchain for Building LLM-Powered Applications

## What we will explore  
- [What/Why is LangChain](#whatwhy-is-langchain)  
- [LangChain Ecosystem](#langchain-ecosystem)  
- [Model Input](#model-input)  
- [Model Output](#model-output)  
- [Chatbot Memory](#chatbot-memory)  
- [Retrieval-Augmented Generation](#retrieval-augmented-generation)  
- [Agent Tooling](#agent-tooling)  
- [LangChain Expression Language (LCEL)](#langchain-expression-language-lcel)  

---

## What/Why is LangChain  

LangChain is an open-source framework designed to help developers build applications powered by **large language models (LLMs)** with greater flexibility and efficiency. It simplifies the process of creating complex, multi-step workflows by connecting LLMs with external data, memory, and tools.  

### 🔥 **Why Use LangChain?**  
- **Seamless LLM Integration:** LangChain supports various language models, including **OpenAI’s GPT**, **Anthropic’s Claude**, **Hugging Face models**, and more.  
- **Simplifies Workflow Chaining:** Instead of writing custom code to handle multiple operations, you can create **"chains"** that sequentially execute tasks such as retrieving data, summarizing content, and generating answers.  
- **Data-Augmented Generation:** It allows your LLM-powered app to interact with **real-world data**, making the responses more accurate and contextually relevant.  
- **Memory Management:** LangChain adds **memory capabilities** to applications, enabling multi-turn conversations that retain context, similar to how humans communicate.  
- **Rapid Prototyping:** With its modular architecture, LangChain makes it easy to **prototype and deploy** AI applications faster.  

### ✅ **Real-World Use Cases**
- **Conversational Agents:** Build chatbots with memory and contextual understanding.  
- **Automated Document Analysis:** Extract insights from large document repositories.  
- **Knowledge Retrieval:** Retrieve and process information from external APIs or databases.  
- **Autonomous Agents:** Create AI agents capable of decision-making and task automation.  

---

## LangChain Ecosystem  
The **LangChain ecosystem** consists of a set of modular components that developers can use to build and scale AI applications. It offers tools for managing the interaction between LLMs and external data sources, enhancing the flexibility and capabilities of AI-powered apps.  

### 🔥 **Key Components in the LangChain Ecosystem**  

### 🔹 1. **LLMs (Language Models)**  
At the core of LangChain are **LLMs** that generate text, answer questions, and process information. LangChain supports multiple providers, including:  
- **OpenAI GPT models** – For text generation and conversation.  
- **Anthropic Claude** – Known for its safety and interpretability features.  
- **Hugging Face models** – Offers a variety of open-source language models.  
- **Google’s Gemini and Vertex AI** – For integrating with Google Cloud services.  

---

### 🔹 2. **Chains**  
Chains are the building blocks of LangChain applications. They define the sequence of operations, combining multiple LLM calls and external processes into **multi-step workflows**.  

**Example:**  
- Retrieve data from a document → Summarize it → Generate a response → Display output.  

Chains make it easy to orchestrate complex operations without writing repetitive boilerplate code.  

---

### 🔹 3. **Memory**  
Memory adds **context retention** to applications. This allows for more natural and meaningful interactions, where the LLM remembers previous messages or actions.  

**Use Case:**  
- In a chatbot, memory ensures the assistant remembers the user’s previous queries and preferences, making the conversation more coherent.  

---

### 🔹 4. **Agents**  
Agents use **decision-making logic** to determine which actions to take based on the input they receive. They can interact with external APIs, search the web, or perform calculations.  

**Example:**  
- A travel assistant agent can automatically book flights, hotels, and fetch real-time weather updates.  

---

### 🔹 5. **Tools**  
Tools are external integrations that LangChain agents can use to **enhance functionality**. This can include:  
- **Search engines** for real-time information retrieval.  
- **Databases and APIs** for data access.  
- **Custom scripts** to perform specific operations.  

---

### 🔹 6. **LangChain Expression Language (LCEL)**  
LCEL is LangChain’s custom language for **defining chains and workflows** in a flexible and expressive manner. It allows you to describe complex chains in a simplified format, making your code more readable and maintainable.  

---

✅ With this modular ecosystem, LangChain enables you to build **robust, scalable, and intelligent LLM-powered applications** with ease.  

---

## Model Input/Output  
**Input** refers to the data provided to the system, such as user queries, prompts, structured data, or documents.

**Output** is the response returned by the language model, which can be in the form of text, structured data, or action steps.

LangChain applications typically follow a flow where input is passed through prompts and language models, processed, and returned as output.

In LangChain, Chains are sequences of components where the output of one step can serve as the input for the next. Each chain component defines:
- `input_keys`: required input data
- `output_keys`: expected output data

**Prompt Template** is a reusable format that defines how input variables are inserted into a prompt string. It ensures structured and consistent prompt creation for the language model.

**Chat Prompt Template** is used specifically for chat-based models. It organizes input into a sequence of messages (e.g., system, user, assistant roles) and supports dynamic construction of conversational prompts.

To build effective applications, it’s important to clearly define and manage the input and output at each step of the chain or workflow.
---

## Chatbot Memory  

## 🧠 What is Chat Memory?

Chat memory stores previous inputs and outputs from the conversation. This context allows the model to generate more relevant responses, simulate memory, and behave more naturally in extended dialogues.

---

## 📜 What is Chat History?

**Chat history** refers to the structured log of past interactions between a human and an AI. In LangChain, memory modules use this history to create context for the current prompt.

Chat history can be stored as:
- A **list of messages** (buffer memory)
- A **moving window** (limited number of messages)
- A **token-limited buffer** (limited by token count)
- A **summary string** (summary of conversation)

These formats affect how much of the conversation is remembered and how it's represented.

---

## 🧩 Chat Memory Types and Definitions

### 1. `ConversationBufferMemory`
> **Definition:** Stores the entire chat history as a buffer of messages.

- Keeps full conversation.
- Simple and effective for short sessions.

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
```

---

### 2. `ConversationBufferWindowMemory`
> **Definition:** Stores only the most recent `k` interactions.

- Trims older messages.
- Helps control memory size and token usage.

```python
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=3)
```

---

### 3. `ConversationTokenBufferMemory`
> **Definition:** Stores memory based on the number of tokens, not message count.

- Trims history based on token count.
- Great for managing LLM token limits.

```python
from langchain.memory import ConversationTokenBufferMemory

memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=1000)
```

---

### 4. `ConversationSummaryMemory`
> **Definition:** Generates a summary of the conversation using an LLM to reduce context length.

- Compresses long chats into a short summary.
- Ideal for long-running agents.

```python
from langchain.memory import ConversationSummaryMemory

memory = ConversationSummaryMemory(llm=llm)
```

---

## 🛠️ Viewing and Resetting Chat History

- **View history contents:**

```python
print(memory.buffer)
```

- **Clear/reset history:**

```python
memory.clear()
```

---

## 📝 Summary Table

| Memory Type                    | Stores History As         | Best For                         |
|-------------------------------|---------------------------|----------------------------------|
| `ConversationBufferMemory`     | All messages (no limit)    | Short or simple conversations    |
| `ConversationBufferWindowMemory` | Last `k` messages          | Mid-length chats with context     |
| `ConversationTokenBufferMemory` | Messages up to token limit | Token-efficient conversations     |
| `ConversationSummaryMemory`     | Summarized text            | Long-running sessions or agents   |

---

## Retrieval-Augmented Generation 

📚 What is Retrieval-Augmented Generation (RAG)?
**Definition:** RAG is a method that enhances LLMs by retrieving relevant external information (documents) at query time and using that data to generate more accurate responses.

**Key Idea:** Instead of training the LLM on every possible document, you give it the right documents *just in time* when a user asks a question.

**Analogy:** Like a student who quickly refers to a textbook before answering a question.

🧱 RAG Pipeline: The Building Blocks
1. **Document Loading** – Bringing in files (PDFs, DOCX, etc.) into your system.
2. **Document Splitting** – Breaking large texts into smaller, digestible chunks.
3. **Embedding** – Converting text chunks into vectors (numeric representations).
4. **Storing** – Saving those vectors in a searchable vector database.
5. **Retrieval** – Finding the most relevant chunks when a user asks something.
6. **Generation** – Using the retrieved context to generate a response.


🥽 Document Loading
Bring in raw content from various formats:
- **PyPDFLoader** – Loads and extracts text from PDFs.
- **Docx2txtLoader** – Extracts text from Microsoft Word `.docx` files.


✂️ Document Splitting
Split documents into manageable pieces:
- **Character Text Splitter** – Divides based on fixed character count.
- **Markdown Header Text Splitter** – Splits based on markdown headings to preserve structure.


🧠 Document Embedding
Convert each document chunk into a vector (a list of numbers) so that we can search for similar ones later.

- Embedding models like **OpenAI Embeddings** are commonly used.


💾 Vector Store
Store and index your document vectors:
- **Chroma Vectorstore** – A fast, lightweight tool to store and query vectors.
- **Managing Vector Stores** – Allows inspection, deletion, and update of stored vectors.


🔍 Retrieval Techniques
Find the most relevant document chunks:
- **Similarity Search** – Fetches chunks closest in meaning to the user’s query.
- **Maximal Marginal Relevance (MMR)** – Improves diversity in results by reducing overlap.
- **Vector Backend Retriever** – Plug-in layer for accessing different vector stores.

🧾 Generation Phase
- **Stuffing Documents** – Put the retrieved chunks into the prompt alongside the question.
- **Generating Response** – Use the LLM to answer using that prompt context.


Summary
- RAG allows LLMs to stay current with private/internal knowledge.
- It uses retrieval to bring relevant content at response time.
- You don’t need to re-train your model — just manage your data pipeline.

---

## Agent Tooling  
(Include content here)  

---

## LangChain Expression Language (LCEL)  
🔍 Definition  
LangChain Expression Language (LCEL) is a declarative and composable syntax within LangChain for building chains of operations. It enables developers to connect components such as prompts, language models, tools, and output parsers in a clear and structured way using intuitive expressions. Each component behaves like a callable unit, known as a "runnable," that can be linked together to form pipelines.

❓ Why Use LCEL  
LCEL simplifies the process of designing and executing multi-step language model workflows. It replaces verbose, class-based chaining with a streamlined syntax that is easier to read and maintain. LCEL encourages modular programming, supports advanced features like streaming and batching, and enables rapid prototyping of complex chains.

✅ Benefits  
- Declarative syntax that focuses on what to do, not how to do it  
- Modular design that makes components easy to reuse  
- Improved readability for both simple and complex workflows  
- Native support for streaming and batching operations  
- Seamless integration with LangChain tools and features  

🔗 Chain  
A chain in LCEL is a sequence of runnable components connected in a pipeline. Each component processes input and passes the result to the next. Chains allow for clear, logical construction of workflows involving prompts, models, and output handlers.

🧪 Batch  
Batching in LCEL allows multiple inputs to be processed at once through the same chain. It is ideal for bulk tasks like running the same prompt across many items, making it efficient for scaling up inference or evaluations.

🌀 Stream  
Streaming in LCEL allows outputs from language models to be received incrementally as they are generated. This is useful for real-time applications where immediate feedback is important, such as chatbots or live data processing.

🧱 Runnables

LangChain Runnables are the foundational building blocks for constructing modular, composable, and testable pipelines in language model applications. This section covers their definition, composition, parallelism, and visualization.

🔹 What Are Runnables?
Runnables are the core abstraction in LangChain representing any unit of computation that takes input and produces output. They enable a consistent and composable interface for building LLM-based pipelines.

🔹 Chaining Runnables
Runnables can be chained to form a sequence where the output of one becomes the input of the next. This allows modular and readable pipeline construction.

🔹 Piping with `.pipe()`
`.pipe()` is a method for chaining Runnables explicitly. It is functionally equivalent to using the `|` operator but may be clearer in complex setups.

🔹 Branching with `RunnableParallel`
`RunnableParallel` enables multiple Runnables to be executed in parallel on different branches of input. Each branch can process the input differently and return a combined result.

🔹 Visualizing Chains with `grandalf`
Chains of Runnables can be visualized as graphs using the `grandalf` library. This is useful for debugging, documentation, and understanding pipeline structure.

✅ Summary
- **Runnables** are composable units of work.
- Use chaining and piping to build modular workflows.
- Apply `.map()` for parallel inputs and `RunnableParallel` for branching logic.
- Visualize chains using `grandalf` to gain clarity on structure and flow.

Lambda Function

    A **lambda function** is a small, anonymous function defined using a single expression. In LangChain, it is used to embed concise logic within pipelines — such as transforming inputs, conditionally selecting outputs, or defining temporary behaviors — without requiring a full named function. Its main strength is simplicity and quick inline usage.

RunnableLambda

    **RunnableLambda** is a LangChain utility that wraps a regular Python function — including lambdas — into a **Runnable** interface. This allows it to behave like other LangChain components (e.g., models, retrievers) and be composed into chains. It standardizes function execution so it can be invoked, streamed, or combined with other steps.

@chain Decorator

    The **@chain** decorator is used to define a custom step in a LangChain pipeline. When applied to a function, it converts it into a RunnableChain, making it compatible with LangChain's chaining system. This allows developers to build and reuse modular steps that can be linked together with inputs and outputs flowing between them.

itemgetter

    **`itemgetter`** is a utility (from Python’s `operator` module) that retrieves specific values from a data structure, like a dictionary. In LangChain, it’s often used to extract fields (e.g., `"input"` or `"question"`) from structured input objects before passing them to another component. This helps route or filter information cleanly inside a chain.

Memory

    **Memory** in LangChain refers to a component that stores and retrieves state across multiple interactions. It allows chains or agents to maintain **context** — for example, remembering prior messages in a conversation. Different memory types (like buffer or summary memory) determine how information is stored and recalled, enabling more natural and coherent interactions over time.





