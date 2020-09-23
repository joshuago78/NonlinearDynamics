
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