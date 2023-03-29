def hanoi(n):
    tours = [
        [1, [i for i in range(n, 0, -1)]],
        [2, []],
        [3, []]
        ]
    return hanoi_inner(n, tours, [])

def hanoi_inner(n, tours, moves):
    if n != 0:
        hanoi_inner(n-1, [tours[0], tours[2], tours[1]], moves)
        largest_disk = tours[0][1].pop()
        tours[2][1].append(largest_disk)
        moves.append([largest_disk, tours[0][0], tours[2][0]])
        hanoi_inner(n-1, [tours[1], tours[0], tours[2]], moves)
        return moves

moves = hanoi(4)

for move in moves:
    print(f"Déplacez le disque {move[0]} de la tour {move[1]} vers la tour {move[2]}")
print(f"{len(moves)} coups")



""" 
mvo    n : nombre de disques utilisés,
    D : emplacement de départ,
    A : emplacement d'arrivée,
    I : emplacement intermédiaire. """
""" 
procédure Hanoï(n, D, A, I)
    si n ≠ 0
        Hanoï(n-1, D, I, A)
        Déplacer le disque de D vers A
        Hanoï(n-1, I, A, D)
    fin-si
fin-procédure """

""" 1
2          1        1
3          2        2
4        4 3        3 4
X X X    X X X  X X X   """