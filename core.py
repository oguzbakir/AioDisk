from __future__ import print_function
import httplib2
import os
import json

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

apiKeyTemplate = """{
    "yadisk" : {
        "application-id" : "4eb072432c9d4113a09a830e29abc329",
        "application-secret" : "f25f6031d2794fb5ad8f2be60e6ddcbe",
        "token" : ""
    }
}"""
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
global j

def initYadisk():
    if(os.path.exists("api_keys.json")):
        j = json.load(open("api_keys.json"))
    else:
        f = open("api_keys.json","w")
        print(apiKeyTemplate,file=f)
        print("Api key file created. Please fill required fields and re-run script.")

def checkGoogleAPI():
    if(os.path.exists("client_secret.json")):
        return 1
    else:
        return 0

def get_credentials():
    
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    initYadisk()
    
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))

if __name__ == '__main__':
    if checkGoogleAPI() == 1:
        main()
    else:
        print("client_secret.json file not found")
