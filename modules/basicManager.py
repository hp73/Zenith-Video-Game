

class BasicManager(object):

   def draw(self, drawSurface):
      raise NotImplementedError("Draw not implemented.")
   
   def update(self, ticks):
      raise NotImplementedError("Update not implemented.")
   
   def handleEvent(self, event):
      raise NotImplementedError("Handle event not implemented.")