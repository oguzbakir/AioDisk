import os

def checkGoogleAPI():
    if os.path.exists("client_secret.json"):
        return 1
    else:
        return 0

def test_google():
    assert checkGoogleAPI()
