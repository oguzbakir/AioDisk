from __future__ import print_function

import os
import sys
from optparse import OptionParser

from googledrive import GoogleDrive

__version__ = "0.1"

parser = OptionParser()
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
parser.add_option("-m", "--mime",
                  action="store", dest="mimeoption", default=False,
                  help="Mime type search input Ex: image/jpeg for jpg/jpeg files")
parser.add_option("-n", "--name-search",
                  action="store", dest="filename", default=False,
                  help="Search only on file names")
parser.add_option("-f", "--full-text-search",
                  action="store", dest="fulltext", default=False,
                  help="Search in file and file names")
parser.add_option("-d", "--disk",
                  action="store", dest="disk", default=False,
                  help="Select a disk. Avaiable options: 'google-drive, mega'")

(options, args) = parser.parse_args()
DEFAULT_PAGE_SIZE_GOOGLE = 100


def checkGoogleAPI():
    if os.path.exists("client_secret.json"):
        return 1
    else:
        return 0


def main():
    gDrive = False
    mega = False
    if options.disk == "google-drive":
        # Show Google Drive Panel
        if not checkGoogleAPI():
            print("Google client_secret.json not found. Please check your configuration.")
            main()
        else:
            Drive = GoogleDrive()
            items = Drive.getWebContentLink(options.fulltext)
            for item in items:
                print('{0}&name={1}'.format(item['webContentLink'],item['name']))

    elif options.disk == "mega":
        # Show Mega Panel
        nothing = 1
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
