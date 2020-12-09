from .vector2D import Vector2


SCREEN_SIZE = Vector2(400, 256)
SCALE = 2
UPSCALED_SCREEN_SIZE = SCREEN_SIZE * SCALE

def adjustMousePos(mousePos):
   return Vector2(*mousePos) // SCALE