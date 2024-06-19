from iterator import JsonIterator
from style_strategy import RectangleStyle
from style_strategy import TreeStyle

class FunnyJsonExplorer:
    def __init__(self, json_data, style):
        self.json_data = json_data
        self.style = style

    def show(self):
        output_lines = []
        #在show里面可以选择使用哪个版本
        # self._traverse(self.json_data, output_lines)
        self._traverse_with_iterator(output_lines)
        output_lines = self.style.format_output(output_lines)
        for line in output_lines:
            print(line)
    #不使用迭代器的版本
    def _traverse(self, data, output_lines, indent=0, is_last=True,prefix=""):
        if isinstance(data, dict):
            items = list(data.items())
            for i, (key, value) in enumerate(items):
                is_last_item = (i == len(items) - 1)
                
                output_lines.append(self.style.apply(key, value, indent, is_last_item,prefix))
                if isinstance(value,dict):
                    extension=''
                    if isinstance(self.style,TreeStyle) :
                        extension = '│' if not is_last_item else ''
                        self._traverse(value, output_lines, indent+4, is_last_item,prefix+extension)

                    if isinstance(self.style,RectangleStyle):
                        extension = '│  '                         
                        self._traverse(value, output_lines, indent, is_last_item,prefix+extension)
        else:
            output_lines.append(self.style.apply(None, data, indent, is_last,prefix))

    #迭代器优化版本        
    def _traverse_with_iterator(self, output_lines, indent=0, is_last=True,prefix=""):
            iterator = JsonIterator(self.json_data)
            indent_levels=[]
            prelevel=0
            for key, value, level in iterator:
                if not value:
                    indent_levels.append(key)
                if key is not None:
                    is_last=(len(indent_levels)==0)or level<=prelevel
                    extension=''
                    if isinstance(self.style,TreeStyle) :
                        extension = '│  ' if not is_last else ''
                        output_lines.append(self.style.apply(key,value,4*(level-1),is_last,prefix))

                    if isinstance(self.style,RectangleStyle):
                        extension = '│  '  
                        output_lines.append(self.style.apply(key,value,(level-2),is_last,prefix+(level-1)*extension))
 
                    # prefix=prefix+extension     
                    
                    if( len(indent_levels)>0):
                        indent_levels.pop()
                    prelevel=level