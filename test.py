def bresenham(x0, y0, x1, y1):
    
    dx, dy = x1 - x0, y1 - y0
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx, dy = abs(dx), abs(dy)
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
    D = 2*dy - dx
    y = 0
    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy

#print(list(bresenham(3, 10,1, 4)))
#print(list(bresenham(1, 1, 3, 1)))
#print(list(bresenham(1, 1, 2, 3)))
print(list(bresenham(1, 4, 4, 2)))
print(list(bresenham(1, 4, 3, 10)))
print(list(bresenham(4, 2, 3, 10)))

