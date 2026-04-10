from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq 
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    concept: str
    explanation: str

def simplify_node(state: AgentState):
    # 2. CHANGE THE LLM ENGINE HERE
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7) 
    
    concept_to_explain = state["concept"]
    
    messages = [
        SystemMessage(content="You are a senior software engineer and AI expert. Explain the given technology or concept in one simple, easy-to-understand paragraph. Do not use jargon."),
        HumanMessage(content=f"Please simplify this concept for me: {concept_to_explain}")
    ]
    
    response = llm.invoke(messages)
    
    return {"explanation": response.content}

# 3. Build and Compile the Graph
# This maps out the flowchart of how the agent thinks.
builder = StateGraph(AgentState)

# Add our single step to the graph
builder.add_node("simplifier", simplify_node)

# Define the flow: Start -> Simplifier -> End
builder.add_edge(START, "simplifier")
builder.add_edge("simplifier", END)

# Compile it into a working brain
app_graph = builder.compile()