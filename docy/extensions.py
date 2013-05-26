from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree


class MLAExtension(Extension):
    """ Transform to html appropriate for generating an MLA document. """
    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        md.treeprocessors.add(
            "mlaheading", MLAHeadingProcessor(self), '_begin')


class MLAHeadingProcessor(Treeprocessor):
    """ Convert the leading lines of markdown into an MLA heading.

    All elements before the first h1 tag are grouped together then added to a
    <div class="heading"> element as paragraph elements.
    """

    def run(self, root):
        lines = []

        for i, element in enumerate(root):
            if element.tag == 'h1':
                break

            lines.extend(element.text.split('\n'))

        del root[:i]
        heading = etree.Element('div', {'class': 'heading'})

        for line in lines:
            elem = etree.Element('p')
            elem.text = line
            heading.append(elem)

        root.insert(0, heading)
