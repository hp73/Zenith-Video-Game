from .animated import Animated
from .FSM import MobileState
from.vector2D import Vector2


import pygame

class Fountain(Animated):
   def __init__(self, position):
      super().__init__("fountain.png", position)
      
      self._nFrames = 1
      self._framesPerSecond = 2
      self._animate = True
      
      self._nFramesList = {
         "standing" : 3
      }
      
      self._rowList = {
         "standing" : 0
      }
      
      self._framesPerSecondList = {
         "standing" : 6
      }
      
      self._state = MobileState()
      
   
      
      
      
      
   