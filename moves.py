from Perso.supermap import supermap


def mov(supermap, Playpos):
    dir = input()
    if dir == "D":
        Playpos[1] = Playpos[1] + 1
    if dir == "S":
        Playpos[0] = Playpos[0] + 1
    if dir == "Z":
        Playpos[0] = Playpos[0] - 1 
    if dir == "Q":
        Playpos[1] = Playpos[1] -1
    supermap[Playpos[0]][Playpos[1]] = "P"
    return Playpos
M = supermap()
P = [0, 0]
P = mov(M, P)
