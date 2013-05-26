import re


def parse(md_filename):
    """ Seperate metadata from the markdown content of a file.

    Returns the metadata as a dictionary as the first value and a string of the
    remaining markdown as the second argument. The newline after the metadata
    is not included in the second value.
    """

    parse_error = (
        "Error parsing line %d '%s'\nCould not determine key: value pair. "
        "Metadata is improperly formatted, or missing. In the second case, "
        "the file must begin with a blank line.")

    metadata = {}
    md = []

    done = False
    with open(md_filename, 'r') as raw:
        for i, line in enumerate(raw.readlines()):
            if line == '\n' and not done:
                done = True
            elif done:
                md.append(line)
            else:
                match = re.match(r'(?P<key>\S+): (?P<value>.+)$', line)

                if match:
                    metadata[match.group('key')] = match.group('value')
                else:
                    print parse_error % (i + 1, line[:-1])
                    exit()

    return metadata, ''.join(md)
