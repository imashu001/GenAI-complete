# Tool and function calling

While Folder 1 covered the ReAct control loop conceptually, Folder 2 tackles the foundational technical mechanism that makes agentic execution possible: Function Calling (Tool Calling).

An LLM is fundamentally a text-in, text-out neural network. It cannot natively query your SQL database, run a bash script, or check live stock prices. Function calling bridges this gap by allowing you to provide a JSON Schema or Pydantic model describing your code functions. The model parses a user prompt, determines if an external action is needed, and returns a structured JSON payload containing the function name and arguments—which your backend code then executes.

##  1. The Core 5-Step Function Calling Lifecycle

[1. Define Schema] (Pydantic / JSON Schema) 
        │
        v
[2. Send Request] (User Message + Available Tools sent to LLM API)
        │
        v
[3. Model Returns Tool Call] (LLM responds with structured JSON args, NOT text)
        │
        v
[4. Backend Execution] (Your code executes the local function safely)
        │
        v
[5. Final Synthesis] (Send tool output back to LLM to generate the final response)

 ## 2. Production Code Implementation (02_tools_and_function_calling/pydantic_function_handler.py)
Here is a robust, production-ready Python script demonstrating how to define tools using Pydantic, handle LLM tool call routing, and complete the round-trip conversation loop.