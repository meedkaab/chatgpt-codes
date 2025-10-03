#!/usr/bin/env python3
"""
ChatGPT Code Examples
This file contains example code snippets for working with ChatGPT API
"""

import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def simple_chatgpt_request(prompt):
    """
    Send a simple request to ChatGPT
    
    Args:
        prompt (str): The user's prompt
    
    Returns:
        str: ChatGPT's response
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def chatgpt_with_conversation_history(messages):
    """
    Send a request to ChatGPT with conversation history
    
    Args:
        messages (list): List of message dictionaries with 'role' and 'content'
    
    Returns:
        str: ChatGPT's response
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Example 1: Simple request
    print("Example 1: Simple Request")
    result = simple_chatgpt_request("What is the capital of France?")
    print(f"Response: {result}\n")
    
    # Example 2: Conversation with history
    print("Example 2: Conversation with History")
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I'm doing well, thank you! How can I help you today?"},
        {"role": "user", "content": "Can you explain Python decorators?"}
    ]
    result = chatgpt_with_conversation_history(conversation)
    print(f"Response: {result}")
