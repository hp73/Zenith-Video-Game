
class BasicState(object):
   def __init__(self, facing="none"):
      self._facing = facing
      
   def getFacing(self):
      return self._facing

   def _setFacing(self, direction):
      self._facing = direction
      
class MobileState(object):
   def __init__(self, state="standing"):
      self._state = state
      self.movement = {
         "up" : False,
         "down" : False,
         "left" : False,
         "right" : False,
      }
      
      self._lastFacing = "down"
      
   def getFacing(self):
      if self.movement["left"] == True:
         self._lastFacing = "left"
      if self.movement["up"] == True:
         self._lastFacing = "up"
      if self.movement["down"] == True:
         self._lastFacing = "down"
      elif self.movement["right"] == True:
         self._lastFacing = "right"
         
      
      return self._lastFacing

   def manageState(self, action, obj):
      if action in self.movement.keys():
         if self.movement[action] == False:
            self.movement[action] = True
            if self._state == "standing":
               self._state = "moving"
               obj.transitionState(self._state)
         
      elif action.startswith("stop") and action[4:] in self.movement.keys():
         direction = action[4:]
         if self.movement[direction] == True:            
            self.movement[direction] = False
            allStop = True
            for move in self.movement.keys():
               if self.movement[move] == True:
                  allStop = False
                  break
               
            if allStop:
               self._state = "standing"
               obj.transitionState(self._state)
      elif action == "stopall":
         if self._state != "standing":
            for direction in self.movement.keys():
               self.movement[direction] = False
               
            self._state = "standing"
            obj.transitionState(self._state)
      
      
            
   def getState(self):
      return self._state
      
   
