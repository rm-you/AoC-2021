from AoC import common

data = common.get_input(sample=False)

pos = {'horizontal': 0, 'depth': 0, 'aim': 0}


def forward(dist):
    pos['horizontal'] += dist
    pos['depth'] += dist * pos['aim']


def up(dist):
    pos['aim'] -= dist


def down(dist):
    pos['aim'] += dist


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
