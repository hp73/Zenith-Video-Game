from .soundManager import SoundManager

class ScreenState(object):
   def __init__(self, state="mainMenu"):
      self._state = state
      self._paused = False
      SoundManager.getInstance().playMusic("Hawkin_-_01_-_Woods.mp3")
   
   def manageState(self, action, screenManager):
      if action == "pause" and self._state == "game":
         self._paused = not self._paused
         screenManager.transitionState(self._state)
      
      elif action == "mainMenu" and not self._paused and self._state != "mainMenu":
         self._state = "mainMenu"
         SoundManager.getInstance().playMusic("Hawkin_-_01_-_Woods.mp3")
         screenManager.transitionState(self._state)
      
      elif action == "startGame" and self._state != "game":
         self._state = "game"
         SoundManager.getInstance().playMusic("Four_Minutes_Of_Sadness_(Antti_Luode).mp3")
         screenManager.transitionState(self._state)
         
      elif action == "gameWin" and self._state != "gameWin":
         self._state = "gameWin"
         screenManager.transitionState(self._state)
      
      elif action in "cursor" and self._state != "mainMenu":
         self._state = "mainMenu"
         screenManager.setMainMenu(action)
         screenManager.transitionState(self._state)
      
      """
      elif action == "dialogue" and not self._paused and self._state == "game":
         self._state = "dialogueMenu"
         screenManager.transitionState(self._state)
      """
         
   
   def __eq__(self, other):
      return self._state == other

   def isPaused(self):
      return self._paused
   
   def menuType(self):
      return self._menuType
