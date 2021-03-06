from matplotlib import pyplot as plt


def logistic_map(r, x, n):
    results = []
    for i in range(n):
        x = r * x * (1 - x)
        results.append(x)
    return results


def plot_trajectory(r, x, n):
    results = logistic_map(r, x, n)
    plt.plot(results, "ob")
    plt.show()


def plot_diffs(r, x, xhat, n):
    trajectory1 = logistic_map(r, x, n)
    trajectory2 = logistic_map(r, xhat, n)
    xPoints = range(n)
    yPoints = []
    for i in xPoints:
        diff = abs(trajectory1[i] - trajectory2[i])
        yPoints.append(diff)
    plt.plot(xPoints, yPoints, "ob")
    plt.show()


def avg_abs_diff(r, x, xhat, n):
    trajectory1 = logistic_map(r, x, n)
    trajectory2 = logistic_map(r, xhat, n)
    diffs = [abs(trajectory1[i]-trajectory2[i]) for i in range(n)]
    return sum(diffs)/n


def plot_bifurcation(x0, rmin, rmax, rstep, n, k):
    xpoints = []
    ypoints = []
    r = rmin
    while r < rmax:
        mapr = logistic_map(r, x0, n)
        for pt in mapr[k:]:
            xpoints.append(r)
            ypoints.append(pt)
        r += rstep
    plt.plot(xpoints, ypoints, "ob", alpha=0.5)
    plt.show()
