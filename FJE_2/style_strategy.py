from icons import Icons

class BaseStyle:
    def __init__(self, icons):
        self.icons = icons

    def apply(self, key, value, indent, is_last):
        raise NotImplementedError

class TreeStyle(BaseStyle):
    def apply(self, key, value, indent, is_last,prefix=""):
        #传进来判断value是字符串则直接输出，是字典或者其他的只输出key然后等待递归 
        if isinstance(value,str):
            return (prefix +' ' * indent + self.icons.leaf + ' '+key +': ' + value)
        elif key is not None:
            return (prefix +' ' * indent + (self.icons.leaf if is_last else self.icons.node) + ' ' + str(key))
    def format_output(self, output_lines):
        max_length = max(len(line) for line in output_lines)
        formatted_output = []
        for line in output_lines:
            formatted_output.append( line.ljust(max_length) )
        return formatted_output            

class RectangleStyle(BaseStyle):
    def apply(self, key, value, indent, is_last,prefix=""):
        #传进来判断value是字符串则直接输出，是字典或者其他的只输出key然后等待递归 
        if isinstance(value,str):
            return (prefix +' ' * indent + self.icons.leaf + ' '+key +': ' + value)
        elif key is not None:
            return (prefix +' ' * indent + (self.icons.leaf if is_last else self.icons.node) + ' ' + str(key))
    

    def format_output(self, output_lines):
        max_length = max(len(line) for line in output_lines)
        formatted_output = []
        for i,line in enumerate(output_lines):
            if i == len(output_lines) - 1:
                formatted_output.append('└──' + line[3:].ljust(max_length-3,'─') + '┘')
            else:
                formatted_output.append( line.ljust(max_length,'─') + '│')
        return formatted_output