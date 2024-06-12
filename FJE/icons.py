class Icons:
    def __init__(self):
        self.node = None
        self.leaf = None

class DefaultIcons(Icons):
    def __init__(self):
        super().__init__()
        self.node = '├─'
        self.leaf = '└─'

class PokerIcons(Icons):
    def __init__(self):
        super().__init__()
        self.node = '├─♢'
        self.leaf = '└─♤'
