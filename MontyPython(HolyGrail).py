from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class Person(Sprite):
    """
    
    """
    asset = ImageAsset("images/platformer_sprites_base.png",
        Frame(0, 256, 64, 64), 8, 'horizontal')
    asset.append("images/platformer_sprites_base -left.png",
        Frame(0, 256, 64, 64), 8, 'horizontal')
    asset.append("images/platformer_sprites_base.png",
        Frame(256, 0, 64, 64), 4, 'horizontal')
    asset.append("images/platformer_sprites_base.png",
        Frame(0, 64, 64, 64), 4, 'horizontal')
    asset.append("images/platformer_sprites_base -left.png",
        Frame(0, 0, 64, 64), 4, 'horizontal')
    asset.append("images/platformer_sprites_base -left.png",
        Frame(256, 64, 64, 64), 4, 'horizontal')
    asset.append("images/platformer_sprites_base.png",
        Frame(0, 512, 64, 64), 1, 'horizontal')
    asset.append("images/platformer_sprites_base -left.png",
        Frame(448, 512, 64, 64), 1, 'horizontal')
    asset.append("images/platformer_sprites_base.png",
        Frame(0, 320, 64, 64), 8, 'horizontal')
    def __init__(self, position):
        super().__init__(Person.asset, position)
        self.vl = 0
        self.vr = 0
        self.tv = 0
        Game.listenKeyEvent("keydown", "w", self.jump)
        Game.listenKeyEvent("keydown", "a", self.left)
        Game.listenKeyEvent("keydown", "d", self.right)
        Game.listenKeyEvent("keydown", "s", self.drop)
        self.fxcenter = self.fycenter = 0.5
        self.vertmov = 0
        self.animater = 0
        self.animatel = 15
        self.animaterr = 16
        self.animatelr = 30
        self.animaterd = 0
        self.animateld = 0
        self.animaterrj = 34
        self.tvlist = []
        self.setImage(32)
        self.dead = False

    def step(self):
        self.tv = self.vr - self.vl
        if self.tv > 6:
            self.tv = 6
        if self.tv < -6:
            self.tv = -6
        self.y += self.vertmov
        self.tvlist.append(self.tv)
        if self.y < 400:
            self.vertmov += 1
        if self.y > 400:
            self.y = 400
            vertmov = 0
        if self.y < 400:
            if self.dead == False:
                if self.tv > 2:
                    self.setImage(self.animaterrj)
                    self.animaterr += 0.5
                if self.tv < 0:
                    pass
                if self.tv == 0:
                    pass
        if self.vertmov == 0 or self.y == 400:
            if self.dead == False:
                if self.tv == 0:
                    if self.tvlist[(len(self.tvlist))-2] < 0:
                        self.setImage(33)
                    if self.tvlist[(len(self.tvlist))-2] > 0:
                        self.setImage(32)
                    else:
                        pass
                if self.tv > 0:
                    if self.tv < 3:
                        self.setImage(self.animater)
                        self.animater += 0.25
                        if self.animater == 8:
                            self.animater = 0
                if self.tv > 2:
                    self.setImage(self.animaterr)
                    self.animaterr += 0.25
                    if self.animaterr == 23:
                        self.animaterr = 16
                if self.tv < 0:
                    if self.tv > -3:
                        self.setImage(self.animatel)
                        self.animatel -= 0.25
                        if self.animatel <= 8:
                            self.animatel = 14
                if self.tv < -2:
                    self.setImage(self.animatelr)
                    self.animatelr -= 0.25
                    if self.animatelr <= 24.25:
                        self.animatelr = 30.5
            '''if self.dead == True:
                if self.tvlist[(len(self.tvlist))-2] < 0:
                    self.setImage(self.animateld)
                    self.animateld -= 0.25
                if self.tvlist[(len(self.tvlist))-2] > 0:
                    self.setImage(self.animaterd)
                    self.animaterd += 0.25
                else:
                    pass'''
        collides = self.collidingWithSprites(ObstacleS)
        collides.extend(self.collidingWithSprites(ObstacleR))
        for player in collides:
            if self.tvlist[(len(self.tvlist))-2] < 0:
                global myapp
            if self.tvlist[(len(self.tvlist))-2] > 0:
                global myapp
            self.tv = 0
            

    def left(self, event):
        self.vl += 1
        
    def right(self, event):
        self.vr += 1
    
    def jump(self, event):
        if self.y == 400:
            self.vertmov -= 14

    def drop(self, event):
        self.vertmov += 1

    def death(self, event):
        self.dead = True

class ObstacleS(Sprite):
    
    asset = ImageAsset("images/platformer_sprites_base.png",
        Frame(0, 192, 64, 64), 8, 'horizontal')
    asset.append("images/platformer_sprites_base -left.png",
        Frame(0, 192, 64, 64), 8, 'horizontal')

    def __init__(self, position):
        super().__init__(ObstacleS.asset, position)
        self.animateosr = 0
        self.animateosl = 8
        #ok, so 2 types of obstacles; 1 runs the other doesn't. simple enough.

    def step(self):
        global myapp
        self.x -= myapp.p.tv
        self.tvlist = myapp.p.tvlist
        if self.tvlist[(len(self.tvlist))-2] > 0:
            self.setImage(self.animateosl)
            self.animateosl -= 0.2
            if self.animateosl >= 15:
                self.animateosl = 8
        if self.tvlist[(len(self.tvlist))-2] < 0:
            self.setImage(self.animateosr)
            self.animateosr += 0.2
            if self.animateosr >= 8:
                self.animateosr = 0

class ObstacleR(Sprite):
    
    asset = ImageAsset("images/platformer_sprites_base.png",
        Frame(0, 256, 64, 64), 8, 'horizontal')
    asset.append("images/platformer_sprites_base -left.png",
        Frame(0, 256, 64, 64), 8, 'horizontal')

    def __init__(self, position):
        super().__init__(ObstacleR.asset, position)
        animateosr = 0
        animateosl = 8
        #ok, so 2 types of obstacles; 1 runs the other doesn't. simple enough.

    def step(self):
        pass

class Game(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        pic_asset = ImageAsset("images/backgroundexperiment.png", Frame(0, 0, 960, 672), 1, 'horizontal')
        linpic_asset = ImageAsset("images/Game_Background_701.jpg", Frame(0, 0, 1280, 640), 1, 'horizontal')
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        self.bg1 = Sprite(linpic_asset, (0,-60))
        self.bg2 = Sprite(linpic_asset, (1152,-60))
        self.bg1.scale = 0.9
        self.bg2.scale = 0.9
        self.p = Person((Game.width/2,400))
        'self.os = ObstacleS((800,369))'


    def step(self):
        for player in self.getSpritesbyClass(Person):
            player.step()
            self.bg1.x -= player.tv
            self.bg2.x -= player.tv
            if self.bg2.x >= 0:
                self.bg1.x = self.bg2.x-1152
            if self.bg1.x >= 0:
                self.bg2.x = self.bg1.x-1152
                
            if self.bg2.x <= 0:
                self.bg1.x = self.bg2.x+1152
            if self.bg1.x <= 0:
                self.bg2.x = self.bg1.x+1152
        for obs in self.getSpritesbyClass(ObstacleS):
            obs.step()
            
myapp = Game()
myapp.run()
