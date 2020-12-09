
from .basicManager import BasicManager
from .halcyon import Halcyon
from .drawable import Drawable
from .backgrounds import *
from .vector2D import Vector2
from .npc import NPC
from .screenInfo import adjustMousePos
from .soundManager import SoundManager
from .fountain import Fountain
from .door import Door
from .textBox import *
import pygame
import os
import json
import time, threading

class GameManager(BasicManager):
   
   def __init__(self, screenSize, loadFile):
      """
      self._fountain = Fountain(Vector2(350, 48))
   
      """
      self._loadFile = loadFile
      self._screenSize = screenSize
   
      self._NPCList = []
      self._NPCNum = 0
      self._doorList = []
      self._doorNum = 0
      self._houseList = []
      self._houseNum = 0
      self._houseBackList = []
      self._houseBackNum = 0
      self._brushList = []
      self._brushNum = 0
      self._TEXTS = TextManager.getInstance()
      
      
      
      
   def load(self):
      filePtr=open(os.path.join("resources","levels",self._loadFile))
      info=json.load(filePtr)
      filePtr.close()
      self._worldSize=Vector2(*info["worldSize"])

        
   
      self._backgroundName=info["background"]
      if self._backgroundName == "1":
         self._background = EfficientBackground(self._worldSize, "grass.png")
      if self._backgroundName == "2":
         self._background = EfficientBackground(self._worldSize, "floorInside.png")
      if self._backgroundName == "3":
         self._background = Drawable("background.png", Vector2(0,0))
         
         
      self._halcyon = Halcyon(Vector2(*info["starthalcyon"]))
      self._door = Door(info["door"])
        
      """
      doorLocations = info["door"]
      if len(doorLocations) !=0:
         self._doorNum = len(doorLocations)
            
         for i in range(self._doorNum):
            self._doorList.append(Door(Vector2(*info["door"])))
      """
        
      NPCLocations = info["NPC"]
      if len(NPCLocations) != 0:
         self._NPCNum = len(NPCLocations)//2

         for i in range (self._NPCNum):
            self._NPCList.append(NPC(Vector2(NPCLocations[i*2],NPCLocations[i*2+1])))
        
        
      houseLocations = info["house"]
      if len(houseLocations) != 0:
         self._houseNum = len(houseLocations)//2

         for i in range (self._houseNum):
            self._houseList.append(Drawable("House1.png", Vector2(houseLocations[i*2],houseLocations[i*2+1])))
      
      houseBackLocations = info["houseBack"]
      if len(houseBackLocations) != 0:
         self._houseBackNum = len(houseBackLocations)//2

         for i in range (self._houseBackNum):
            self._houseList.append(Drawable("House1Back.png", Vector2(houseBackLocations[i*2],houseBackLocations[i*2+1])))
            
            
      brushLocations = info["brush"]
      if len(brushLocations) != 0:
         self._brushNum = len(brushLocations)//2

         for i in range (self._brushNum):
            self._houseList.append(Drawable("brush.png", Vector2(brushLocations[i*2],brushLocations[i*2+1])))
            
      talkLocations = info["NPC"]
      
   def draw(self, drawSurface):
      
      drawSurface.fill((255,0,255))
      self._background.draw(drawSurface)
      
      # Draw everything
      """
      self._fountain.draw(drawSurface)
      """
      
      
      self._halcyon.draw(drawSurface)
      self._door.draw(drawSurface)
      for house in self._houseList:
         house.draw(drawSurface)
      """
      for door in self._doorList:
         door.draw(drawSurface)
      """
      for npc in self._NPCList:
         npc.draw(drawSurface)
         
      for houseback in self._houseBackList:
         houseback.draw(drawSurface)
         
      for brush in self._brushList:
         brush.draw(drawSurface)
         
      self._TEXTS.draw(drawSurface)
      
      
   def handleEvent(self, event):
      self._halcyon.handleEvent(event)
      if event.type == pygame.KEYDOWN and event.key in [pygame.K_0, pygame.K_1,pygame.K_2, pygame.K_3,pygame.K_6, pygame.K_7]:
         self._TEXTS.showBox(pygame.key.name(event.key))
      else:            
         self._TEXTS.handleEvent(event)
      
        

   def update(self, ticks, screenSize):
      # let others update based on the amount of time elapsed
      
      status = self._halcyon.update(ticks, self._worldSize)
      if status:
         return status
   
      if self._halcyon.getCollisionRect().colliderect(self._door.getCollisionRect()):
         return "nextLevel"
            
      
      """
      self._npc1.update(ticks, GameManager.WORLD_SIZE,self._halcyon)
      self._npc2.update(ticks, GameManager.WORLD_SIZE,self._halcyon)
      self._npc3.update(ticks, GameManager.WORLD_SIZE,self._halcyon)
      self._npc4.update(ticks, GameManager.WORLD_SIZE,self._halcyon)
      self._npc5.update(ticks, GameManager.WORLD_SIZE,self._halcyon)
      self._fountain.update(ticks)
      """
      Drawable.updateWindowOffset(self._halcyon, screenSize, self._worldSize)
   
      
   def updateMovement(self):
      self._halcyon.updateMovement()
   
   """
   def canTalk1(self):
      if self._npc1.difference.magnitude()<self._npc1.sight:
         print(self._npc1.difference)
         return True
      else:
         return False
      
   def canTalk2(self):
      if self._npc2.difference.magnitude()<self._npc2.sight:
         print(self._npc2.difference)
         return True
      else:
         return False
      
   def canTalk3(self):
      if self._npc3.difference.magnitude()<self._npc3.sight:
         print(self._npc3.difference)
         return True
      else:
         return False
      
   def canTalk4(self):
      if self._npc4.difference.magnitude()<self._npc4.sight:
         print(self._npc4.difference)
         return True
      else:
         return False
      
   def canTalk5(self):
      if self._npc5.difference.magnitude()<self._npc5.sight:
         print(self._npc5.difference)
         return True
      else:
         return False
   """   
class GameManagerThreaded(GameManager):
   
   def __init__(self, screenSize, loadFile):
      super().__init__(screenSize, loadFile)
      
      self._loaded = False
      
   
   def load(self):
      self._loaded = False
      self._loadingThread = threading.Thread(target=self._loadAssets)
      self._loadingThread.start()
      
      
   def _loadAssets(self):
      super().load()
      time.sleep(1) # Artificially inflate loading time
      self._loaded = True
   
   def isLoaded(self):
      return self._loaded

   def updateMovement(self):
      if self.isLoaded():
         super().updateMovement()
         