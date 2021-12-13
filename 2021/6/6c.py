import common.util as u
def calc_fish(age, days_rem, spawn_check):
    spawn = days_rem - age
    family = 0
    while spawn >= 1:
        if spawn_check[spawn]:
            family += spawn_check[spawn]
        else:
            spawn_check[spawn] = 1 + calc_fish(8, spawn - 1, spawn_check)
            family += spawn_check[spawn]
        spawn -= 7
    return family


def laternfish():
    ages = []
    with open(u.AOC_2021 + "\\6\\input.txt", 'r') as input:
        ages = [int(age) for age in input.readline().split(",")]
    
    spawn_check = [None for _ in range(300)]
    total = 0
    for age in ages:
        total += 1 + calc_fish(age, 256, spawn_check)
    return total


if __name__ == "__main__":
    print(laternfish())