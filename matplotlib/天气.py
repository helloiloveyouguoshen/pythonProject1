from matplotlib import pyplot as plt
fig = plt.figure(figsize=(30,4),dpi=80)
x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]

plt.plot(x,y)
# plt.xticks(range(2,25))
_xtick_labels = [i/2 for i in range(4,49)]
plt.xticks(range(25,50))
plt.savefig("./picture/1.svg")
plt.show()