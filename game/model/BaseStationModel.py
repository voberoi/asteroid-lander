'''
Created on 16/02/2013

@author: Christian Adriano
'''
from Constants import *
from game.Constants import *
class BaseStationModel(object):
    '''
    This class holds the data shared between the client (Spaceship) and the GameServer.
    This class is used solely by the Spaceship.
    '''
    

    def __init__(self, selfparams):
        '''
        Constructor
        '''
        self.fuel = MAX_FUEL_BASE_STATION
        self.gameScore = {GOLD:0,
                          COPPER:0,
                          IRON:0}
        self.mineGrid = {GOLD:GOLD_PLOT_TOTAL,
                          COPPER:COPPER_PLOT_TOTAL,
                          IRON:IRON_PLOT_TOTAL}
        self.conquredPlot = {GOLD:0,
                          COPPER:0,
                          IRON:0}
        
    def setgameScore(self, i,value):
        self.gameScore[i] = value
    
    def setMineGrid(self, i,value):
        self.mineGrid[i] = value
        
    def setfuel(self, value):
        self.fuel= value
