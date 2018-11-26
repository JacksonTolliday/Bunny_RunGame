class Rabbit(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/bunnysheet5.png",
        Frame(25,217,35,32), 8, 'horizontal')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.setImage(0)
        self.setImage(1)
        self.setImage(2)
        self.setImage(3)
        self.setImage(4)
        self.setImage(5)
        self.setImage(6)
        self.setImage(7)
        