from AoC import common

data = common.get_input(sample=False)

pos = {'horizontal': 0, 'depth': 0}


def forward(dist):
    pos['horizontal'] += dist


def up(dist):
    pos['depth'] -= dist


def down(dist):
    pos['depth'] += dist


commands = {
    'forward': forward,
    'up': up,
    'down': down,
}
for d in data:
    command, distance = d.split()
    distance = int(distance)
    commands[command](distance)

print(pos['horizontal'] * pos['depth'])
