'''
music by Griffin McElroy:
https://soundcloud.com/griffinmcelroy/
Pygame instructions:
https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound
'''

import pygame

class Music(object):
    def init():
        pygame.mixer.init()
        Music.titleScreen = pygame.mixer.Sound('TAZ Theme.wav')
        Music.intro = pygame.mixer.Sound('ArmsOutstretched.wav')
        Music.wheel = pygame.mixer.Sound('WonderlandRound1.wav')
        Music.trustForsake = pygame.mixer.Sound('WonderlandRound2.wav')
        Music.battle = pygame.mixer.Sound('WonderlandRound3.wav')
        Music.currSong = None
        Music.prevSong = None
        Music.fadeOut = 500
        Music.vol = 0.4

    def startMusic(self, mode):
        if mode == 'Title Screen':
            Music.prevSong = Music.titleScreen
            Music.currSong = Music.titleScreen
        elif mode == 'Intro':
            Music.prevSong = Music.currSong
            Music.currSong = Music.intro
        elif mode == 'Wheel':
            Music.prevSong = Music.currSong
            Music.currSong = Music.wheel
        elif mode == 'Trust/Forsake':
            Music.prevSong = Music.currSong
            Music.currSong = Music.trustForsake
        elif mode == 'Battle':
            Music.prevSong = Music.currSong
            Music.currSong = Music.battle
            
        Music.prevSong.fadeout(Music.fadeOut)
        Music.currSong.set_volume(Music.vol)
        Music.currSong.play(-1)
        
    def changeVol(change):
        if (Music.vol + change) >= 0 and (Music.vol + change) <= 1:
            Music.vol += change
        Music.currSong.set_volume(Music.vol)
