# pip install -qU langchain "langchain[anthropic]"
from langchain.agents import create_agent
import os

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    # Here you would normally call a real weather API
    return f"The weather in {city} is 72°F and sunny."

agent = create_agent(
    model="claude-sonnet-4-5-20250929",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

print(f'Running agent...')

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
    config={"run_name": os.path.basename(__file__)},
)

print(response["messages"][-1].content)