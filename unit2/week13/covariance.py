x = [10, 12, 14, 8]
y = [40, 48, 56, 32]

#x bar

xbar = 0

for i in x:
    xbar += i

xbar /= len(x)

#y bar

ybar = 0

for i in y:
    ybar += i

ybar /= len(y)

#covariance

cov = 0

for i in range(len(x)):
    tempx = x[i] - xbar
    tempy = y[i] - ybar

    cov += tempx * tempy

cov /= len(x) - 1

print(xbar)
print(ybar)
print(cov)

