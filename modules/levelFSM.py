""" 
File: levelFSM.py
Author: Dr. Elizabeth Matthews
Version: 1.0
Date: 11/11/20
FrameStateManager with for level generation
"""

class LevelState(object):
   """Level FSMs"""

   def __init__(self, state="running"):
      """Instantiates level with state regarding generation/loading"""
      self._state = state
   
   def manageState(self, action, levelManager):
      """Method to manage how level is generated in response to certain events.
      Checks if action requires generation of the next level, is finished loading, or requires
      a restart."""
      if action == "nextLevel" and self._state == "running":
         self._state = "startLoading"
         levelManager.transitionState("nextLevel")
            
      elif action == "doneLoading" and self._state == "startLoading":
         self._state = "running"
      
      elif action == "restart" and self._state == "running":
         self._state = "startLoading"
         levelManager.transitionState("restart")
   
   def __eq__(self, other):
      """Equality method to check if current state is equal to input"""
      return self._state == other

class LevelStateThreaded(LevelState):
   """Threaded Level FSMs"""

   def manageState(self, action, levelManager):
      """Method to manage how level is generated in response to certain events.
      Checks if action needs to start or finish loading."""

      if action == "load" and self._state == "startLoading":
         self._state = "loading"
      elif action == "doneLoading" and self._state == "loading":
         self._state = "running"
      else:
         super().manageState(action, levelManager)
