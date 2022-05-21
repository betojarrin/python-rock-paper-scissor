import os
from random import randint

from player import Player


class Game:

    

    def __init__(self):
        self.__options = ["Rock","Paper","Scissor"]
        self.__machine = "Rock Lee"
        self.__human_point = 0
        self.__machine_point = 0
        self.__score_game=''
        self.__summary_game=[]


    def selection_machine(self):
        return randint(0,2)

    def play_game(self,player:str):
        print(50*"*")
        print(f'Enfrentamiento entre {player} y {self.__machine}.... Que gane el mejor')
        print(50*"*")

        print("Que comience el juego")
        round = 1
        while round<4:
            
            option_machine = self.__options[self.selection_machine()]
            print(50*"*")
            
            print(50*"*")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissor")
            print(50*"*")
            
            try:
                selection_human = int(input("Selecciona una opción: "))
                if selection_human <= 0:
                    print("Por favor seleccione un valor entre 1 y 3. Valores como cero o números negativos no son permitidos")
                else:    
                    option_human = self.__options[selection_human-1]
                    movement = {player:option_human,self.__machine:option_machine}

                    print(50*"*")
                    print(f'{self.__machine} seleccionó {option_machine}')
                    print(50*"*")
                    print(50*"*")
                    print(f'{player} seleccionó {option_human}')
                    print(50*"*")
                    os.system('clear')

                    self.score(movement,player,self.__machine)
                    print(f'Ronda #{round} - Marcador: {self.__score_game}')
                    round+=1


            except ValueError:
                print("Opción seleccionada no es correcta. No se permiten valores alfabéticos ni valores vacíos")
            
            except IndexError:
                print("Opción no válida, por favor seleccione un valor entre 1 y 3")

        self.show_summary_game(player)



    def score(self,dic_options, human_player,machine_player):

        switcher = {
            1: [{human_player:"Rock",machine_player:"Scissor"},{"Resultado":human_player +" gana","Mensaje":"Roca vence a Tijera"}],
            2: [{human_player:"Rock",machine_player:"Paper"},{"Resultado":machine_player +" gana","Mensaje":"Roca pierde con Papel"}],
            3: [{human_player:"Rock",machine_player:"Rock"},{"Resultado":"Empate","Mensaje":"Roca vs Roca"}],
            4: [{human_player:"Scissor",machine_player:"Scissor"},{"Resultado":"Empate","Mensaje":"Tijera vs Tijera"}],
            5: [{human_player:"Scissor",machine_player:"Paper"},{"Resultado":human_player +" gana","Mensaje":"Tijera vence a Papel"}],
            6: [{human_player:"Scissor",machine_player:"Rock"},{"Resultado":machine_player +" gana","Mensaje":"Tijera pierde con Roca"}],
            7: [{human_player:"Paper",machine_player:"Scissor"},{"Resultado":machine_player +" gana","Mensaje":"Papel pierde con Tijera"}],
            8: [{human_player:"Paper",machine_player:"Paper"},{"Resultado":"Empate","Mensaje":"Papel vs Papel"}],
            9: [{human_player:"Paper",machine_player:"Rock"},{"Resultado":human_player+" gana","Mensaje":"Papel vence a Roca"}],
        }


        if dic_options == switcher.get(1)[0]:
            print(f"{human_player} Roca vs Tijera {machine_player}")
            print(switcher.get(1)[1].get("Resultado")+" | "+switcher.get(1)[1].get("Mensaje"))
            self.__human_point+=1
            self.__score_game = f"{human_player} *Roca* ({self.__human_point}) - ({self.__machine_point}) *Tijera* {self.__machine}"
            self.__summary_game.append(self.__score_game)

        if dic_options == switcher.get(2)[0]:
            print(f"{human_player} Roca vs Papel {machine_player}")
            print(switcher.get(2)[1].get("Resultado")+" | "+switcher.get(2)[1].get("Mensaje"))
            self.__machine_point+=1
            self.__score_game = f"{human_player} *Roca* ({self.__human_point}) - ({self.__machine_point}) *Papel* {self.__machine}"
            self.__summary_game.append(self.__score_game)


        if dic_options == switcher.get(3)[0]:
            print(f"{human_player} Roca vs Roca {machine_player}")
            print(switcher.get(3)[1].get("Resultado")+" | "+switcher.get(3)[1].get("Mensaje"))
            self.__score_game = f"{human_player} *Roca*  ({self.__human_point}) - ({self.__machine_point}) *Roca* {self.__machine}"
            self.__summary_game.append(self.__score_game)

        if dic_options == switcher.get(4)[0]:
            print(f"{human_player} Tijera vs Tijera {machine_player}")
            print(switcher.get(4)[1].get("Resultado")+" | "+switcher.get(4)[1].get("Mensaje"))
            self.__score_game = f"{human_player} *Tijera* ({self.__human_point}) - ({self.__machine_point}) *Tijera* {self.__machine}" 
            self.__summary_game.append(self.__score_game)

        if dic_options == switcher.get(5)[0]:
            print(f"{human_player} Tijera vs Papel {machine_player}")
            print(switcher.get(5)[1].get("Resultado")+" | "+switcher.get(5)[1].get("Mensaje"))
            self.__human_point+=1
            self.__score_game = f"{human_player} *Tijera* ({self.__human_point}) - ({self.__machine_point}) *Papel* {self.__machine}"
            self.__summary_game.append(self.__score_game)

        if dic_options == switcher.get(6)[0]:
            print(f"{human_player} Tijera vs Roca {machine_player}")
            print(switcher.get(6)[1].get("Resultado")+" | "+switcher.get(6)[1].get("Mensaje"))
            self.__machine_point+=1
            self.__score_game = f"{human_player} *Tijera*  ({self.__human_point}) - ({self.__machine_point}) *Roca* {self.__machine}"
            self.__summary_game.append(self.__score_game)

        if dic_options == switcher.get(7)[0]:
            print(f"{human_player} Papel vs Tijera {machine_player}")
            print(switcher.get(7)[1].get("Resultado")+" | "+switcher.get(7)[1].get("Mensaje"))
            self.__machine_point+=1
            self.__score_game = f"{human_player} *Papel* ({self.__human_point}) - ({self.__machine_point}) *Tijera* {self.__machine}"
            self.__summary_game.append(self.__score_game)

        if dic_options == switcher.get(8)[0]:
            print(f"{human_player} Papel vs Papel {machine_player}")
            print(switcher.get(8)[1].get("Resultado")+" | "+switcher.get(8)[1].get("Mensaje"))
            self.__score_game = f"{human_player} *Papel* ({self.__human_point}) - ({self.__machine_point}) *Papel* {self.__machine}" 
            self.__summary_game.append(self.__score_game)
      

        if dic_options == switcher.get(9)[0]:
            print(f"{human_player} Papel vs Roca {machine_player}")
            print(switcher.get(9)[1].get("Resultado")+" | "+switcher.get(9)[1].get("Mensaje"))
            self.__human_point+=1
            self.__score_game = f"{human_player} *Papel* ({self.__human_point}) - ({self.__machine_point}) *Roca* {self.__machine}"
            self.__summary_game.append(self.__score_game)

    
    def show_summary_game(self,player):
        # print(self.__summary_game[0])
        # print(range(0,len(self.__summary_game)-1))
        print(50*"*")
        print("RESUMEN DEL JUEGO")
        print(50*"*")

        for i in range(0,len(self.__summary_game)):
            print(f'Ronda #{i+1} {self.__summary_game[i]}')

        print(50*"*")
        print(50*"_")
        print(50*"_")
        print(50*"_")

        if(self.__human_point > self.__machine_point):
            print(50*"")
            print(f'El Ganador es: {player}')
        elif self.__human_point < self.__machine_point:
            print(f'El ganador es: {self.__machine}')
        else:
            print("Tablas")

        print(50*"_")
        print(50*"_")
        print(50*"_")
    
    
        

        

        # for i in range(1,)
        #     print(i)
        #     print(f'Ronda # {i} {self.__summary_game[i]}')

    

        


    
        
    

