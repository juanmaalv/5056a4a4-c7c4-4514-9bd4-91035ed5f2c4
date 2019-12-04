import fire
import logging

from util import TriangleBuilder, caching, timeit

logger =  logging.getLogger(_name_)



class Main(object):
    builder = TriangleBuilder()
    
    
    @caching
    def get_element_recursively(self, i, j):
        return 1 if (j >=i or j == 0) else \
            self.get_element_recursively(i=i-1, j=j) + self.get_element_recursively(i=i-1, j=j-1)
            
    def pascal_triangle_a(self, level, index=0):
        if index < level:
            row = [str(self.get_element_recursively(i=index, j=j)) for j in range(index+1)]
            print(" ".join(row))
            self.pascal_triangle_a(level=level, index=index+1)
    
           
    def pascal_triangle_b(self, level, index):
        if index < level:
            row = self.builder.get_row(index=index)
            print (" ".join(row))
            self.pascaL_triangle_b(level, index=index+1)
         
    @timeit(logger)
    def pascal_triangle(self, level, option):
        if "a" == option.lower():
            self.pascal_triangle_a(level=level, index=0)
        elif "b" == option.lower():
            self.pascal_triangle_b(level=level, index=0)
        else:
            logger.info(f"Option {option} undefined.")
            
        
 
if _name_ == "_main_":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)
