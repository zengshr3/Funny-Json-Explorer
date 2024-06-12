import argparse
import json
from factories.total_factory import TotalFactory

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
    #根据参数调用抽象工厂创建工厂，生产不同的icon
    factory = TotalFactory.create_factory(args.style, args.icon)
    explorer = factory.create_explorer()
    explorer.show(json_data)

if __name__ == '__main__':
    main()
