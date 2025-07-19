1. Agent
An Agent is an AI persona or entity that behaves according to the instructions you provide. It acts as a specialized assistant or expert to answer questions or perform tasks based on its role.

Agent aik AI entity (persona) hota hai jo aapki instructions ke mutabiq kaam karta hai. Ye aapke questions ke jawab dene ya tasks perform karne ke liye bana hota hai.

Use case:
Agar aap chahte hain ke AI kisi specific role mein behave kare, jese ki digital marketer, customer support, ya math tutor, to aap Agent banate hain.

Key feature:

Aap agent ko name dete hain.

Aap agent ko instructions dete hain ke wo kaise jawab de ya kaam kare.

Example:

python
Copy
Edit
agent = Agent(
    name="Math Tutor",
    instructions="You are a helpful math tutor, answer math questions clearly."
)
2. AsyncOpenAI
AsyncOpenAI is an asynchronous client used to communicate with OpenAI or compatible APIs like Google Gemini. It handles API requests without blocking your program, allowing multiple tasks to run smoothly.

Ye ek client hai jo OpenAI (ya Google Gemini) API ke saath asynchronous communication karta hai. Matlab aap API requests async tareeke se bhej sakte hain, jisse aapka program efficiently multiple requests handle kar sakta hai bina rukawat ke.

Use case:
Jab aapko API calls karni hain, to aap AsyncOpenAI client use karte hain jo aapke API key aur endpoint URL ko set karta hai.

Key features:

API key provide karni hoti hai.

Base URL set karna hota hai agar default OpenAI nahi use kar rahe.

Example:

python
Copy
Edit
client = AsyncOpenAI(
    api_key="aapki_api_key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
3. OpenAIChatCompletionsModel
This component represents the specific AI model you want to use for chat completions. It links your API client to the chosen model like GPT-4 or Gemini.

Ye ek model wrapper hai jo specific OpenAI ya Gemini chat completion models ko represent karta hai. Matlab ye batata hai ke aap kaun sa AI model use karna chahte hain.

Use case:
Aap specify karte hain model ka naam (jese "gpt-4o", "gemini-2.0-flash") aur kis client ke zariye call karna hai.

Key features:

model parameter mein model ka naam dena hota hai.

openai_client mein woh client dena hota hai jo API requests karega (jaise AsyncOpenAI).

Example:

python
Copy
Edit
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)
4. RunConfig
RunConfig is a configuration object that defines how the model and client should run. It holds information like which model to use, which API client to connect, and additional options such as enabling or disabling tracing.

Ye configuration object hai jo batata hai ke model aur client ko kaise run karna hai. Isme aap model, client, aur optional settings set kar sakte hain.

Use case:
Jab aap agent ko run karte hain, to aapko config dena hota hai jisme ye bataya jata hai ki kis model aur client ke saath kaam karna hai.

Key features:

model: Jo aapka AI model hai.

model_provider: Jo API client hai.

tracing_disabled: Agar aap debugging info disable karna chahte hain.

Example:

python
Copy
Edit
config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)
5. Runner
Runner is a utility that executes the agent with given input and configuration. It manages the interaction between your program and the AI, returning the agent’s response either synchronously or asynchronously.

Ye ek utility hai jo agent ko chalata hai. Iske zariye aap agent ko input dete hain aur output lete hain. Isme synchronous (run_sync) aur asynchronous (run_async) dono tareeqe available hain.

Use case:
Jab aapko AI agent se interaction karna hota hai, aap Runner ka use karke input bhejte hain aur response receive karte hain.

Key features:

run_sync(agent, input, run_config) synchronous call hai.

run_async(agent, input, run_config) async call hai.

Example:

python
Copy
Edit
result = Runner.run_sync(
    agent,
    input="Hello! How can you help me?",
    run_config=config
)
print(result.final_output)
