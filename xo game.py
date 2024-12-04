import string, random
from gui import *
digits = [x for x in range(1, 11)]

bourd = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



def show():
    print()
    for x in bourd:
        count = 0
        for item in x:
            count += 1
            print(f" {item} ", end="")
            if count != 3:
                print("|", end="")
            if count == 3:
                print()
    print()


def user_play(user_pos):
    user_position = int(user_pos)
    num = True
    digit = []
    while num:
        if user_position in digits and user_position not in digit:
            num = False
            digit.append(user_position)
            for index, value in enumerate(bourd):
                for index_1, value_1 in enumerate(value):
                    if user_position == value_1:
                        bourd[index][index_1] = user
                        show()
                        return True
method = True

def method1():
    lis = [x for x in range(1, 6)]
    random.shuffle(lis)
    n = lis
    for x in n:
        if x == 1:
            if bourd[1][1] in digits:
                agent_raw, agent_colomn = 1, 1
                bourd[1][1] = agent
                agent_played = 0
                print("APlus")
                return
        elif x == 2:
            if bourd[0][0] in digits:
                agent_raw, agent_colomn = 0, 0
                bourd[0][0] = agent
                agent_played = 0
                print("APlus")
                return
        elif x == 3:
            if bourd[0][2] in digits:
                agent_raw, agent_colomn = 0, 2
                bourd[0][2] = agent
                agent_played = 0
                print("APlus")
                return
        elif x == 4:
            if bourd[2][0] in digits:
                agent_raw, agent_colomn = 2, 0
                bourd[2][0] = agent
                agent_played = 0
                print("APlus")
                return
        elif x == 5:
            if bourd[2][2] in digits:
                agent_raw, agent_colomn = 2, 2
                bourd[2][2] = agent
                agent_played = 0
                print("APlus")
                return
    if bourd[0][2] in digits:
        agent_raw, agent_colomn = 0, 2
        bourd[0][2] = agent
        agent_played = 0
        print("APlus")
        return
    elif bourd[1][0] in digits:
        agent_raw, agent_colomn = 1, 0
        bourd[1][0] = agent
        agent_played = 0
        print("APlus")
        return
    elif bourd[1][2] in digits:
        agent_raw, agent_colomn = 1, 2
        bourd[1][2] = agent
        agent_played = 0
        print("APlus")
        return
    elif bourd[2][1] in digits:
        agent_raw, agent_colomn = 2, 1
        bourd[2][1] = agent
        agent_played = 0
        print("APlus")
        return

def method2():
    if bourd[1][1] in digits:
        bourd[1][1] = agent
        agent_raw, agent_colomn = 1, 1
        agent_played = 0
        print("APlus")
        return
    elif bourd[1][0] == user and (bourd[0][1] == user or bourd[0][2] == user) and bourd[0][0] in digits:
        agent_raw, agent_colomn = 0, 0
        bourd[0][0] = agent
        agent_played = 0
        print("APlus")
        return
    elif bourd[1][0] == user and (bourd[2][1] == user or bourd[2][2] == user) and bourd[2][0] in digits:
        agent_raw, agent_colomn = 2, 0
        bourd[2][0] = agent
        agent_played = 0
        print("APlus")
        return
    elif bourd[1][2] == user and (bourd[0][1] == user or bourd[0][0] == user) and bourd[0][2] in digits:
        agent_raw, agent_colomn = 0, 2
        bourd[0][2] = agent
        agent_played = 0
        print("APlus")
        return
    elif bourd[1][2] == user and (bourd[2][1] == user or bourd[2][0] == user) and bourd[2][2] in digits:
        agent_raw, agent_colomn = 2, 2
        bourd[2][2] = agent
        agent_played = 0
        print("APlus")
        return
    elif bourd[0][1] == user and (bourd[1][2] == user or bourd[2][2] == user) and bourd[0][2] in digits:
        agent_raw, agent_colomn = 0, 2
        bourd[0][2] = agent
        agent_played = 0
        print("APlus")
        return
    elif bourd[0][1] == user and (bourd[2][0] == user or bourd[1][0] == user) and bourd[0][0] in digits:
        agent_raw, agent_colomn = 0, 0
        bourd[0][0] = agent
        agent_played = 0
        print("APlus")
        return
    elif bourd[2][1] == user and (bourd[0][2] == user or bourd[1][2] == user) and bourd[2][2] in digits:
        agent_raw, agent_colomn = 2, 2
        bourd[2][2] = agent
        agent_played = 0
        print("APlus")
        return
    elif bourd[2][1] == user and (bourd[0][0] == user or bourd[1][0] == user) and bourd[2][0] in digits:
        agent_raw, agent_colomn = 2, 0
        bourd[2][0] = agent
        agent_played = 0
        print("APlus")
        return
    else: method1()

