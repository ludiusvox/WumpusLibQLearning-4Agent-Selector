import WumpusLib
import sys
import os




class ChoiceManager:
    
    def __init__(self):
        
        self.__choice_table = \
        {
            "REFLEX" : self.Reflex,
            "MODEL" : self.Model,
            "GOAL" : self.Goal,
            "UTILITY" : self.Utility
        }
       
    def Reflex(self,data):
        
        
        print("WUMPUS REFLEX AGENT!")
        while True:
            WG = WumpusLib.WumpusGame(PrintMessages=True)
            WG.printBoard() 
            Reflex = WumpusLib.SimpleReflex(WG) 
            Reflex.play_game()
            pass 

    def Model(self, data):
        print("Attempted to make a smarter model based on 1 grid sense")    
        WG = WumpusLib.WumpusGame(PrintMessages=True)
        WG.printBoard() 
        Model = WumpusLib.SimpleModel(WG) 
        Model.play_game() 
        pass
       
        
    def Goal(self,data):
        print("This algorithm will learn to path the obstical course and get the gold but it's not automated")
        WG = WumpusLib.WumpusGame(PrintMessages=True)
        WG.printBoard() 
       
        print("run qlearning.py from spyder manually input data in cartesian coordinates")  
        os.system('./test.sh')
        pass
    
    def Utility(self,data):
        WG = WumpusLib.WumpusGame(PrintMessages=True)
        WG.printBoard() 
        print("INSTRUCTIONS, map is printed, use the map x,y coordinates to tell numpy a path for q learning")
        print(" qlearning.py from spyder manually input data type and the script will run")
        print("Machine runs 500 interations")
        print("I couldn't figure out how to script translate the map! Sorry!")
        
        os.system('./test.sh')
        
        
        
        
        
        
        
        
        pass

    
    
    def process(self, case, data):
        return self.__choice_table[case](data)



# Function to convert number into string
# Switcher is dictionary data type here


if __name__ == "__main__":
    print("WUMPUS BOARD GAME!")
    
    data= []
    arguement1=0  
    print("What is your choice of programs? ")
    print("'REFLEX': Simple Reflex Agent")
    print("'MODEL': Model Based Agent")
    print("'GOAL': Goal Based Agent")
    print("'UTILITY': Utility Based Agent")
    string= input()
    ChoiceManager().process(string, data)    





    
    
       
            
      
    



    

    
