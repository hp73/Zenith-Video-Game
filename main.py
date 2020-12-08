
import pygame
import os
from modules.drawable import Drawable
from modules.textBox import *
from modules.screenInfo import *
from modules.screenManager import *

def main():
   
   # initialize the pygame module
   pygame.init() 
   # load and set the logo
   
   pygame.display.set_caption("Zenith")
   
   screen = pygame.display.set_mode(list(UPSCALED_SCREEN_SIZE))
   
   drawSurface = pygame.Surface(list(SCREEN_SIZE))
   
   screenManager = ScreenManager()
   

   # Make a game clock for nice, smooth animations
   gameClock = pygame.time.Clock()
   
   
   # define a variable to control the main loop
   running = True
   
   # main loop
   while running:
      
      # Draw everything
      
      screenManager.draw(drawSurface)
      pygame.transform.scale(drawSurface, list(UPSCALED_SCREEN_SIZE), screen)
      
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or e is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
            # change the value to False, to exit the main loop 
            running = False
            break
         
         result = screenManager.handleEvent(event)
         
         if result == "exit":
            running = False
            break     
      
      
      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      
      # Get some time in seconds
      ticks = gameClock.get_time() / 1000
      
      screenManager.update(ticks)
      
   
      
if __name__ == "__main__":
   main()