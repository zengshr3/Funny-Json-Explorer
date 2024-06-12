from factories.factory import TreeFactory, RectangleFactory

class TotalFactory:
    @staticmethod#无需创建实例即可调用该函数
    def create_factory(style, icon):
        if style == 'tree':
            return TreeFactory(icon)
        elif style == 'rectangle':
            return RectangleFactory(icon)
