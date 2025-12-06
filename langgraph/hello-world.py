from langgraph.graph import StateGraph, MessagesState, START, END
import os

def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}

graph = StateGraph(MessagesState)
graph.add_node(mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
app = graph.compile()

result = app.invoke({"messages": [{"role": "user", "content": "hi!"}]},
             config={"run_name": os.path.basename(__file__)})

print(result["messages"][-1].content)  # Access .content attribute