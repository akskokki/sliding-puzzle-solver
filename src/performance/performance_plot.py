import matplotlib.pyplot as plt

with open('performance_log', 'r') as log:
    lines = log.readlines()

values = []
for i in range(81):
    values.append([])

for line in lines:
    line.strip('\n')
    value = line.split(',')
    values[int(value[0])].append(float(value[1]))

values[80] = []

for i in range(81):
    if len(values[i]) == 0:
        values[i] = 0
        continue
    values[i] = sum(values[i]) / len(values[i])
    print(f'{i}: {values[i]}')

fig = plt.figure(figsize=(10, 5))

plot_keys = []
plot_values = []
for i in range(0, 81, 2):
    plot_keys.append(i)
    plot_values.append(values[i])

plt.bar(plot_keys, plot_values, width=1.5)

plt.xlabel('Solution length (moves)')
plt.ylabel('Avg time (s)')
plt.title('Average times to find solutions with the algorithm\
    (runtime capped at 60 seconds)')
plt.show()
