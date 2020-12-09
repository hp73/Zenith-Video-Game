from .frameManager import FrameManager
from .drawable import Drawable

class CollideableObject(Animated):
   
   def __init__(self, imageName, location, nFrames, row, framesPerSecond):
      super().__init__(imageName, location)
      
      self._nFramesList = {
         
      }
      
      self._rowList = {
        
      }
      
      self._framesPerSecondList = {
         
      }
      
    def update(self, ticks, boundaries):
      
      super().update(ticks)   
  
   
   def transitionState(self, state):
      self._nFrames = self._nFramesList[state]
      self._frame = 0
      self._row = self._rowList[state]
      self._framesPerSecond = self._framesPerSecondList[state]
      self._animationTimer = 0
      self._image = FrameManager.getInstance().getFrame(self._imageName, (self._row, self._frame))
      
      