verticals = (1,2,3,4,5,6,7,8)
horizontals = "abcdefgh"

def get_knight_moves(h, v):
    h = horizontals.index(h)
    v = verticals.index(v)
    moves = []
    moves.append((horizontals[h+2], verticals[v+1])) if h+2 < len(horizontals) and v+1 < len(verticals) else None
    moves.append((horizontals[h+2], verticals[v-1])) if h+2 < len(horizontals) and v-1 >= 0 else None

    moves.append((horizontals[h-2], verticals[v+1])) if h-2 >= 0 and v+1 < len(verticals) else None
    moves.append((horizontals[h-2], verticals[v-1])) if h-2 >= 0 and v-1 >= 0 else None

    moves.append((horizontals[h-1], verticals[v+2])) if h-1 >= 0 and v+2 < len(verticals) else None
    moves.append((horizontals[h-1], verticals[v-2])) if h-1 >= 0 and v-2 >= 0 else None

    moves.append((horizontals[h+1], verticals[v+2])) if h+1 < len(horizontals) and v+2 < len(verticals) else None
    moves.append((horizontals[h+1], verticals[v-2])) if h+1 < len(horizontals) and v-2 >= 0 else None


    return moves

def get_bishop_moves(h, v):
    h = horizontals.index(h)
    v = verticals.index(v)

    moves = []

    i = 1
    while(h+i < len(horizontals) and v+i < len(verticals)):
        moves.append((horizontals[h+i], verticals[v+i]))
        i += 1

    i = -1
    while(h+i >= 0 and v+i >= 0):
        moves.append((horizontals[h+i], verticals[v+i]))
        i -= 1

    i = -1
    j = 1
    while(h+i >= 0 and v+j < len(verticals)):
        moves.append((horizontals[h+i], verticals[v+j]))
        i -= 1
        j += 1

    i = 1
    j = -1
    while(h+i < len(horizontals) and v+j >= 0):
        moves.append((horizontals[h+i], verticals[v+j]))
        i += 1
        j -= 1

    return moves






def main():
    kh = input("Please enter horizontal position of the knight (a,b,c,d,e,f,g,h): ")
    if not (len(kh)==1 and kh in horizontals):
        print("Horizontal input for knight is not a letter")
        return
    kv = input("Please enter vertical position of the knight (1,2,3,4,5,6,7,8): ")
    if not (kv.isdigit() and int(kv) in verticals):
        print("Vertical input for knight is not a number")
        return
    kv = int(kv)


    bh = input("Please enter horizontal position of the bishop (a,b,c,d,e,f,g,h): ")
    if not (len(bh)==1 and bh in horizontals):
        print("Horizontal input for bishop is not a letter")
        return
    bv = input("Please enter vertical position of the bishop (1,2,3,4,5,6,7,8): ")
    if not (bv.isdigit() and int(bv) in verticals):
        print("Vertical input for bishop is not a number")
        return
    bv = int(bv)

    if kh == bh and kv == bv:
        print("They can't be in the same square")
        return

    k_moves = get_knight_moves(kh,kv)
    b_moves = get_bishop_moves(bh, bv)

    if (bh, bv) in k_moves:
        print("Knight can attack bishop")
    elif (kh, kv) in b_moves:
        print("Bishop can attack knight")
    else:
        print("Neither of them can attack each other")



if __name__ == "__main__":
    main()
