'''
text formatting help: http://pygame-zero.readthedocs.io/en/stable/ptext.html
'''

import pygame

class SplashScreen(object):
    def init():
        # initialize images
        TAZlogo = pygame.image.load('TAZ LOGO.png').convert_alpha()
        SplashScreen.TAZlogoSize = TAZlogo.get_rect()
        SplashScreen.TAZlogoSize[2] *= .75 
        SplashScreen.TAZlogoSize[3] *= .75
        SplashScreen.TAZlogo = pygame.transform.scale(TAZlogo, \
            (SplashScreen.TAZlogoSize[2], SplashScreen.TAZlogoSize[3]))
        
        wonderLogo = pygame.image.load('LOGO.png').convert_alpha()
        SplashScreen.wonderLogoSize = wonderLogo.get_rect()
        SplashScreen.wonderLogo = pygame.transform.scale(wonderLogo,\
            (SplashScreen.wonderLogoSize[2], SplashScreen.wonderLogoSize[3]))
        
        credits = pygame.image.load('CREDITS.png').convert_alpha()
        SplashScreen.creditsSize = credits.get_rect()
        SplashScreen.credits = pygame.transform.scale(credits, \
            (SplashScreen.creditsSize[2], SplashScreen.creditsSize[3]))
        
    def __init__(self, screenWidth, screenHeight):
        # initialize image positions
        self.radius = 10
        self.w, self.h = screenWidth, screenHeight
        self.wonderLogoPos = ((self.w//2)-(SplashScreen.wonderLogoSize[2]/2),\
                              (2*self.h//3)-SplashScreen.wonderLogoSize[3])
                              
        self.TAZlogoPos = ((self.w//2)-(SplashScreen.TAZlogoSize[2]/2),\
                           (self.h//3.5)-(SplashScreen.TAZlogoSize[3]/2))

        self.creditsPos = ((self.w//2)-(SplashScreen.creditsSize[2]/2),\
                           (2*self.h//5)-(SplashScreen.creditsSize[3]/2))

    def drawLogos(self, screen):
        # draw title screen logos
        screen.blit(SplashScreen.wonderLogo, self.wonderLogoPos)
        screen.blit(SplashScreen.TAZlogo, self.TAZlogoPos)
        
        font = pygame.font.SysFont('SignPainter', 25)
        instruct = font.render('Press "Enter" to Begin', True,(255, 255, 255))
        creditCall = font.render('Press "Space" to View Credits', \
                     True,(255, 255, 255))
        instructSize = instruct.get_rect()
        creditCallSize = creditCall.get_rect()
        
        beginPos = ((self.w//2)-(instructSize.width//2), 3*self.h//4)
        screen.blit(instruct, beginPos)
        
        screen.blit(creditCall, ((self.w//2)-(creditCallSize.width//2),\
                    3*self.h//4+instructSize.height))
        
        pygame.display.update()
        
    def drawCredits(self, screen):
        # draw credits page
        screen.blit(SplashScreen.credits, self.creditsPos)
        
        font = pygame.font.SysFont('SignPainter', 25)
        instruct = font.render('Press "Esc" to Return to Main Menu',\
                                True,(255, 255, 255))
        instructSize = instruct.get_rect()
        screen.blit(instruct, (self.w//2 - instructSize.width//2,\
                    self.h-(instructSize.height*4)))
        
        pygame.display.update()