def agent_play():
    global agent_played
    global state
    global agent_raw
    global agent_colomn
    global method
    
    if method:
        for index, value in enumerate(bourd):
            for index_c, value_c in enumerate(value):
                if value_c == user:
                    if (index,index_c)==(1,1):
                        global chosen_method
                        chosen_method = 1
                        method = False
                    elif (index,index_c)==(0,1) or(index,index_c)==(1,0) or (index,index_c)==(1,2) or (index,index_c)==(2,1):
                        chosen_method = 2
                        method = False
                    elif (index,index_c)==(0,0) or(index,index_c)==(2,0) or (index,index_c)==(0,2) or (index,index_c)==(2,2):
                        chosen_method = 3
                        method = False
    terminate_draw = check_draw()
    while terminate_draw == False:
        terminate_won = check_won()
        if terminate_won == False:
            terminate_lose = check_lose()
            if terminate_lose == False:
                if (
                    (terminate_won == False)
                    and (terminate_lose == False)
                    and (terminate_draw == False)
                ):
                    # (1,1) (0,0) (0,2) (2,0) (2,2)
                    #case num1
                    if bourd[1][1] == user and chosen_method == 1:
                        method1()
                    #case num2
                    elif (bourd[0][1]==user or bourd[1][0]==user or bourd[1][2]==user or bourd[2][1]==user) and chosen_method == 2:
                        method2()
                    #case num3
                    elif (bourd[0][0]==user or bourd[2][0]==user or bourd[0][2]==user or bourd[2][2]==user) and chosen_method == 3:
                        if bourd[1][1] in digits:
                            agent_raw, agent_colomn = 1, 1
                            bourd[1][1] = agent
                            agent_played = 0
                            print("APlus")
                            return
                        if (bourd[0][0] == bourd[2][2] == user) or (bourd[0][2] == bourd[2][0] == user):
                                if bourd[1][0] in digits:
                                    agent_raw, agent_colomn = 1, 0
                                    bourd[1][0] = agent
                                    agent_played = 0
                                    print("APlus")
                                    return
                                elif bourd[1][2] in digits:
                                    agent_raw, agent_colomn = 1, 2
                                    bourd[1][2] = agent
                                    agent_played = 0
                                    print("APlus")
                                    return
                                else:
                                    method2()
                        else:
                            method2()
                    else:
                        chosen_method = 2
                else:
                    return
            return
        else:
            # print("Game Over! APlus Agent wins.")
            state = -1
            return 
    else:
        # print("Game Over! It's Draw.")
        state = 0
        return

def check_draw():
    return all(value not in digits for raw in bourd for value in raw)

