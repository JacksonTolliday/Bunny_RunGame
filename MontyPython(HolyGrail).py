from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class Person(Sprite):
    """
    
    """
    rightasset = ImageAsset("images/platformer_sprites_base.png",
        Frame(227,0,65,125), 8, 'horizontal')

    leftasset = ImageAsset("images/platformer_sprites_base.png",
        Frame(227,0,65,125), 8, 'horizontal')
    
    def __init__(self, position):
        super().__init__(Person.asset, position)
        self.vl = 0
        self.vr = 0
        Game.listenKeyEvent("keydown", "space", self.bigjump)
        Game.listenKeyEvent("keydown", "w", self.jump)
        Game.listenKeyEvent("keydown", "a", self.left)
        Game.listenKeyEvent("keydown", "d", self.right)
        Game.listenKeyEvent("keydown", "s", self.slow)
        self.fxcenter = self.fycenter = 0.5
        self.thrust = 0


    def step(self):
        self.x += self.vr
        self.x -= self.vl

    def left(self, event):
        self.vl += 1
        
    def right(self, event):
        self.vr += 1

    def jump(self, event):
        self.thrust = 1
        
    def bigjump(self, event):
        self.thrust = 2
