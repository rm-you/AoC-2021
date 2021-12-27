from AoC import common

data = common.get_input(int)

last = None
increases = 0
for value in data:
    if last and value > last:
        increases += 1
    #     print("%s (increased)" % value)
    # else:
    #     print("%s (decreased)" % value)
    last = value

print(increases)
