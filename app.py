# option types: checkbox, input, integer, number, select, slider, display
# implement: replace, split, custom python
# display intermediate results
# requirements

# import libraries
from barfi import Block, st_barfi, barfi_schemas
import streamlit as st
from streamlit_navigation_bar import st_navbar

# import blocks
from Blocks.input_blocks import input_csv_block, input_pdf_block, input_word_block, input_excel_block, input_text_block, input_url_block
from Blocks.result_blocks import result_block
from Blocks.chatgpt_blocks import ask_chatgpt_block, summariser_block, rag_block
from Blocks.processing_blocks import replace_block, splitter_block

# streamlit settings
st.set_page_config(
    page_title="Your App Title",
    page_icon=":elephant:",  # You can use emoji or path to a custom icon
    layout="wide"  # Or 'centered'
)

# navbar - optional
#page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
#st.write(page)

# set barfi parameters
base_blocks = [input_csv_block, input_pdf_block, input_word_block, result_block, 
               input_text_block, input_excel_block, input_url_block, rag_block,
               summariser_block, ask_chatgpt_block, replace_block, splitter_block]

col3, col4 = st.columns([2,5])

with col3:
    saved_schemas = barfi_schemas()
    barfi_schema_name = st.selectbox(
        'Load existing schema:', saved_schemas, index = saved_schemas.index('blank'))
    
#compute_engine = st.checkbox('Activate Computation', value=True)
compute_engine = True

# run barfi
barfi_result = st_barfi(base_blocks=base_blocks, compute_engine = compute_engine, load_schema=barfi_schema_name)

if barfi_result:
        with st.sidebar:
            st.success('Ran Successfully', icon="✅")
            st.title('Result:')
            st.code(barfi_result['Result-1']['block'].get_interface(name='any'), language='')