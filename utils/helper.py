import streamlit as st
import os
import pandas as pd

os.system("pip install together")

from together import Together

import os

# Set the environment variable (just for testing purposes)
os.environ["api"] = "37f259442b9ccc25a9e91de961b1916ee08b39794435fcfefb28a549db659dab"

# Now, the code can access the api key from the environment variable
client = Together(api_key=os.environ["api"])


def call_llama(prompt: str) -> str:
    """
    Send a prompt to the Llama model and return the response.
    Args:
        prompt (str): The input prompt to send to the Llama model.
    Returns:
        str: The response from the Llama model.
    """
    response = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf", 
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
