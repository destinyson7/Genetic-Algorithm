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

    err = get_errors('se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2', [-1.0514621416531283e-12, 8.512477622724045, 3.060450949278663e-13, 0.04933903144709126, 3.6090897828431077e-13, 1.4272193190449243e-12, 3.575898426563937e-13, 1.1897388833614035e-12, 0.0, 6.716119879538675e-13, -7.719253852496137e-15])
    assert len(err) == 2
    print(err)

    submit_status = submit('se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2', [-1.0514621416531283e-12, 8.512477622724045, 3.060450949278663e-13, 0.04933903144709126, 3.6090897828431077e-13, 1.4272193190449243e-12, 3.575898426563937e-13, 1.1897388833614035e-12, 0.0, 6.716119879538675e-13, -7.719253852496137e-15])
    print(submit_status)
