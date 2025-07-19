# import os

# from dotenv import load_dotenv

# from agents import (
#     Agent, 
#     AsyncOpenAI, 
#     OpenAIChatCompletionsModel, 
#     RunConfig, 
#     Runner
# )

# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# config = RunConfig(
#     model= model,
#     model_provider= external_client,
#     tracing_disabled= True
# )

# agent = Agent(
#     name = "Digital Marketer",
#     instructions= "You are a pro level digital marketing expert.so you can reply only digital marketing related question. because you are digital marketer expert."
# )

# result = Runner.run_sync(
#     agent,
#     input="Hello! can you solve my coding error?",
#     run_config=config
# )

# print(result.final_output)



import os

from dotenv import load_dotenv

from agents import (
    Agent, 
    AsyncOpenAI, 
    OpenAIChatCompletionsModel, 
    RunConfig, 
    Runner
)

load_dotenv()

gemini_api_key= os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name= "Mathemetics Tutor",
    instructions="You are a high level mathemetics expert tutor. and you only answer mathemtics realted question."
)

result = Runner.run_sync(
    agent,
    input="Hello! who are you? Please tell m in detail.",
    run_config=config
)

print(result.final_output)