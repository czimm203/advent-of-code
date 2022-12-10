#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

from collections import namedtuple

MY_MOVES = {"X": 1, "Y":2, "Z":3}
OTHER_MOVES = {"A": 1, "B":2, "C":3}
DESIRED = {"X": "loss", "Y":"draw","Z":"win"}

Move = namedtuple("move",["loss","draw","win"])
move_matrix = {"A": Move("Y","X","Z"), "B":Move("Z","Y","X"),"C":Move("X","Z","Y")}


def game(me:str, them:str) -> int:
    my_score = MY_MOVES[me]
    them_score = OTHER_MOVES[them]
    bonuses = {"win": 6, "draw":3, "loss":0}

    if my_score == them_score:
        outcome = "draw"
    elif my_score == 1 and them_score == 2:
        outcome = "loss"
    elif my_score == 1 and them_score == 3:
        outcome = "win"
    elif my_score == 2 and them_score == 3:
        outcome = "loss"
    elif my_score == 2 and them_score == 1:
        outcome = "win"
    elif my_score == 3 and them_score == 1:
        outcome = "loss"
    elif my_score == 3 and them_score == 2:
        outcome = "win"
    else:
        raise ValueError

    bonus = bonuses[outcome]
    my_score+=bonus

    return my_score

def game2(them:str, desire:str) -> int:
    my_score = 0 
    # them_score = OTHER_MOVES[them]
    bonuses = {"win": 6, "draw":3, "loss":0}
    outcome = DESIRED[desire]
    my_move = ""
    if outcome == "draw":
        my_move = move_matrix[them].draw
    elif outcome == "loss":
        my_move = move_matrix[them].win
    else:
        my_move = move_matrix[them].loss

    my_score = MY_MOVES[my_move]
    bonus = bonuses[outcome]

    my_score+=bonus

    return my_score
        
if __name__ == "__main__":
    with open("./input.txt") as f:
        lines = f.readlines()

    score1 = 0
    score2 = 0
    for line in lines:
        play = line.strip().split(" ")
        score1 += game(play[1], play[0])
        score2 += game2(*play)

    print(score1, score2)
