from PvP import PvP
from PvC import PvC


class Game:
    def main(self):
        while True:
            mode = input("Press 1 for PvP and 2 for PvC: ")
            try:
                mode = int(mode)
                break
            except ValueError:
                print("Please enter 1 or 2")
                continue
        if mode == 1:
            PvP().gameplay()
        elif mode == 2:
            PvC().gameplay()


if __name__ == '__main__':
    Game().main()
