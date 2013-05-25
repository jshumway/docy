#!/usr/bin/env python

import markdown

from extensions import MLAExtension


def main(argv):
    html = markdown.markdown(
        open(argv[1], 'r').read(), output_format="html5",
        extensions=[MLAExtension()])

    print html

if __name__ == '__main__':
    import sys
    main(sys.argv)
