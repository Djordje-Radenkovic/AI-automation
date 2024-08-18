###############################################################################
                            # Manually Input Text
###############################################################################

# libraries
from barfi import Block

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