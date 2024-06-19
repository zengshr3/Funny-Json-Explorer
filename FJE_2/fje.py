import argparse
import json
from FJE_context import FunnyJsonExplorer
from icons import DefaultIcons,PokerIcons
from style_strategy import TreeStyle,RectangleStyle
from iterator import JsonIterator
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def main():
    parser = argparse.ArgumentParser(description="Funny JSON Explorer (FJE)")#参数处理
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', type=str, choices=['tree', 'rectangle'], default='tree', help='Display style')
    parser.add_argument('-i', '--icon', type=str, choices=['default', 'poker'], default='default', help='Icon family')
    
    args = parser.parse_args()

    json_data = load_json(args.file)
    iterator = JsonIterator(json_data)

    if args.icon == 'default':
        icons=DefaultIcons()
    elif args.icon == 'poker':
        icons=PokerIcons()
    
    # Choose style
    if args.style == 'tree':
        style=TreeStyle(icons)
    elif args.style == 'rectangle':
        style=RectangleStyle(icons)
    
    # Create and show the FunnyJsonExplorer
    fje = FunnyJsonExplorer(json_data, style)
    fje.show()
    iterator = JsonIterator(json_data)
    # for key, value, level in iterator:
    #     print(str(key)+" " +str(value)+" "+str(level))
if __name__ == '__main__':
    main()
