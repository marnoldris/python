
import matplotlib.pyplot as plt

def ball_trajectory(x):
    location = 10*x - 5*(x**2)
    return (location)

xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(x) for x in xs]

xs2 = [0.1, 2]
ys2 = [ball_trajectory(0.1), 0]
xs3 = [0.2, 2]
ys3 = [ball_trajectory(0.2), 0]
xs4 = [0.3, 2]
ys4 = [ball_trajectory(0.3), 0]

#plt.plot(xs, ys)
plt.title('The Trajectory of a thrown ball')
plt.xlabel('Horizontal position')
plt.ylabel('Vertical position')
plt.axhline(y = 0)
plt.plot(xs, ys, xs2, ys2, xs3, ys3, xs4, ys4)
plt.show()
