###############################################################################
                # Input: Word, PDF, Excel, CSV, URL, Manual Text
###############################################################################

# libraries
import os
from barfi import Block
import csv
import PyPDF2  # For reading PDF files
import pandas as pd  # For reading Excel files
import docx  # For reading Word files
import requests
from bs4 import BeautifulSoup

# Read CSV File Input ---------------------------------------------------------

# define block
input_csv_block = Block(name='Input CSV')

# add text
input_csv_block.add_option(name='display-option', type='display', value='select CSV file')

# take names of all csv files in current directory
csv_files = [f for f in os.listdir('Data') if f.endswith('.csv')]
if len(csv_files)==0:
    csv_files = ['']

# add select-file input
input_csv_block.add_option(name='select-file', type='select', items=csv_files, value='')

# add output
input_csv_block.add_output(name='dict of lists')

# define function to read csv
def input_csv_funct(self):
    file_path = self.get_option(name='select-file')
    df = pd.read_csv('Data/'+file_path)
    self.set_interface(name='dict of lists', value=df.to_dict(orient='list'))  

    
# add function to block
input_csv_block.add_compute(input_csv_funct)


# Read PDF File Input ---------------------------------------------------------

# Define block
input_pdf_block = Block(name='Input PDF')

# Add display option
input_pdf_block.add_option(name='display-option', type='display', value='select PDF file')

# Get PDF files in the current directory
pdf_files = [f for f in os.listdir('Data') if f.endswith('.pdf')]
if len(pdf_files) == 0:
    pdf_files = ['']

# Add select-file input
input_pdf_block.add_option(name='select-file', type='select', items=pdf_files, value='')

# Add output
input_pdf_block.add_output(name='text')

# Define function to read PDF
def input_pdf_funct(self):
    file_path = self.get_option(name='select-file')
    with open('Data/'+file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    self.set_interface(name='text', value=text[:500])  # Example: returning the first 500 characters

# Add function to block
input_pdf_block.add_compute(input_pdf_funct)

# Read Excel File Input -------------------------------------------------------

# Define block
input_excel_block = Block(name='Input Excel')

# Add display option
input_excel_block.add_option(name='display-option', type='display', value='select Excel file')

# Get Excel files in the current directory
excel_files = [f for f in os.listdir('Data') if f.endswith(('.xls', '.xlsx'))]
if len(excel_files) == 0:
    excel_files = ['']

# Add select-file input
input_excel_block.add_option(name='select-file', type='select', items=excel_files, value='')

# Add output
input_excel_block.add_output(name='dict of lists')

# Define function to read Excel
def input_excel_funct(self):
    file_path = self.get_option(name='select-file')
    df = pd.read_excel('Data/'+file_path)
    self.set_interface(name='dict of lists', value=df.to_dict(orient='list'))  # Example: returning column names

# Add function to block
input_excel_block.add_compute(input_excel_funct)

# Read Word File Input --------------------------------------------------------

# Define block
input_word_block = Block(name='Input Word')

# Add display option
input_word_block.add_option(name='display-option', type='display', value='select word file')

# Get Word files in the current directory
word_files = [f for f in os.listdir('Data') if f.endswith('.docx')]
if len(word_files) == 0:
    word_files = ['']

# Add select-file input
input_word_block.add_option(name='select-file', type='select', items=word_files, value='')

# Add output
input_word_block.add_output(name='text')

# Define function to read Word files
def input_word_funct(self):
    file_path = self.get_option(name='select-file')
    doc = docx.Document('Data/'+file_path)
    text = '\n'.join([para.text for para in doc.paragraphs])
    self.set_interface(name='text', value=text[:500])  # Example: returning the first 500 characters

# Add function to block
input_word_block.add_compute(input_word_funct)

# Input Text Manually ---------------------------------------------------------

# define block
input_text_block = Block(name='Input Text')

# add text
input_text_block.add_option(name='display-option', type='display', value='Input Text Manually.')

# add the input option
input_text_block.add_option(name='input-option', type='input')

# add output
input_text_block.add_output('text')

# function
def input_text_funct(self):
    
    input1 = self.get_option(name='input-option')
    
    self.set_interface(name='text', value=str(input1))
    
# add function to block
input_text_block.add_compute(input_text_funct)

# Scrape Website URl ----------------------------------------------------------

# Define block
input_url_block = Block(name='Input Scrape URL')

# Add display option
input_url_block.add_option(name='display-option', type='display', value='input URL')

# Add select-file input
input_url_block.add_option(name='input-url', type='input')

# Add output
input_url_block.add_output(name='text')

# scraper function
def input_url_funct(self):
    url = self.get_option(name='input-url')
    
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        all_text = soup.get_text(separator='\n', strip=True)
    else:
        all_text = 'Scraper failed.'
    
    self.set_interface(name='text', value = all_text[:1000])
    
input_url_block.add_compute(input_url_funct)










