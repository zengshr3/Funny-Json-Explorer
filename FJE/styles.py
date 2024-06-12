class RectangleStyle:
    def __init__(self, icons):
        self.icons = icons

    def show(self, json_data):
        # 调用递归来处理数据并储存，来获得最大长度
        output_lines = []
        self._traverse(json_data, output_lines)
        max_length = max(len(line) for line in output_lines)
        #显示全文
        # print('┌' + '─' * (max_length-1) + '┐')
        #加上左右边界
        output_lines[0].replace("├","┌")
        for i,line in enumerate(output_lines):
            if i == 0:
                print('┌' + line[2:].ljust(max_length,'─') + '──┐')
            elif i == len(output_lines) - 1:
                print('└──' + line[3:].ljust(max_length,'─') + '┘')
            else:
                print( line.ljust(max_length+3,'─') + '|')

        # print('└' + '─' * (max_length-1) + '┘')
    def _traverse(self, data, output_lines,indent=0, prefix=""):
        if isinstance(data, dict):
            length = len(data)
            # print(length)
            for i, (key, value) in enumerate(data.items()):
                connector = self.icons.node if isinstance(value, dict) else self.icons.leaf
                if isinstance(value,str):
                    output_lines.append(prefix + connector + ' ' + key+':'+str(value))
                    # print(prefix + connector + ' ' + key+':'+str(value))#
                else:
                    output_lines.append (prefix + connector + ' ' + key)#

                if isinstance(value, (dict, list)):
                    extension = '|  ' #
                    if(value):
                        self._traverse(value, output_lines,indent + 4, prefix + extension)
                # else:
                #     if(value):
                #         print(prefix + ('│  ' if i < length - 1 else '   ') + ' ' * 4 + self.icons.leaf + ' lll' + str(value))


class TreeStyle:
    def __init__(self, icons):
        self.icons = icons
    def show(self, json_data):
        self._traverse(json_data)

    def _traverse(self, data, indent=0, prefix=""):
        if isinstance(data, dict):
            length = len(data)
            for i, (key, value) in enumerate(data.items()):
                connector = self.icons.node if isinstance(value, dict) else self.icons.leaf
                if isinstance(value,str):
                    print(prefix + connector + ' ' + key+':'+str(value))#
                else:
                    print(prefix + connector + ' ' + key)#

                if isinstance(value, (dict, list)):
                    extension = '|  ' if i < length - 1 else '   '
                    if(value):
                        self._traverse(value, indent + 4, prefix + extension)
                # else:
                #     if(value):
                #         print(prefix + ('│  ' if i < length - 1 else '   ') + ' ' * 4 + self.icons.leaf + ' lll' + str(value))


