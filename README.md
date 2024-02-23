  

## Simple Custome LLM on Llama

POC


## Llama Index

> version: 0.9.25.post1

Install the above version with the following command:

```pip install llama-index==0.9.25.post1```

from llama_index.llms import OpenAI, ChatMessage, LLMMetadata
from llama_index.agent import ReActAgent


llm = OpenAI(
    model=model,
    api_key=semicolons_gateway_api_key,
    api_base=semicolons_gateway_base_url, # api_base represents the endpoint the Llama-Index object will make a call to when invoked
    temperature=0.1
)

# Adjust the below parameters as per the model you've chosen
llm.__class__.metadata = LLMMetadata(
    context_window=4000, 
    num_output=1000,
    is_chat_model=True,
    is_function_calling_model=False, 
    model_name=model,
)


print(llm.chat([ChatMessage(role="user",content="Hi, who are you?")]).message.content)

# agent = ReActAgent.from_tools(tools=[],llm=llm)