
class PvP:
    def __init__(self):
        self.player = 1
        pass

    def valid_input(self, pick_up, num_of_sticks):
        if pick_up in [1, 2, 3] and pick_up < num_of_sticks:
            return True
        else:
            return False

    def win(self, player, num_of_sticks):
        if num_of_sticks == 1:
            print("player", player, "wins")
            return True

    def switch_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1
        return self.player

    def valid_num_of_sticks(self, num_of_sticks):
        if num_of_sticks >= 10 and num_of_sticks <= 100:
            return True
        else:
            print("please enter a number 10-100")
            return False

    def gameplay(self):
        player = 1
        while True:
            num_of_sticks = input("Please enter a number from 10-100: ")
            try:
                num_of_sticks = int(num_of_sticks)
                break
            except ValueError:
                print("Please enter a vaild number")
                continue
        while not self.valid_num_of_sticks(num_of_sticks):
            num_of_sticks = int(input("Please enter a number from 10-100: "))
            print("please enter a number 10-100")
            break

        print("There are", num_of_sticks, "number of sticks left")

        while True:
            print("Player ", player)
            while True:
                pick_up = int(input("Enter the amount of sticks you wish to pick up: "))
                if self.valid_input(pick_up, num_of_sticks):
                    break
                else:
                    print("Please enter a vaild number")

            num_of_sticks -= pick_up
            if self.win(player, num_of_sticks):
                break
            player = self.switch_player()
            print("\nthere are", num_of_sticks, "sticks left")

        print("Game over")
