from styles import TreeStyle
from styles import RectangleStyle
from icons import DefaultIcons
from icons import PokerIcons

class Factory:
    def __init__(self) -> None:
        pass
    def create_explorer():
        pass
    def get_icons(self):
        pass
    
class TreeFactory(Factory):
    def __init__(self, icon):
        self.icon = icon

    def create_explorer(self):
        return TreeStyle(self.get_icons())

    def get_icons(self):
        if self.icon == 'default':
            return DefaultIcons()
        elif self.icon == 'poker':
            return PokerIcons()

class RectangleFactory(Factory):
    def __init__(self, icon):
        self.icon = icon

    def create_explorer(self):
        return RectangleStyle(self.get_icons())

    def get_icons(self):
        if self.icon == 'default':
            return DefaultIcons()
        elif self.icon == 'poker':
            return PokerIcons()
