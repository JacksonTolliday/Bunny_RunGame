class Rabbit(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/bunnysheet5.png",
        Frame(25,217,35,32), 8, 'horizontal')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "a", self.rotl)
        SpaceGame.listenKeyEvent("keydown", "d", self.rotr)
        self.fxcenter = self.fycenter = 0.5
        self.thrust = 0
        self.thrustframe = 1
