OPPONENT_HAND_MAP = {"A": "R", "B": "P" , "C": "S"}
MY_HAND_MAP = {"X": "R", "Y": "P" , "Z": "S"}
OUTCOME_MAP = {"X": "L", "Y": "D" , "Z": "W"}
OPPONENT_OUTCOME_MY_HAND_MAP = {
    "R": {"W": "P", "D": "R", "L": "S"},
    "P": {"W": "S", "D": "P", "L": "R"},
    "S": {"W": "R", "D": "S", "L": "P"}
}
GAME_POINTS_MAP = {
    "R": {"P": 6, "R": 3, "S": 0},
    "P": {"S": 6, "P": 3, "R": 0},
    "S": {"R": 6, "S": 3, "P": 0}
}
HAND_POINTS_MAP = {
    "R": 1,
    "P": 2,
    "S": 3
}


def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]


def calculate_points(opponent_hand: str, my_hand: str):
    game_points = GAME_POINTS_MAP.get(opponent_hand).get(my_hand)
    hand_points = HAND_POINTS_MAP.get(my_hand)
    return sum((game_points, hand_points))


def one():    
    total_points = 0
    for game in read_input("src/aoc/02/02.txt"):
        opponent_hand = OPPONENT_HAND_MAP.get(game[0])
        my_hand = MY_HAND_MAP.get(game[2])
        total_points += calculate_points(opponent_hand, my_hand)
    print(f"[1]: {total_points}")


def two():
    total_points = 0
    for game in read_input("src/aoc/02/02.txt"):
        opponent_hand = OPPONENT_HAND_MAP.get(game[0])
        outcome = OUTCOME_MAP.get(game[2])
        my_hand = OPPONENT_OUTCOME_MY_HAND_MAP.get(opponent_hand).get(outcome)
        total_points += calculate_points(opponent_hand, my_hand)
    print(f"[2]: {total_points}")

def main():
    one()
    two()

if __name__ == "__main__":
    main()