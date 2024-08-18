# option types: checkbox, input, integer, number, select, slider, display
# implement: scrape website, summarise, custom GPT, replace, split, custom python
# make white, put results in sidebar, display intermediate results
# requirements, gitignore

# import libraries
from barfi import Block, st_barfi, barfi_schemas
import streamlit as st
from streamlit_navigation_bar import st_navbar

# import blocks
from Blocks.input import input_csv_block, input_pdf_block, input_word_block, input_excel_block, input_text_block, input_url_block
from Blocks.result import result_block

# streamlit settings
st.set_page_config(
    page_title="Your App Title",
    page_icon=":rocket:",  # You can use emoji or path to a custom icon
    layout="wide"  # Or 'centered'
)

# navbar - optional
#page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
#st.write(page)

# set barfi parameters
base_blocks = [input_csv_block, input_pdf_block, input_word_block, result_block, input_text_block, input_excel_block, input_url_block]

col3, col4, col5 = st.columns([2,3,2])

with col3:
    compute_engine = st.checkbox('Activate Computation', value=True)
with col5:
    saved_schemas = barfi_schemas()
    barfi_schema_name = st.selectbox(
        'Load existing schema:', saved_schemas, index = saved_schemas.index('blank'))

# run barfi
barfi_result = st_barfi(base_blocks=base_blocks, compute_engine = compute_engine, load_schema=barfi_schema_name)

if barfi_result:
        with st.sidebar:
            st.success('Ran Successfully', icon="✅")
            st.title('Result:')
            st.code(barfi_result['Result-1']['block'].get_interface(name='any'), language='')