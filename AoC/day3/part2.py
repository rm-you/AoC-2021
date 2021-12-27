import copy

from AoC import common

datas = common.get_input(sample=False)


def calc_gamma_epsilon(data):
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
        if bit < 0:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"
    return gamma_rate, epsilon_rate


def calc_oxgen_rate(data):
    oxy_values = copy.copy(data)
    for i in range(len(data[0])):
        gamma, _ = calc_gamma_epsilon(oxy_values)
        for value in copy.copy(oxy_values):
            if value[i] != gamma[i]:
                oxy_values.remove(value)
                if len(oxy_values) == 1:
                    return int(oxy_values[0], 2)


def calc_co2_rate(data):
    co2_values = copy.copy(data)
    for i in range(len(data[0])):
        _, epsilon = calc_gamma_epsilon(co2_values)
        for value in copy.copy(co2_values):
            if value[i] != epsilon[i]:
                co2_values.remove(value)
                if len(co2_values) == 1:
                    return int(co2_values[0], 2)

oxy_rate = calc_oxgen_rate(datas)
co2_rate = calc_co2_rate(datas)

print(oxy_rate * co2_rate)
