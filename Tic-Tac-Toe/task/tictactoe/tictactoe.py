# write your code here
class TicTacToe:
    input_values = input()

    def standard_matrix(self):
        counter = 0
        temp_list = []
        print("---------")
        #  print("X O X \nO X X \nX X O")
        for value in self.input_values:
            counter += 1
            temp_list.append(value)
            if counter % 3 == 0:
                print(f"| {temp_list[0]} {temp_list[1]} {temp_list[2]} |")
                temp_list = []
        print("---------")


game = TicTacToe()
game.standard_matrix()
