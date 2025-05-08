import streamlit as st
import os
import pandas as pd
from utils.helper import *

# Installing the necessary library
os.system("pip install together")
os.system("python3 -m pip install --no-cache-dir together")

from together import Together

# Set the page config with wide layout
st.set_page_config(layout="wide")
st.title("Dual Agent Simulation 🤖", anchor="top")

# Add custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .sidebar .sidebar-content {
            background-color: #f4f8fb;
            padding: 20px;
        }
        .title {
            font-size: 36px;
            color: #0d47a1;
            font-weight: bold;
        }
        .stTextInput>div>input {
            background-color: #ffffff;
            border-radius: 5px;
            border: 1px solid #ddd;
            padding: 10px;
            font-size: 16px;
        }
        .stSelectbox>div>label {
            font-size: 16px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for user instructions and input
with st.sidebar:
    with st.expander("Instruction Manual"):
        st.markdown("""
            # Duel Agent ChatBot Streamlit App
            
            ## Overview
            This is an interactive simulation featuring two agents: the Interviewer and the Interviewee. Additionally, there is a Guru agent that provides expert feedback during the interview simulation.
            
            **How to Use:**
            - Enter a topic in the input box.
            - Press "Run Simulation!" to start the conversation.
            - View the agent's responses, including feedback from the Guru.
            
            **Credits:**
            - Developed by Bhairavi Borade
        """)

    # Input for the topic
    user_topic = st.text_input("Enter a topic", "Data Science")

    # Dropdown to select agent type
    agent_type = st.selectbox("Choose an Interview Agent:", ["Interviewee", "Guru"])

    # Submit button to run simulation
    submit_button = st.button("Run Simulation!")

    # Button to clear session
    if st.button("Clear Session"):
        st.session_state.messages = []
        st.experimental_rerun()

# Initialize chat history if not already
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat history dynamically
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # Adding an avatar for each role (interviewer, user, guru)
        avatar = "🧑‍💼" if message["role"] == "assistant" else "👩‍💻" if message["role"] == "user" else "👨‍🏫"
        st.markdown(f"{avatar} {message['content']}")

# Create agents
interviewer = call_llama
interviewee = call_llama
guru = call_llama

# Handling conversation flow
if submit_button:
    prompt = f"Ask a question about this topic: {user_topic}"

    # Show the user's input as the first message
    st.chat_message("user").markdown(f"👨‍💻 **Topic:** {user_topic}")
    st.session_state.messages.append({"role": "user", "content": f"👨‍💻 **Topic:** {user_topic}"})

    iter = 0
    list_of_iters = []
    list_of_questions = []
    list_of_answers = []
    list_of_judge_comments = []
    list_of_passes = []

    while True:
        # Interviewer asks the first question
        question = interviewer(prompt)

        # Show the interviewer's question with an avatar
        st.chat_message("assistant").markdown(f"🧑‍💼 **Interviewer:** {question}")
        st.session_state.messages.append({"role": "assistant", "content": f"🧑‍💼 **Interviewer:** {question}"})

        # Interviewee answers the question
        answer = interviewee(f"Answer the question: {question} as an inexperienced candidate.")
        st.chat_message("user").markdown(f"👩‍💻 **Interviewee:** {answer}")
        st.session_state.messages.append({"role": "user", "content": f"👩‍💻 **Interviewee:** {answer}"})

        # Guru provides feedback
        judge_comments = guru(f"Provide expert feedback on the answer: {answer}. Rate it from 1 to 10.")
        st.chat_message("assistant").markdown(f"👨‍🏫 **Guru Feedback:** {judge_comments}")
        st.session_state.messages.append({"role": "assistant", "content": f"👨‍🏫 **Guru Feedback:** {judge_comments}"})

        # Collect all responses
        list_of_iters.append(iter)
        list_of_questions.append(question)
        list_of_answers.append(answer)
        list_of_judge_comments.append(judge_comments)
        list_of_passes.append(1 if '8' in judge_comments else 0)

        # Show a table with responses and feedback
        results_tab = pd.DataFrame({
            "Iter.": list_of_iters,
            "Questions": list_of_questions,
            "Answers": list_of_answers,
            "Judge Comments": list_of_judge_comments,
            "Passed": list_of_passes
        })
        with st.expander("See Explanation"):
            st.table(results_tab)

        # Stop after receiving a positive rating
        if '8' in judge_comments:
            break

        iter += 1
