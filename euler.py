def forward_euler(xt0, vt0, dt, g, k, m, B):
	xprime = vt0
	print(f"x' = {xprime}")
	vprime = g - ((k * xt0) / m) - ((B/m) * vt0)
	print(f"v' = {vprime}")
	x = xt0 + dt * xprime
	print(f"x = {x}")
	v = vt0 + dt * vprime
	print(f"v' = {v}")
	return (x, v)


def backward_euler(xt0, vt0, dt, g, k, m, B):
	xfe, vfe = forward_euler(xt0, vt0, dt, g, k, m, B)
	xprime = vfe
	vprime = g - ((k * xfe) / m) - ((B/m) * vfe)
	x = xt0 + dt * xprime
	v = vt0 + dt * vprime
	return (x, v)


from pprint import pprint
from matplotlib import pyplot as plt

# forward Euler
# x' = v
# v' = G - (Bv)/m - (kx)/m
def fe(x, v, h, tfinal, m=1, k=1, G=9.8, B=0):
    t = 0
    steps = [(x, v)]
    while t < tfinal:
        xprime = v
        vprime = G - (B*v)/m - (k*x)/m
        x = x + (h * xprime)
        v = v + (h * vprime)
        steps.append((x, v))
        t += h
    return steps


# backward Euler
def be(x, v, h, tfinal, m=1, k=1, G=9.8, B=0):
    t = 0
    steps = [(x, v)]
    while t < tfinal:
        xfe, vfe = fe(x, v, h, h, m, k, G, B)[1]
        xprime = vfe
        vprime = G - (B*vfe)/m - (k*xfe)/m
        x = x + (h * xprime)
        v = v + (h * vprime)
        steps.append((x, v))
        t += h
    return steps


def quiz(): 
    pprint(fe(-1, -2, 0.1, 0.1, 0.5, 2, 0, 0))


def hw_q1a():
    pprint(fe(-1, -2, 0.1, 0.5, 0.5, 2, 0, 0))


def hw_q1b():
    steps = fe(-1, -2, 0.1, 19.9, 0.5, 2, 0, 0)
    xpoints = [step[0] for step in steps]
    ypoints = [step[1] for step in steps]
    steps2 = fe(-1, -2, 0.11, 21.8, 0.5, 2, 0, 0)
    xpoints2 = [step[0] for step in steps2]
    ypoints2 = [step[1] for step in steps2]
    fig = plt.figure()
    axis = fig.add_subplot(111)
    axis.plot(xpoints, ypoints, "ob")
    axis.plot(xpoints2, ypoints2, "or")
    plt.show()


def hw_q2a():
    pprint(be(-1, -2, 0.1, 0.5, 0.5, 2, 0, 0))


def hw_q2b():
    steps = be(-1, -2, 0.1, 19.9, 0.5, 2, 0, 0)
    xpoints = [step[0] for step in steps]
    ypoints = [step[1] for step in steps]
    steps2 = be(-1, -2, 0.11, 21.8, 0.5, 2, 0, 0)
    xpoints2 = [step[0] for step in steps2]
    ypoints2 = [step[1] for step in steps2]
    fig = plt.figure()
    axis = fig.add_subplot(111)
    axis.plot(xpoints, ypoints, "ob")
    axis.plot(xpoints2, ypoints2, "or")
    plt.show()


def hw_q2c():
    steps = fe(-1, -2, 0.1, 5, 0.5, 2, 0, 0)
    xpoints = [step[0] for step in steps]
    ypoints = [step[1] for step in steps]
    steps2 = be(-1, -2, 0.1, 5, 0.5, 2, 0, 0)
    xpoints2 = [step[0] for step in steps2]
    ypoints2 = [step[1] for step in steps2]
    fig = plt.figure()
    axis = fig.add_subplot(111)
    axis.plot(xpoints, ypoints, "ob")
    axis.plot(xpoints2, ypoints2, "or")
    plt.show()
