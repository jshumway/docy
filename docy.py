#!/usr/bin/env python

from docy import convert_to_mla


def main(argv):
    convert_to_mla(argv[1])

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print "Error: one argument required."
    else:
        main(sys.argv)
