
#length of board side
lobs = 6

# board
board = [[0 for i in range(lobs)] for l in range(lobs)]

#moves a knight can make
knightmoves = [[-1, 2], [1, 2], [-2, 1], [2, 1], [1, -2], [-1, -2], [2, -1], [-2, -1]]

#checks if you can move there
def legalmove(x,y):
    if((0 <= x < lobs) and (0 <= y < lobs) and board[x][y] == 0):
        return True
    return False

#recursive function that solves a knights tour and adds the moves to the board 2d list
def solveit(x, y, stepcount):
    #stops recursion
    if stepcount > lobs*lobs:
        return True
    #tests if x move is possible, then moves the knight there
    for move in knightmoves:
        nextx = x+move[0]
        nexty = y+move[1]
        if legalmove(nextx, nexty):
            board[nextx][nexty] = stepcount
            if solveit(nextx, nexty, stepcount+1):
                return True
            board[nextx][nexty] = 0
    return False

#prints the board when done
def solution():
    for r in board:
        for c in r:
            print('0'+str(c) if c < 10 else c, end=' ')
        print()

def main():
    print('Welcome to a 6x6 Knight\'s tour solver!')
    print('Warning: The process uses lots of memory, but will eventually finish.')

    try:
        ix = int(input('Enter x(Integer between 0 and 5): '))
        iy = int(input('Enter y(Integer between 0 and 5): '))
        print('Processing...')
        board[ix][iy] = 1
        if solveit(ix, iy, 2):
            print('Finished!')
            solution()
        else:
            print('Didn\'t work, please try again!')
    except IndexError:
        print('Enter valid x and ys. Try again!')
    except ValueError:
        print('Enter numbers. Try Again!')


if __name__ == '__main__':
    main()








