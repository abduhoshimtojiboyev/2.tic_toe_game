column = " | "
row = "---------"
positions = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
example = f" 1 | 2 | 3 \n{row}\n 4 | 5 | 6 \n{row}\n 7 | 8 | 9"
winning_positions = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]


def draw_field():
    field = ""
    for i in range(1, 10):
        piece = f"{positions[i]}"
        if i == 3 or i == 6:
            piece += f"\n{row}\n"
        elif i < 9:
            piece += column
        field += piece
    return print(field)
    # field= f"{postions[1]} | {postions[2]} | {postions[3]} | {postions[4]} | {postions[5]} | {postions[6]} | {postions[7]} | {postions[8]}"


def check(index):
    if positions[index] != "0" and positions[index] != "x":
        return True


def check_winning(test):
    for winning in winning_positions:
        if set(winning).issubset(set(test)):
            return True


print(example)
n = 0
beginner = input('which one begin first x/0: ')
if beginner == "x":
    n = 1
else:
    n = 2  # it means 0

keys_0 = []
keys_x = []
while True:

    if n % 2 == 0:
        sign = "0"
        index = int(input(f'{sign}`s turn. Please choose position where you want to draw (1-9): '))
        if 10 > index > 0:
            if check(index):
                keys_0.append(index)
                positions[index] = sign
                draw_field()
                if check_winning(keys_0) and len(keys_0)>2:
                    print(f"\n\nyou win {sign}'s player")
                    break
                n += 1
            else:
                print('this place already drawn')
    else:
        sign = "x"
        index = int(input(f'{sign}`s turn. Please choose position where you want to draw (1-9): '))
        if 10 > index > 0:
            if check(index):
                keys_x.append(index)
                positions[index] = sign
                draw_field()
                if check_winning(keys_x) and len(keys_x)>2:
                    print(f"\n\nyou win {sign}'s player")
                    break
                n += 1
            else:
                print('this place already drawn')

