# Third-party imports...
from nose.tools import assert_true
import requests
import json

# Deploeyed server testing
URL = "http://52.35.92.27:5000/api"

# Local testing
# URL = "http://localhost:5000/api"



def test_read_all():
    # Send a request to the API server and store the response.
    response = requests.get(URL + '/message')

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)


def test_read_one():
    # Send a request to the API server and store the response.
    response = requests.get(URL + '/message')

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)


def test_create():
    # Post a request to the API server and store the response.
    response = requests.post(URL + '/message', data=json.dumps({"id": 5, "message": "Hi New Message "}), headers={'Content-Type': 'application/json'})
    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)

# Run Terminal : nosetests --verbosity=2 tests