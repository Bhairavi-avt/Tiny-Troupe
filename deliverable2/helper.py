import streamlit as st
import os
import pandas as pd

os.system("pip install together")

from together import Together

import os

# Set the environment variable (just for testing purposes)
os.environ["api"] = "Together_API_KEY"

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

    # Create a completion request with the prompt
    response = client.chat.completions.create(

        # Use the Llama-3-8b-chat-hf model
        model="meta-llama/Llama-3-8b-chat-hf",

        # Define the prompt as a user message
        messages=[
            {
                "role": "user",
                "content": prompt  # Use the input prompt
            }
        ],
        temperature=0.7,
    )

    # Return the content of the first response message
    return response.choices[0].message.content
