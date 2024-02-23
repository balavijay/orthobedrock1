from llama_index.llms import OpenAI, ChatMessage, LLMMetadata
from llama_index.agent import ReActAgent


llm = OpenAI(
    model="gpt-35-turbo-16k",
    api_key="sk-jfoNrqmyPiA_xop2fJ53Wg",
    api_base="https://4veynppxjm.us-east-1.awsapprunner.com",
    temperature=0.1
)

# Adjust the below parameters as per the model you've chosen
llm.__class__.metadata = LLMMetadata(
    context_window=4000, 
    num_output=1000,
    is_chat_model=True,
    is_function_calling_model=False, 
    model_name="bedrock/meta.llama2-13b-chat-v1",
)


print(llm.chat([ChatMessage(role="user",content="Hi, who are you?")]).message.content)

# agent = ReActAgent.from_tools(tools=[],llm=llm)