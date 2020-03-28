from client_moodle import *
import random
import json

k = 10
num_generations = 245

secret_key = 'se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2'

# OUR: se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2
# JASHN: mBAkj2CeFNwihROmN2lzWnH6EJ9uBAXQGBxUD4hnRDKzm1BWkm
# SWASTIK: RVOghkfjIZR3X3vImlTXMmYmSU9uc790vLqjTozGD4Ka9qFtO1
# AKSHAT: MsOYrg4QoHcnSUht1hvbjhYM5BgzBcQT5HO3WVReiC338ykhP1
# ANIMESH: EdQPhzkQ1CnpQ9jxCY4AH8eATTHeZm4IwEs2P1jE2xT3p8sCeE
# PRIYANSHU: ox5ZDGP4WNz3B8mUC7zSdS7PdrPIJOXWnRsH5QPrl5GyJ0TZwq

small_random_prob = 0.63

initial_coefficients = json.load(open("coefficients.txt"))
init = []

min_error = (1e12, 1e12)
best_coeff = []
errors = []

ratio = 1
mutation_range = 1e-13

for i in initial_coefficients:
    if min_error > (float(abs(initial_coefficients[i][0] + ratio * initial_coefficients[i][1]) + 2 * abs(initial_coefficients[i][0] - ratio * initial_coefficients[i][1])), float(abs(initial_coefficients[i][0] + ratio * initial_coefficients[i][1]))):
        min_error = (float(abs(initial_coefficients[i][0] + ratio * initial_coefficients[i][1]) + 2 * abs(initial_coefficients[i][0] - ratio * initial_coefficients[i][1])), float(abs(initial_coefficients[i][0] + ratio * initial_coefficients[i][1])))

        best_coeff = i.strip('][').split(', ')
        both_errors = (initial_coefficients[i][0], initial_coefficients[i][1])

    init.append(list(map(float, i.strip('][').split(', '))))

    errors.append(((float(abs(initial_coefficients[i][0] + ratio * initial_coefficients[i][1]) + 2 * abs(initial_coefficients[i][0] - ratio * initial_coefficients[i][1])), float(abs(initial_coefficients[i][0] + ratio * initial_coefficients[i][1]))), list(map(
        float, i.strip('][').split(', '))), (initial_coefficients[i][0], initial_coefficients[i][1])))

while len(init) < k:
    init.append(list(map(float, best_coeff)))
    errors.append((min_error, list(map(float, best_coeff)), both_errors))

# print(errors)

err = [[1, 1] for j in range(k)]

state = [init[j] for j in range(k)]


# def get_errors(id, vector):
#     return [1, 10000]


print(errors)
print()
print()
print()


def mutate(child):
    # no_of_mutation = random.randint(1, 6)
    no_of_mutation = 1

    for i in range(no_of_mutation):
        index = random.randint(0, 10)

        new_val = random.uniform(-20, 20)
        new_val /= 100
        new_val *= child[index]

        child[index] += new_val
        child[index] = max(child[index], -10)
        child[index] = min(child[index], 10)

    return child


def crossover(child1, child2):
    crossover_point = random.randint(0, 10)
    a = child1[:crossover_point] + child2[crossover_point:]
    b = child2[:crossover_point] + child1[crossover_point:]

    return a, b


# def select(prob_weights):
#     val = random.uniform(0, 100)

#     if val < prob_weights[0]:
#         return state[0]

#     elif val < prob_weights[0] + prob_weights[1]:
#         return state[1]

#     elif val < prob_weights[0] + prob_weights[1] + prob_weights[2]:
#         return state[2]

#     else:
#         return state[3]

for i in range(num_generations):
    err = [get_errors(secret_key, state[j]) for j in range(k)]

    fitness = [(err[j][0] + ratio * err[j][1] + 2 * abs(err[j][0] - ratio * err[j][1]), abs(err[j][0] + ratio * err[j][1])) for j in range(k)]
    # fitness = [(ratio * err[j][1]) for j in range(k)]

    # print(i, errors)
    # print()
    # print()
    # print()

    new_errors = errors

    for j in range(k):
        tup = (fitness[j], state[j], (err[j][0], err[j][1]))
        new_errors.append(tup)
    new_errors.sort()

    errors = [new_errors[j] for j in range(k)]

    const = 100 / (1 / fitness[0][0] + 1 / fitness[1][0] +
                   1 / fitness[2][0] + 1 / fitness[3][0])

    perc = [const / fitness[j][0] for j in range(k)]

    new_state = random.choices(state, perc, k=k)
    # print(new_state)

    for j in range(k // 2):
        new_state[2 * j], new_state[2 * j + 1] = crossover(new_state[2 * j], new_state[2 * j + 1])

        new_state[2 * j] = mutate(new_state[2 * j])
        new_state[2 * j + 1] = mutate(new_state[2 * j + 1])

    state = new_state

print(errors)
new_coefficients = {}
for i in range(k):
    new_coefficients[str(errors[i][1])] = [errors[i][2][0], errors[i][2][1]]

json.dump(new_coefficients, open("coefficients.txt", 'w'))
