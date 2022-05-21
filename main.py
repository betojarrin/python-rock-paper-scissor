from player import Player
from ppt_game import Game


def run():
    try:
        print("Bienvenido a Piedra Papel o Tijera")
        while True:
            name_player = input("Ingresa tu nombre para competir: ")
            if name_player == "":
                print("Por favor ingresa tu nombre para poder jugar")
                continue
            else:
                player = Player(name_player)
                game = Game()
                game.play_game(player.player_name)
                print("fin del juego")
                return False
    except ValueError as ve:
        print(ve)

if __name__ == ("__main__"):
    run()