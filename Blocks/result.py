###############################################################################
                            # Display Result
###############################################################################

# read libraries
from barfi import Block

# define block
result_block = Block(name='Result')

# add input
result_block.add_input(name='any')

# function 
def result_func(self):
    in_1 = self.get_interface(name='any')
    
# add function    
result_block.add_compute(result_func)
