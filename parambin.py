import random
import matplotlib.pyplot as plt

#standard distribution
x = []

for i in range(10000):
    newval = int(round(random.gauss(4.5, 2.8877)))
    print newval
    print "appending",newval
    x.append(newval)

binrange = max(x) - min(x)
print "max", max(x), "min", min(x)

plt.hist(x,binrange)
plt.show()


# plt.hist(x, bins=22)
# for i in range(10000):
#     x.append(int(round(random.gauss(4.5, 2.8877)))%9)
# x = []
# for i in range(10000):
#     x.append(int(round(random.gauss(4.5, 2.8877)))%9)
# x
# plt.hist(x, bins=22)
# plt.hist(x)
# for i in range(10000):
#     x.append(int(round(random.gauss(4.5, 2.8877)))%9)
# for i in range(10000):
#     x.append(int(round(random.gauss(4.5, 2.8877)))%9)
# for i in range(10000):
#     x.append(int(round(random.gauss(4.5, 2.8877)))%9)
# for i in range(10000):
#     x.append(int(round(random.gauss(4.5, 2.8877)))%9)
# plt.hist(x)
# plt.hist(x, bins=9)
