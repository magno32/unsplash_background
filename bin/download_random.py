#!/usr/bin/python
import urllib2
import sys, getopt

def usage():
    print 'Usage: download_random.py -w <width> -h <height> -o <output>'

def main(argv):
    width = ''
    height = ''
    output = ''
    try:
        opts, args = getopt.getopt(argv, "?w:h:o:",["help","output=","width=", "height="])
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
        elif opt in ("-o", "--output"):
            output = arg
    download(width, height, output)

def download(width, height, output):
    response = urllib2.urlopen("https://unsplash.it/" + width + "/" + height + "?random")
    #Download the file
    file_size_dl = 0
    block_size = 8192
    f = open(output,"wb")
    while True:
        buffer = response.read(block_size)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
