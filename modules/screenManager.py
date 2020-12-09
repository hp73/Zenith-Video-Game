from .basicManager import BasicManager
from .gameManager import GameManager
from .levelManager import LevelManager,LevelManagerThreaded
from .screenFSM import ScreenState
from .items import Text
from .displays import *
from .vector2D import Vector2
from .screenInfo import SCREEN_SIZE
import pygame
from .textBox import *
from .soundManager import SoundManager



class ScreenManager(BasicManager):
      
   def __init__(self):
      super().__init__()
      self._game = LevelManagerThreaded(SCREEN_SIZE)
      self._state = ScreenState()
      self._pausedText = Text(Vector2(0,0),"Paused")
      #self._TEXTS = TextManager.getInstance()
      self._startText = Text(Vector2(0,0), "Zenith", font="default24", color=(47,79,79))
      
      size = self._pausedText.getSize()
      midPointX1 = SCREEN_SIZE.x // 2 - size[0] // 2
      midPointY1 = SCREEN_SIZE.y // 2 - size[1] // 2
      
      size = self._startText.getSize()
      midPointX2 = SCREEN_SIZE.x // 2 - size[0] // 2
   
      
      self._startText.setPosition(Vector2(midPointX2,40))
      self._pausedText.setPosition(Vector2(midPointX1, midPointY1))
   
   
      self._cursorMenu = CursorMenu("background 2.png", fontName = "default8")
      self._cursorMenu.addOption("start", "New Game",
                                 SCREEN_SIZE // 2 - Vector2(0,25),
                                 center="both")
      self._cursorMenu.addOption("exit", "Exit Game",
                                 SCREEN_SIZE // 2 + Vector2(0,25),
                                 center="both")
      
      self._cursorMenu.setCursor("start")
   
      
      self._mainMenu = self._cursorMenu
      
      
      
   def draw(self, drawSurface):
      if self._state == "game":
         self._game.draw(drawSurface)
         #self._TEXTS.draw(drawSurface)
      
         if self._state.isPaused():
            self._pausedText.draw(drawSurface)
         
      
      elif self._state == "mainMenu":
         self._mainMenu.draw(drawSurface)
         self._startText.draw(drawSurface)
        
        
         
   def handleEvent(self, event):
      # Handle screen-changing events first
      if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
         self._state.manageState("pause", self)
      
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
         self._state.manageState("mainMenu", self)
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
         SoundManager.getInstance().stopMusic()
      
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
         self._game.restart()
          
      else:
         
         #self._TEXTS.handleEvent(event)
         if self._state == "game" and not self._state.isPaused():
            self._game.handleEvent(event)
                
         elif self._state == "mainMenu":
            choice = self._mainMenu.handleEvent(event)
            
            if choice == "start":
               self._state.manageState("startGame", self)
            elif choice == "exit":
               return "exit"
   
   
   def update(self, ticks):      
      if self._state == "game" and not self._state.isPaused():
         status = self._game.update(ticks, SCREEN_SIZE)
         #self._game.update(ticks, SCREEN_SIZE)
      elif self._state == "mainMenu":
         self._mainMenu.update(ticks)
   
   
   # Prevents halcyon from constantly walking if the direction arrow
   #  is released when the game isn't playing
   def transitionState(self, state):
      if state == "game":
         self._game.updateMovement()