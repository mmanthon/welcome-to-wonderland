'''
framework referenced from:
Lukas Peraza, 2015 for 15-112 Pygame Lecture
https://github.com/LBPeraza/Pygame-Asteroids
'''
import pygame
import random
from pygamegame import PygameGame
from music import Music
from SplashScreen import SplashScreen
from Intro import Intro
from ActionBox import ActionBox

class Game(PygameGame):
            
    # mode changes throughout game for display
    MODE = 'Title Screen'
    # possible modes: Title Screen, Credits, Intro, Wheel, Trust/Forsake, Battle
    TIMEKEEP = 0
    
    def init(self):
        self.bgColor = (0, 0, 0)
        
        # initialize splash
        SplashScreen.init()
        self.logo = SplashScreen(self.width, self.height)
        
        # initialize intro
        Intro.init()
        self.intro = Intro()
        
        # initialize box
        ActionBox.init()
        self.actionBox = ActionBox()
        
        #initialize music
        self.startMusic = True
        Music.init()
        self.sounds = Music()
       

    def keyPressed(self, code, mod):
        
        # change music volume
        if code == pygame.K_EQUALS:
            Music.changeVol(0.05)
        elif code == pygame.K_MINUS:
            Music.changeVol(-0.05)
        
        # start game, view credits
        if Game.MODE=='Title Screen':
            if code == pygame.K_RETURN:
                Game.MODE = 'Intro'
                self.startMusic = True
            elif code == pygame.K_SPACE:
                Game.MODE = 'Credits'
                
        elif Game.MODE == 'Credits':
            if code == pygame.K_ESCAPE:
                Game.MODE = 'Title Screen'
        
        # skip intro
        elif Game.MODE == 'Intro':
            if code == pygame.K_RETURN:
                Game.MODE = 'Wheel'
                self.startMusic = True


    def timerFired(self, dt):
        Game.TIMEKEEP += 1
        
        # music player
        if self.startMusic == True:
            self.sounds.startMusic(Game.MODE)
            self.startMusic = False
            #MUST RESET self.startMusic WHEN NEXT ROUND STARTS
            
        # allows letter by letter text crawl
        if Game.MODE == 'Intro':
            if Game.TIMEKEEP % 2 == 0:
                self.intro.crawlText(Game.TIMEKEEP)
            
        
    def redrawAll(self, screen):
        if Game.MODE == 'Title Screen':
            self.logo.drawLogos(screen)
            
        elif Game.MODE == 'Credits':
            self.logo.drawCredits(screen)
            
        elif Game.MODE == 'Intro':
            self.intro.drawText(screen)
            self.actionBox.draw(screen)



Game(1000, 800).run()