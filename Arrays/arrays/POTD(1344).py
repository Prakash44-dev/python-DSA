hour = 1
minutes = 57
angle = (30*hour)-(5.5*minutes)
print(angle)
if angle<0:
    angle=(-1)*angle
min_angle = min(angle,360-angle)

print(min_angle)