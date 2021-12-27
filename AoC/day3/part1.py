import copy

from AoC import common

data = common.get_input(sample=False)


def calc_gamma_epsilon():
    bits = [0 for x in range(len(data[0]))]
    for d in data:
        for i in range(len(d)):
            if d[i] == '0':
                bits[i] -= 1
            else:
                bits[i] += 1

    gamma_rate = ""
    epsilon_rate = ""
    for bit in bits:
        if bit <= 0:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"
    return int(gamma_rate, 2), int(epsilon_rate, 2)

gamma, epsilon = calc_gamma_epsilon()

print(gamma * epsilon)
