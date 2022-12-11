import math
import operator

OPS = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]


def get_monkeys():
    lines = read_input("src/aoc/11/11.txt")
    monkeys = {}
    for idx in range(0, len(lines), 7):
        monkey_idx = int(lines[idx].replace("Monkey ", "").replace(":", ""))
        items = [int(item) for item in lines[idx + 1].replace("Starting items: ", "").split(", ")]
        operation = lines[idx + 2].replace("  Operation: new = old ", "").split(" ")
        test = int(lines[idx + 3].replace("  Test: divisible by ", ""))
        test_true = int(lines[idx + 4].replace("    If true: throw to monkey ", ""))
        test_false = int(lines[idx + 5].replace("    If false: throw to monkey ", ""))
        monkeys[monkey_idx] = {
            "items": items,
            "operation": operation,
            "test": test,
            "if_true": test_true,
            "if_false": test_false,
            "no_inspected": 0
        }
    return monkeys


def do_monkey_business(rounds, worry_divider):
    monkeys = get_monkeys()
    for r in range(1, rounds + 1):
        for m in range(0, len(monkeys)):
            for i in range(0, len(monkeys[m]["items"])):
                opr_val = monkeys[m]["items"][i] if monkeys[m]["operation"][1] == "old" else int(monkeys[m]["operation"][1])
                new = OPS[monkeys[m]["operation"][0]](monkeys[m]["items"][i], opr_val)
                cwl = math.floor(new / worry_divider) if worry_divider > 1 else new
                if cwl % monkeys[m]["test"] == 0:
                   monkeys[monkeys[m]["if_true"]]["items"].append(cwl)
                else:
                   monkeys[monkeys[m]["if_false"]]["items"].append(cwl)
                monkeys[m]["no_inspected"] += 1
            monkeys[m]["items"] = []
    return sorted([v['no_inspected'] for _, v in monkeys.items()], reverse=True)

    
def run():
    p1 = do_monkey_business(20, 3)
    print(f"[1]: {p1[0] * p1[1]}")
    p2 = do_monkey_business(10000, 1)
    print(f"[2]: {p2[0] * p2[1]}")

def main():
    run()


if __name__ == "__main__":
    main()