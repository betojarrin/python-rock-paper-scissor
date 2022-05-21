class Player:
    
    def __init__(self,name):
        self.__name = name

    @property
    def player_name(self):
        return self.__name

    @player_name.setter
    def player_name(self,new_name):
        self.__name = new_name
        


    