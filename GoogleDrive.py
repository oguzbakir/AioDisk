import os
import io
import httplib2
import mimetypes

from apiclient import discovery
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'


class GoogleDrive:

    def __init__(self):
        self.credentials = self.getCredientials()
        self.http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', http=self.http)


    def getCredientials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'aiodisk.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            credentials = tools.run_flow(flow, store)

            print('Storing credentials to ' + credential_path)
        return credentials

    def getLastItems(self, size):
        results = self.service.files().list(
            pageSize=size, spaces='drive', fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        return items

    def searchWithMimeType(self, mimeString):
        results = self.service.files().list(q="mimeType='" + mimeString + "'",
                                              spaces='drive',
                                              fields='nextPageToken, files(id, name)',
                                              pageToken=None).execute()
        items = results.get('files', [])
        return items

    def searchWithName(self, nameString):
        results = self.service.files().list(q="name contains '" + nameString + "'",
                                            spaces='drive',
                                            fields='nextPageToken, files(id, name)',
                                            pageToken=None).execute()
        items = results.get('files', [])
        return items

    def searchWithFullText(self, fullTextString):
        results = self.service.files().list(q="fullText contains '" + fullTextString + "'",
                                            spaces='drive',
                                            fields='nextPageToken, files(id, name)',
                                            pageToken=None).execute()
        items = results.get('files', [])
        return items

    def getWebContentLink(self, nameString):
        results = self.service.files().list(q="fullText contains '" + nameString + "'",
                                            spaces='drive',
                                            fields='nextPageToken, files(webContentLink,name)',
                                            pageToken=None).execute()
        items = results.get('files', [])
        return items








