import pygame
from pygame import image
import os
from .frameManager import FrameManager
from .drawable import Drawable

class Animated(Drawable):
   
   def __init__(self, imageName, location):
      super().__init__(imageName, location, (0,0))
      
      self._frame = 0
      self._row = 0
      self._animationTimer = 0
      self._framesPerSecond = 10.0
      self._nFrames = 2
      
      self._animate = True
      

      
   def update(self, ticks):
      if self._animate:
         self._animationTimer += ticks
         
         if self._animationTimer > 1 / self._framesPerSecond:
            self._frame += 1
            self._frame %= self._nFrames
            self._animationTimer -= 1 / self._framesPerSecond
            self._image = FrameManager.getInstance().getFrame(self._imageName, (self._row, self._frame))
   
   def transitionState(self, state):
      self._nFrames = self._nFramesList[state]
      self._frame = 0
      self._row = self._rowList[state]
      self._framesPerSecond = self._framesPerSecondList[state]
      self._animationTimer = 0
      self._image = FrameManager.getInstance().getFrame(self._imageName, (self._row, self._frame))
         