def check_won():
    # check raw
    def play_agent(x, y):
        bourd[x][y] = agent
        agent_raw, agent_colomn = x, y
        agent_played = 0
        print("APLus")

    if bourd[0].count(agent) == 2:
        for index, value in enumerate(bourd[0]):
            if value in digits:
                play_agent(0, index)
                return True
    elif bourd[1].count(agent) == 2:
        for index, value in enumerate(bourd[1]):
            if value in digits:
                play_agent(1, index)
                return True
    elif bourd[2].count(agent) == 2:
        for index, value in enumerate(bourd[2]):
            if value in digits:
                play_agent(2, index)
                return True
    # check colunm
    count = 0
    index = 0
    for x in range(3):
        if bourd[x][0] == agent:
            count += 1
        else:
            index = x
    if count == 2 and bourd[index][0] in digits:
        play_agent(index, 0)
        return True
    count = 0
    for x in range(3):
        if bourd[x][1] == agent:
            count += 1
        else:
            index = x
    if count == 2 and bourd[index][1] in digits:
        play_agent(index, 1)
        return True
    count = 0
    for x in range(3):
        if bourd[x][2] == agent:
            count += 1
        else:
            index = x
    if count == 2 and bourd[index][2] in digits:
        play_agent(index, 2)
        return True

    # check diagonal
    count = 0
    for index in range(3):
        if bourd[index][index] == agent:
            count += 1
        else:
            num = index
    if count == 2 and bourd[num][num] in digits:
        play_agent(num, num)
        return True

    # check diagonal الثانوي
    count = 0
    for x in range(3):
        y = 2 - x
        if bourd[x][y] == agent:
            count += 1
        else:
            raw_index, col_index = x, y
    if count == 2 and bourd[raw_index][col_index] in digits:
        play_agent(raw_index, col_index)
        return True
    return False

def check_lose():
    def play_agent(x, y):
        bourd[x][y] = agent
        agent_raw, agent_colomn = x, y
        agent_played = 0
        print("APlus")

    if bourd[0].count(user) == 2:
        for index, value in enumerate(bourd[0]):
            if value in digits and bourd[0][index] in digits:
                play_agent(0, index)
                return True
    elif bourd[1].count(user) == 2:
        for index, value in enumerate(bourd[1]):
            if value in digits and bourd[1][index] in digits:
                play_agent(1, index)
                return True
    elif bourd[2].count(user) == 2:
        for index, value in enumerate(bourd[2]):
            if value in digits and bourd[2][index] in digits:
                play_agent(2, index)
                return True

    count = 0
    index = 0
    for x in range(3):
        if bourd[x][0] == user:
            count += 1
        else:
            index = x
    if count == 2 and bourd[index][0] in digits:
        play_agent(index, 0)
        return True
    count = 0
    for x in range(3):
        if bourd[x][1] == user:
            count += 1
        else:
            index = x
    if count == 2 and bourd[index][1] in digits:
        play_agent(index, 1)
        return True
    count = 0
    for x in range(3):
        if bourd[x][2] == user:
            count += 1
        else:
            index = x
    if count == 2 and bourd[index][2] in digits:
        play_agent(index, 2)
        return True
    # check diagonal
    num = 0
    count = 0
    for index in range(3):
        if bourd[index][index] == user:
            count += 1
        else:
            num = index
    if count == 2 and bourd[num][num] in digits:
        play_agent(num, num)
        return True
    # check diagonal الثانوي
    count = 0
    raw_index, col_index = 0, 0
    for x in range(3):
        y = 2 - x
        if bourd[x][y] == user:
            count += 1
        else:
            raw_index, col_index = x, y
    if count == 2 and bourd[raw_index][col_index] in digits:
        play_agent(raw_index, col_index)
        return True
    return False


if __name__ == "__main__":
    play_again = "y"
    while play_again.lower() == "y":
        gui = TicTacToeGUI()
        user = 'X'
        agent = 'O'
        test = True
        while test == True:
            play = user_play(gui.get_user_input())
            if play:
                check = agent_play()
                print(gui.agent_move(bourd))
                if check_draw():
                    gui.show_message('Its a draw')
                    print('Its a draw')
                if check_lose():
                    gui.show_message('Agent of Aplus wins')
                    print('Agent of Aplus wins')
        bourd = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        method = True
        play_again = input("if you want to play again type y: ").strip().lower()
    else:
        print("Thank you.")
