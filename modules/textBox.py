
# from .cursor import *
from .drawable import Drawable
from .vector2D import Vector2
from .screenInfo import *
import pygame
import os

class TextManager(object):
   """A singleton factory class to create and store text boxes."""
   
   # The singleton instance variable
   _INSTANCE = None
   
   @classmethod
   def getInstance(cls):
      """Used to obtain the singleton instance"""
      if cls._INSTANCE == None:
         cls._INSTANCE = cls._TM()
      
      return cls._INSTANCE
   
   # Do not directly instantiate this class!
   class _TM(object):
      """An internal TextManager class to contain the actual code. Is a private class."""
      
      _TEXT_SOURCE = os.path.join("resources", "newdialog.csv")
      
      
      
      
      def __init__(self):
         
         self._boxes = {}
         sourceFile = open(TextManager._TM._TEXT_SOURCE)
         
         textSplit = [[y for y in x.split(";")] for x in sourceFile.read().split("\n")]
         
         idIndex = textSplit[0].index("id")
         textIndex = textSplit[0].index("fulltext")
         nextIndex = textSplit[0].index("next")
         for line in textSplit:
            self._boxes[line[idIndex]] = {
               "box" : TextManager._TextBox(line[textIndex]),
               "next" : line[nextIndex]
               }
         
         
         sourceFile.close()
         
         self._activeBox = None
      
      
      def __getitem__(self, key):
         return self._boxes[key]
   
      def __setitem__(self, key, item):
         self._boxes[key] = item
      
      def showBox(self, textid):
         
         self._activeBox = self[textid]
         self._activeBox["box"].reset()
   
      
      
      def draw(self, surface):
         if self._activeBox:
            self._activeBox["box"].draw(surface)
      
      def _nextPageEvent(self, event):
         return event.type == pygame.KEYDOWN and event.key == pygame.K_z
               
      
      def handleEvent(self, event):
         if self._activeBox and self._nextPageEvent(event):
            
            if self._activeBox["box"].isDone() and self._activeBox["next"] != "":
               self.showBox(self._activeBox["next"])
               
            elif self._activeBox["box"].isDone():
               self._activeBox = None
               
            else:
               self._activeBox["box"]._renderText()
            
           
   
   class _TextBox(Drawable):
      
      _TEXT_POSITION = Vector2(SCREEN_SIZE.x //4  , SCREEN_SIZE.y - 60)
      
      def __init__(self, text):
         super().__init__("", TextManager._TextBox._TEXT_POSITION)
         
         self._hPad = 4
         self._vPad = 4
         
         if not pygame.font.get_init():
            pygame.font.init()
            
         self._fontColor = pygame.Color("BLACK")
         self._fontSize = 8
         self._font = pygame.font.Font(os.path.join("resources", "fonts", "PressStart2P.ttf"), self._fontSize)
         self._maxRows = 4
         self._maxCols = 25
         self._image = pygame.Surface((self._maxCols * self._fontSize,
                                       self._maxRows * (self._fontSize + self._vPad)),
                                      pygame.SRCALPHA, 32)
         
         
         self._fullText = text.replace("\\n", "\n")
         self._curr = 0
         
         
      
         
      def _renderText(self):
         self._image.fill((0,0,0,0))
         currCol = 0
         currRow = 0
         
         for currRow in range(self._maxRows):
            
            start = self._curr
            end = start + self._maxCols
            
            
            substring = self._fullText[start:end]
            
            
            
            newlineIndex = substring.rfind("\n")
            
            if newlineIndex != -1:
               end = newlineIndex + start
               
            elif end < len(self._fullText):
               spaceIndex = substring.rfind(" ")
               
               if spaceIndex != -1:
                  end = spaceIndex + start
               
            
            
            self._image.blit(self._font.render(self._fullText[start:end], False, self._fontColor), (0, currRow * (self._fontSize + self._vPad)))
            
            self._curr = end + 1
            
      def reset(self):
         self._curr = 0
         self._renderText()
      
      def isDone(self):
         return self._curr >= len(self._fullText)
      
      def draw(self, surface):
         #draw box
         
         textbox = Drawable("textbox.png", Vector2(SCREEN_SIZE.x //4 -20  , SCREEN_SIZE.y - 75))
         textbox.draw(surface)
         """
         pygame.draw.rect(surface, (0,0,0),
                          pygame.Rect(list(self._position - Vector2(10,10)),
                                      list(Vector2(*self.getSize()) + Vector2(20,20))))
         """
         super().draw(surface)
         
      
      
   