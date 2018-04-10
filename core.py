from __future__ import print_function

import os
import sys
from optparse import OptionParser

from GoogleDrive import GoogleDrive

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

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
    print("""Cloud Status:
    Google Drive: {0}
    Mega: {1}
1- Show Google Drive Panel
2- Show Mega Panel
""".format(gDrive, mega))
    choice = input("Please enter a number\n")
    if choice == "1":
        # Show Google Drive Panel
        if not checkGoogleAPI():
            print("Google client_secret.json not found. Please check your configuration.")
            main()
        else:
            Drive = GoogleDrive()
            items = Drive.getLastItems(DEFAULT_PAGE_SIZE_GOOGLE)
            print('Files:')
            for item in items:
                print('{0} ({1})'.format(item['name'], item['id']))

    elif choice == "2":
        # Show Mega Panel
        nothing = 1
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
