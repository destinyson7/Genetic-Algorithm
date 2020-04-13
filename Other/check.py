import json

best_coefficients = json.load(open("individual_best.txt"))

best = []

num_coeff = 11

for i in range(num_coeff):
    best.append(best_coefficients[str(i)][0][1])

print(type(best))
print(type(best[0]))
