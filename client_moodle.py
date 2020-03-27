import json
import requests
import numpy as np

######### DO NOT CHANGE ANYTHING IN THIS FILE ##################
API_ENDPOINT = 'http://10.4.21.147'
PORT = 3000
MAX_DEG = 11

# functions that you can call


def get_errors(id, vector):
    """
    returns python array of length 2
    (train error and validation error)
    """
    for i in vector:
        assert -10 <= abs(i) <= 10
    assert len(vector) == MAX_DEG

    return json.loads(send_request(id, vector, 'geterrors'))


def submit(id, vector):
    """
    used to make official submission of your weight vector
    returns string "successfully submitted" if properly submitted.
    """
    for i in vector:
        assert -10 <= abs(i) <= 10
    assert len(vector) == MAX_DEG
    return send_request(id, vector, 'submit')

# utility functions


def urljoin(root, port, path=''):
    root = root + ':' + str(port)
    if path:
        root = '/'.join([root.rstrip('/'), path.rstrip('/')])
    return root


def send_request(id, vector, path):
    api = urljoin(API_ENDPOINT, PORT, path)
    vector = json.dumps(vector)
    response = requests.post(api, data={'id': id, 'vector': vector}).text
    if "reported" in response:
        print(response)
        exit()

    return response


if __name__ == "__main__":
    """
    Replace "test" with your secret ID and just run this file
    to verify that the server is working for your ID.
    """

    err = get_errors('se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2', [9.99333333333113, 9.995000000003124, -1.170334631314455e-13, 0.045430924415662766, 1.5693232704196097e-13, 1.3309551235711984e-12, 7.033882924317932e-14, 9.144581536698287e-13, -8.789534048848025e-13, 5.640032358879707e-13, -5.79080744870106e-15])
    assert len(err) == 2
    print(err)

    submit_status = submit('se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2', [9.99333333333113, 9.995000000003124, -1.170334631314455e-13, 0.045430924415662766, 1.5693232704196097e-13, 1.3309551235711984e-12, 7.033882924317932e-14, 9.144581536698287e-13, -8.789534048848025e-13, 5.640032358879707e-13, -5.79080744870106e-15])
    print(submit_status)
