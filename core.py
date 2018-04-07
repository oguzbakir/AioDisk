from __future__ import print_function
import httplib2
import os
import sys
import json
import argparse

from optparse import OptionParser
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage




parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()


apiKeyTemplate = """{
    "yadisk" : {
        "application-id" : "",
        "application-secret" : "",
        "token" : ""
    }
}"""
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
global j


def initYadisk():
    global j
    if (os.path.exists("api_keys.json")):
        j = json.load(open("api_keys.json"))
    else:
        f = open("api_keys.json", "w")
        print(apiKeyTemplate, file=f)
        print("Api key file created. Please fill required fields and re-run script.")


def checkGoogleAPI():
    if (os.path.exists("client_secret.json")):
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
        credentials = tools.run_flow(flow, store)

        print('Storing credentials to ' + credential_path)
    return credentials


def main():
    gDrive = False
    yaDisk = False
    mega = False
    print("""Cloud Status:
    Google Drive: {0}
    Yandex Disk: {1}
    Mega: {2}
1- Show Google Drive Panel
2- Show Yandex Disk Panel
3- Show Mega Panel
""".format(gDrive,yaDisk,mega))
    choice = input("Please enter a number\n")
    if choice == "1":
        # Show Google Drive Panel
        if not checkGoogleAPI():
            print("Google client_secret.json not found. Please check your configuration.")
            main()
        else:
            print("I'm in")
    elif choice == "2":
        # Show Yandex Disk Panel
        nothing = 1
    elif choice == "3":
        # Show Mega Panel
        nothing = 1
    else:
        sys.exit(0)

    '''
    initYadisk()

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(fields="nextPageToken, files(id, name)",pageSize=10).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))
            '''


if __name__ == '__main__':
    main()

