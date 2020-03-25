from client_moodle import *
import random
import json

secret_key = 'se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2'

# OUR: se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2
# JASHN: mBAkj2CeFNwihROmN2lzWnH6EJ9uBAXQGBxUD4hnRDKzm1BWkm
# SWASTIK: RVOghkfjIZR3X3vImlTXMmYmSU9uc790vLqjTozGD4Ka9qFtO1
# AKSHAT: MsOYrg4QoHcnSUht1hvbjhYM5BgzBcQT5HO3WVReiC338ykhP1
# ANIMESH: EdQPhzkQ1CnpQ9jxCY4AH8eATTHeZm4IwEs2P1jE2xT3p8sCeE
# PRIYANSHU: ox5ZDGP4WNz3B8mUC7zSdS7PdrPIJOXWnRsH5QPrl5GyJ0TZwq

num_coeff = 11

initial_coefficients = json.load(open("individual_coefficients.txt"))
best_coefficients = json.load(open("individual_best.txt"))

init = []
best = []

ratio = 1

for cur_coefficient in range(num_coeff):

    best = []

    best_coefficients = json.load(open("individual_best.txt"))

    for i in range(cur_coefficient):
        best.append(best_coefficients[str(i)][0][1])

    print(best)

    init = []

    for i in initial_coefficients:
        init.append(list(map(float, i.strip('][').split(', '))))

    state = [init[j] for j in range(len(init))]
    for i in state:
        for j in range(len(i)):
            if j < cur_coefficient:
                i[j] = best[j]

            elif j > cur_coefficient:
                i[j] = 0

    print(state)
    print()
    print()
    print()

    coefficients_withErrors = []
    err = [get_errors(secret_key, j) for j in state]

    fitness = [(err[j][0] + ratio * err[j][1]) for j in range(len(state))]

    for j in range(len(state)):
        to_append = (fitness[j], state[j][cur_coefficient])
        coefficients_withErrors.append(to_append)
    coefficients_withErrors.sort()

    old_best = json.load(open("individual_best.txt"))
    old_best[str(cur_coefficient)].append(coefficients_withErrors[0])
    json.dump(old_best, open("individual_best.txt", 'w'))

    print(coefficients_withErrors)
    print()
    print()
    print()

    print(old_best)
    print()
    print()
    print()
