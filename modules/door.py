from .drawable import Drawable


class Door(Drawable):
   
   def __init__(self, position):
      super().__init__("door2.png", position)