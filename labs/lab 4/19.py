import math

r = float(input())
x0, y0 = map(float, input().split())
x1, y1 = map(float, input().split())

dx = x1 - x0
dy = y1 - y0
d = math.hypot(dx, dy)

def line_intersects_circle():
    a = dx*dx + dy*dy
    b = 2*(x0*dx + y0*dy)
    c = x0*x0 + y0*y0 - r*r
    disc = b*b - 4*a*c
    return disc >= 0 and ((-b - math.sqrt(disc)) / (2*a) <= 1 and (-b + math.sqrt(disc)) / (2*a) >= 0)

if not line_intersects_circle():
    print(f"{d:.10f}")
else:
    d0 = math.hypot(x0, y0)
    d1 = math.hypot(x1, y1)
    l0 = math.sqrt(d0*d0 - r*r)
    l1 = math.sqrt(d1*d1 - r*r)
    ang0 = math.acos(r/d0)
    ang1 = math.acos(r/d1)
    theta = math.atan2(y1, x1) - math.atan2(y0, x0)
    while theta < 0: theta += 2*math.pi
    while theta > math.pi: theta -= math.pi
    arc = r * abs(theta - ang0 - ang1)
    print(f"{l0 + l1 + arc:.10f}")