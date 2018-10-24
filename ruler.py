#!/usr/bin/python3.6

import sys, getopt

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print ('-i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        # help option
        if opt == '-h':
            print ('Ruler for Script files.')
            print ('-i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    ruler(inputfile)

def ruler(ipf):
    
    with open(ipf) as f:
        first_line = f.readline()

    top = []
    top_out = []
    bottom = []

    length = len(first_line)
    for i in range(length):
        # splits the number into top list and bottom list
        top.append((i+1)//10)
        bottom.append((i+1)%10)

    for i in range(length):
        if ((i+1)//10) == 0:
            # all one digits equal to zero
            top_out.append(" ")
        elif (((i+1)//10) in list(sorted(set(top)))) and (((i+1)//10) not in top_out):
            # only the first second-digit is printed to the top_out list
            top_out.append(((i+1)//10))
        else:
            # rest will be printed as space
            top_out.append(" ")

    print (''.join(list(map(str, top_out))))
    print (''.join(list(map(str,bottom))))
    print (first_line)
    
if __name__ == "__main__":
   main(sys.argv[1:])
