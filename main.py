from fastapi import FastAPI
from agent import app_graph # We import the brain we just built!

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Jarvis backend is running perfectly!"}

@app.post("/simplify")
def simplify_concept(concept: str):
    
    # 1. We feed the concept into our LangGraph brain
    # We must pass it in as a dictionary because our AgentState expects a dictionary
    result = app_graph.invoke({"concept": concept})
    
    # 2. We extract the AI's final explanation from the result
    final_answer = result["explanation"]
    
    # 3. We return it to the user
    return {"concept": concept, "explanation": final_answer}