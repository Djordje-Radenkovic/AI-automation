###############################################################################
                             # Data Processing Blocks
###############################################################################

# libraries
from barfi import Block

# Split Text ------------------------------------------------------------------

splitter_block = Block(name = 'Text Splitter')

splitter_block.add_input(name='input-text')

splitter_block.add_option(name='display-option', type='display', value='value by which to split')

splitter_block.add_option(name='div-option', type='input')

splitter_block.add_output(name='output-text')

def splitter_funct(self):
    input_text = self.get_interface(name='input-text')
    div = self.get_option(name='div-option')
    self.set_interface(name='output-text', value=input_text.split(div))

splitter_block.add_compute(splitter_funct)

# Replace in Text -------------------------------------------------------------

replace_block = Block(name='Replace Text')

replace_block.add_input(name='input-text')

replace_block.add_option(name='display-option 1', type='display', value='replace:')

replace_block.add_option(name='to_replace', type='input')

replace_block.add_option(name='display-option 2', type='display', value='with:')

replace_block.add_option(name='with', type='input')

replace_block.add_output(name='output-text')

def replace_funct(self):
    input_text = self.get_interface(name='input-text')
    to_replace = self.get_option(name='to_replace')
    instead = self.get_option(name='with')
    output_text = input_text.replace(to_replace, instead)
    self.set_interface(name='output-text', value=output_text)
    
replace_block.add_compute(replace_funct)