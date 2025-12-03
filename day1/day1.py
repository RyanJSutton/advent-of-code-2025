filename = "input.txt"
dial_start = 50
dial_max = 99
dial_pos = dial_start
zero_count = 0

def get_new_pos(state, movement):
    global step_count
    global dial_max
    direction = movement[0]
    spaces = int(movement[1:])
    match direction:
        case "L":
            newpos = (state - spaces) % (dial_max + 1)
            return newpos
        case "R":
            newpos = (state + spaces) % (dial_max + 1)
            return newpos


with open(filename) as file:
    while line := file.readline():
        movement = line.rstrip()
        dial_pos = get_new_pos(dial_pos, movement)
        if dial_pos == 0:
            zero_count+=1

print(f"Zero Count: {zero_count}")

    