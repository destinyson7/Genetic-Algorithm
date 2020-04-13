import numpy as np
from client_moodle import *

secret_keys = ['se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2', 'ox5ZDGP4WNz3B8mUC7zSdS7PdrPIJOXWnRsH5QPrl5GyJ0TZwq', 'EdQPhzkQ1CnpQ9jxCY4AH8eATTHeZm4IwEs2P1jE2xT3p8sCeE']

# OUR: se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2
# JASHN: mBAkj2CeFNwihROmN2lzWnH6EJ9uBAXQGBxUD4hnRDKzm1BWkm
# SWASTIK: RVOghkfjIZR3X3vImlTXMmYmSU9uc790vLqjTozGD4Ka9qFtO1
# AKSHAT: MsOYrg4QoHcnSUht1hvbjhYM5BgzBcQT5HO3WVReiC338ykhP1
# ANIMESH: EdQPhzkQ1CnpQ9jxCY4AH8eATTHeZm4IwEs2P1jE2xT3p8sCeE
# PRIYANSHU: ox5ZDGP4WNz3B8mUC7zSdS7PdrPIJOXWnRsH5QPrl5GyJ0TZwq

requests = 12000
num_coefficients = 11

epsillon = 1 / 200

answer = [9.99333333333113]

init_best = [0 for c in range(num_coefficients)]
ini_min_error_arr = get_errors(secret_keys[1], init_best)
ini_min_error = ini_min_error_arr[0] * ini_min_error_arr[1]

used_requests = 1
ind = 0

for i in range(1, 2, 1):

    vector = [0 for c in range(num_coefficients)]
    best = 0
    min_error = ini_min_error

    for j in np.arange(-10, 10, epsillon):
        vector[i] = j

        err = get_errors(secret_keys[1], vector)
        used_requests += 1

        fitness = err[0] * err[1]

        if fitness < min_error:
            min_error = fitness
            best = vector[i]

    answer.append(best)
    print(answer, min_error)
    print()
    print()
    print()

print(answer)
print()
print()
print()

# final_err = get_errors(secret_keys[ind], answer)

# save = {}
# save[str(answer)] = final_err
# json.dump(save, open("epsillon_best.txt", 'w'))
