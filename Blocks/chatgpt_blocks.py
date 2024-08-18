###############################################################################
                            # Custom AI Blocks
###############################################################################

# libraries
from openai import OpenAI
import os
from dotenv import load_dotenv
from barfi import Block

# load environment variables
load_dotenv()

# get API key
api_key = os.environ.get("OPENAI_API_KEY")

# initialise client
client = OpenAI()

# Ask ChatGPT Question --------------------------------------------------------

# define block
ask_chatgpt_block = Block(name='Ask ChatGPT')

# add display option
ask_chatgpt_block.add_option(name='display-option', type='display', value = 'ask question')

# add text input
ask_chatgpt_block.add_option(name='input-option', type='input')

# add output
ask_chatgpt_block.add_output(name='text')

def ask_chatgpt_funct(self):
    
    question = self.get_option(name='input-option')
    
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
      ]
    )
    
    self.set_interface(name='text', value=completion.choices[0].message.content)
    
ask_chatgpt_block.add_compute(ask_chatgpt_funct)

# Summariser ------------------------------------------------------------------

summariser_block = Block(name='Summariser')

summariser_block.add_input(name='input-text')

summariser_block.add_option(name='display-option', type='display', value='how many characters should summary be?')

summariser_block.add_option(name='length-option',type='integer', value=500)

summariser_block.add_output(name='output-text')

def summariser_funct(self):
    input_text = self.get_interface(name='input-text')
    length = self.get_option(name='length-option')
    
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
          {"role": "system", "content": "You are a helpful assistant for text summarization."},
          {"role": "user", "content": f"Summarize the following document with {length} characters: Prompt: {input_text}"},
      ]
    )
    
    self.set_interface(name='output-text', value=completion.choices[0].message.content)

summariser_block.add_compute(summariser_funct)

# RAG -------------------------------------------------------------------------

rag_block = Block(name='RAG')

rag_block.add_input(name='context-text')

rag_block.add_option(name='display-option', type='display', value='ask question to be answered from context')

rag_block.add_option(name='question', type='input')

rag_block.add_output(name='text')

def rag_funct(self):
    context = self.get_interface(name='context-text')
    question = self.get_option(name='question')
    
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": f"Answer the Question only based on Context: Question: {question} \n\n Context: {context}"},
      ]
    )
    self.set_interface(name='text', value=completion.choices[0].message.content)

rag_block.add_compute(rag_funct)



