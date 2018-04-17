'''
file writing assistance: http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
'''

import pygame

class Intro(object):
    def init():
        Intro.introCrawl = open('RedRobeScript.txt')
        
    def __init__(self):
        self.pause = False
        self.pauseTime = 151
        self.currPrint = ''
        self.currPrint2 = ''
        self.secondLine = False
        self.currChar = ''
        self.speaker = 'Red Robe'
        self.nameFont = pygame.font.SysFont('SignPainter', 35)
        self.dialogueFont = pygame.font.SysFont('Courier New', 25)
        self.nameColor = (255, 46, 95)
        self.dialogueColor = (84, 84, 84)
        self.xBuffer = 50
        self.yBuffer = 600
        
    def crawlText(self, timeKeep):
        # updates text on screen in intro
        if not self.pause:
            self.currChar = Intro.introCrawl.readline(1)
            
            # pause between lines  
            if self.currChar == '/':
                self.pause = True
            
            # new line but not new box
            elif self.currChar == '|' :
                self.secondLine = True
            elif self.secondLine: 
                self.currPrint2 += self.currChar
                
            # add letter 
            else:
                self.currPrint += self.currChar
                
        elif timeKeep % self.pauseTime == 0:
            self.pause = False
            self.secondLine = False
            self.currPrint = ''
            self.currPrint2 = ''
                    
    def drawText(self, screen):
        # draws character name and current text on screen
        name = self.nameFont.render(self.speaker, True,self.nameColor)
        namePos = (self.xBuffer, self.yBuffer)
        screen.blit(name, namePos)
        
        dialogue = self.dialogueFont.render(self.currPrint, True,\
                                            self.dialogueColor)
        dialoguePos = (self.xBuffer, self.yBuffer+self.xBuffer)
        screen.blit(dialogue, dialoguePos)
        
        dialogue2 = self.dialogueFont.render(self.currPrint2, True,\
                                            self.dialogueColor)
        dialogueSize = dialogue.get_rect()
        dialogue2Pos = (self.xBuffer, self.yBuffer + self.xBuffer +\
                        dialogueSize.height)
        screen.blit(dialogue2, dialogue2Pos)
        
        pygame.display.update()

