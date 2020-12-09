from .basicManager import BasicManager
from .gameManager import GameManager, GameManagerThreaded
from .levelFSM import LevelState, LevelStateThreaded
from .displays import AbstractMenu
from .screenInfo import SCREEN_SIZE

class LevelManager(BasicManager):
   
   def __init__(self, screenSize):
      self._state = LevelState()
      
      self._currentLevel = 0
      self._maxLevel = 3
      
      
      self._level = [GameManager(screenSize,
                                 "jsonLevel" + str(x) + ".txt") for x in range(self._maxLevel)]
      
      self._level[self._currentLevel].load()
      
   def restart(self):
      self._state.manageState("restart", self)
      
   def draw(self, surface):
      self._level[self._currentLevel].draw(surface)
      
   
   def handleEvent(self, event):
      if self._state == "running":
      
         self._level[self._currentLevel].handleEvent(event)
         
         
   def updateMovement(self):
      self._level[self._currentLevel].updateMovement()
         
   
   def update(self, ticks, screenSize):
      if self._state == "running":
         levelStatus = self._level[self._currentLevel].update(ticks, screenSize)
         
         if levelStatus == "nextLevel":
            if self._currentLevel == self._maxLevel - 1:
               return "gameWin"
            
            self._state.manageState("nextLevel", self)
         else:
            return levelStatus
            
   
   def transitionState(self, state):
      if state == "nextLevel":
         self._currentLevel += 1
         
         
         self._level[self._currentLevel].load()
         self._state.manageState("doneLoading", self)
         
         print("Level", self._currentLevel)
      
      elif state == "restart":
         self._level[self._currentLevel].load()
         print("Level", self._currentLevel)
         
         self._state.manageState("doneLoading", self)


class LevelManagerThreaded(LevelManager):
   
   def __init__(self, screenSize):
      
      super().__init__(screenSize)
      
      self._loadingScreen = AbstractMenu("background.png", fontName="default8")
      self._loadingScreen.addText("Loading",
                               SCREEN_SIZE // 2,
                               center="both")
                               
      self._level = [GameManagerThreaded(screenSize,
                                 "jsonLevel" + str(x) + ".txt") for x in range(self._maxLevel)]
      self._state = LevelStateThreaded("startLoading")
      
   
   def draw(self, surface):
      
      if self._state == "running":
         super().draw(surface)
      else:
         self._loadingScreen.draw(surface)
         
   
   def update(self, ticks, screenSize):
      if self._state == "startLoading":
         self._level[self._currentLevel].load()
         print("Level", self._currentLevel)
         self._state.manageState("load", self)
      
      elif self._state == "reload":
         self._level[self._currentLevel].load()
         print("Level", self._currentLevel)
         self._state.manageState("load", self)
      
      elif self._state == "loading" and self._level[self._currentLevel].isLoaded():
         self._state.manageState("doneLoading", self)
         
         print("Level", self._currentLevel, "done")
         
      else:
         return super().update(ticks, screenSize)
   
   
   
   def transitionState(self, state):
      if state == "restart":
         self._level[self._currentLevel].load()
         print("Level", self._currentLevel)
         
         self._state.manageState("load", self)
      
      elif state == "nextLevel":
         self._currentLevel += 1
         self._level[self._currentLevel].load()
         print("Level", self._currentLevel)
         
         self._state.manageState("load", self)
         
      
      else:
         super().transitionState(state)
       