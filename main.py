import math

def projectile_motion(velocity, angle):
    g = 9.81 # acceleration due to gravity
    vx = velocity * math.cos(math.radians(angle)) # x-velocity
    vy = velocity * math.sin(math.radians(angle)) # y-velocity
    t = vx / g # time of flight
    x = vx * t # horizontal distance traveled
    y = (vy**2) / (2*g) # maximum height reached
    return (x, y, t)

velocity = float(input("Enter the initial velocity (m/s): "))
angle = float(input("Enter the launch angle (degrees): "))
x, y, t = projectile_motion(velocity, angle)

print("Time of flight: {:.2f} seconds".format(t))
print("Horizontal distance traveled: {:.2f} meters".format(x))
print("Maximum height reached: {:.2f} meters".format(y))