#!/usr/bin/python
import download_random
import sys, getopt, os

from os.path import expanduser
from subprocess import call

home = expanduser("~")
background_dir = home + "/.unsplash_background/"
if not os.path.exists(background_dir):
    os.mkdir( background_dir, 0700 )
background_output = background_dir + "current.jpg"

def usage():
    print 'Usage: g_random_background.py -w <width> -h <height>'

def main(argv):
    width = ''
    height = ''
    output = ''
    try:
        opts, args = getopt.getopt(argv, "?w:h:",["help","width=", "height="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-?", "--help"):
            usage()
            sys.exit()
        elif opt in ("-w", "--width"):
            width = arg
        elif opt in ("-h", "--height"):
            height = arg
    update_background(width, height)

def update_background(width, height):
    download_random.download(width,height,background_output)
    call([
        "gsettings",
        "set",
        "org.gnome.desktop.background",
        "picture-uri",
        "file://" + background_output])

if __name__ == "__main__":
    main(sys.argv[1:])
