from AoC import common

data = common.get_input(int)

increases = 0
for i in range(int(len(data)/3)*3):
    try:
        window1 = data[i] + data[i+1] + data[i+2]
        window2 = data[i+1] + data[i+2] + data[i+3]
    except IndexError:
        continue
    if window2 > window1:
        increases += 1
        print("%s (increased)" % window2)
    elif window2 == window1:
        print("%s (no change)" % window2)
    else:
        print("%s (decreased)" % window2)

print(increases)
