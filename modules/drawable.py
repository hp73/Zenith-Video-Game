import pygame
from .vector2D import Vector2
from .frameManager import FrameManager
from .FSM import BasicState

class Drawable(object):
   
   WINDOW_OFFSET = Vector2(0,0)
   
   @classmethod
   def updateWindowOffset(cls, tracked, screenSize, worldSize):
      position = tracked.getPosition()
      size = tracked.getSize()
      width = size[0]
      height = size[1]
      cls.WINDOW_OFFSET = Vector2(min(max(0, position[0] + (width // 2) - (screenSize[0] // 2)),
                           worldSize[0] - screenSize[0]),
                       min(max(0, position[1] + (height // 2) - (screenSize[1] // 2)),
                           worldSize[1] - screenSize[1]))
      
   
   def __init__(self, imageName, position, WINDOW_OFFSET=None, parallax=1):
      self._imageName = imageName

      # Let frame manager handle loading the image
      if self._imageName != "":
         self._image = FrameManager.getInstance().getFrame(self._imageName, WINDOW_OFFSET)

      self._position = Vector2(*position)
      self._state = BasicState()
      self._parallax = parallax
      
   def getPosition(self):
      return self._position

   def setPosition(self, newPosition):
      self._position = newPosition
      
   def getSize(self):
      return self._image.get_size()

   def getCollisionRect(self):
      newRect =  self._position + self._image.get_rect()
      return newRect
   
   def draw(self, surface):
      blitImage = self._image
      
      if self._state.getFacing() == "left":
         blitImage = pygame.transform.flip(self._image, True, False)
      
      
      surface.blit(blitImage, list(self._position - Drawable.WINDOW_OFFSET * self._parallax))
     