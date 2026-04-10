import streamlit as st
import requests

# 1. Design the Page
st.title("🤖 Jarvis: The Concept Simplifier")
st.write("Type a complex AI or programming concept below, and I will explain it simply.")

# 2. Create the Input Box
user_concept = st.text_input("Concept to simplify (e.g., FastAPI, LangGraph, LLM):")

# 3. Create the Button and Logic
if st.button("Simplify it for me"):
    
    if user_concept:
        # Show a loading spinner while we wait for the backend
        with st.spinner("Jarvis is thinking..."):
            
            # 4. Make the call to the FastAPI Kitchen!
            # We send the user_concept to exactly the URL we tested earlier
            response = requests.post(
                "https://jarvis-agent-qqfk.onrender.com/simplify", 
                params={"concept": user_concept}
            )
            
            # 5. Extract the answer and display it
            if response.status_code == 200:
                data = response.json()
                st.success(data["explanation"])
            else:
                st.error("Something went wrong in the kitchen!")
    else:
        st.warning("Please enter a concept first!")