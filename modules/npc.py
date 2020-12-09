from .mobile import Mobile
from .FSM import MobileState
from.vector2D import Vector2

import pygame

class NPC(Mobile):
   def __init__(self, position):
      super().__init__("npc.png", position)
      
      self._nFrames = 1
      self._vSpeed = 50
      self._framesPerSecond = 2
      #self._collision = (14,4)
      self._collision = (self._position[0], self._position[1]) 
      
      self._nFramesList = {
         "moving" : 4,
         "standing" : 1
      }
      
      self._rowList = {
         "moving" : 1,
         "standing" : 0
      }
      
      self._framesPerSecondList = {
         "moving" : 8,
         "standing" : 1
      }
      
      self._state = MobileState()
      
      self.sight = 20
      self.differnce=Vector2(0,0)
      

   def update(self,ticks,worldSize,halcyon):
      
      super().update(ticks,worldSize)
      
      self._difference = halcyon.getPosition() - self.getPosition()
      if self._difference.magnitude()<self._sight:
         print(self._.difference)
         return True
      else:
         return False
      
   