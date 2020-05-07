from generate import *


pygame.init()
width, height, diff = 800, 800, 40
linecol, AiColor, winColor = (0, 0, 0), (152, 254, 255), (255, 255, 255)
count, tiles, visited, rows, cols, condition = 0, [], [], width//diff, height//diff, False
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Generator")
win.fill(winColor)
clock = pygame.time.Clock()

for row in range(rows):
    for col in range(cols):
        tile = Tiles(row*diff, col*diff, count)
        tiles.append(tile)
        tile.board(tile)
        count += 1

nextTile = tiles[0]
nextTile.current = True
oldTile = nextTile

y = 0
x = 0
while True:
    pygame.draw.line(win, (0, 0, 0), [0, diff + y], [width, diff + y], 2)
    pygame.draw.line(win, (0, 0, 0), [diff + x, 0], [diff + x, height], 2)
    y += diff
    x += diff
    if y == height - diff and x == width - diff:
        break

#  Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        else:
            break

    if nextTile.current:  # Keep track of previous and next tile using temp variables
        nextTile.removeWalls(oldTile, nextTile)
        oldTile = nextTile
        pygame.display.update()

    nextTile = nextTile.checkNeighbors(nextTile.count)
    while nextTile is None or nextTile == 0:  # If no unvisited neighbors, pop visited list until one if found
        if not visited:
            condition = True
            break
        else:
            temp = visited.pop()
            oldTile = temp
            nextTile = temp.checkNeighbors(temp.count)

    if not condition:
        nextTile.current = True

    else:
        x = [0, 1, 2, 3]
        for cells in tiles:
            if not cells.visited:
                cells.walls[random.choice(x)] = False
                cells.board(cells)

        keepItOn()

    clock.tick(1000)