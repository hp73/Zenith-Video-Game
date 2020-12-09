from .mobile import Mobile
from .FSM import MobileState
from .frameManager import FrameManager

import pygame

class Halcyon(Mobile):
   def __init__(self, position):
      super().__init__("halcyon.png", position)
      
      self._nFrames = 1
      self._vSpeed = 50
      self._framesPerSecond = 2
      #self._collision = (16,4)
      self._collision = (self._position[0], self._position[1]) 
      
      self._nFramesList = {
         "moving" : 4,
         "movingup" : 4,
         "movingdown" : 4,
         "movingleft" : 4,
         "movingright" : 4,
         "standing" : 1

      }
      
      self._rowList = {
         "moving" : 1,
         "movingup" : 2,
         "movingdown" : 0,
         "movingleft" : 3,
         "movingright" : 1,
         "standing" : 0

      }
      
      self._framesPerSecondList = {
         "moving" : 8,
         "movingup" : 8,
         "movingdown" : 8,
         "movingleft" : 8,
         "movingright" : 8,
         "standing" : 1

      }
      
      self._state = MobileState()
      
      
   def handleEvent(self, event):
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
            self._state.manageState("down", self)
            
         elif event.key == pygame.K_UP:
            self._state.manageState("up", self)
            
         elif event.key == pygame.K_LEFT:
            self._state.manageState("left", self)
            
         elif event.key == pygame.K_RIGHT:
            self._state.manageState("right", self)
         
         
         elif event.key == pygame.K_x:
            self._vSpeed = self._vSpeed *2
            self._framesPerSecond = self._framesPerSecond *2
            
            
      
      elif event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN:
            self._state.manageState("stopdown", self)
            
         elif event.key == pygame.K_UP:
            self._state.manageState("stopup", self)
            
         elif event.key == pygame.K_LEFT:
            self._state.manageState("stopleft", self)
            
         elif event.key == pygame.K_RIGHT:
            self._state.manageState("stopright", self)
            
            
         elif event.key == pygame.K_x:
            self._vSpeed = self._vSpeed /2
            self._framesPerSecond = self._framesPerSecond /2 
            
   def updateMovement(self):
      pressed = pygame.key.get_pressed()
     
      if not pressed[pygame.K_LEFT]:
         self._state.manageState("stopleft", self)
      if not pressed[pygame.K_RIGHT]:
         self._state.manageState("stopright", self)
      if not pressed[pygame.K_UP]:
         self._state.manageState("stopup", self)
      if not pressed[pygame.K_DOWN]:
         self._state.manageState("stopdown", self)
         
      
   