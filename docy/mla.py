import os
import re

import markdown
from weasyprint import CSS, HTML

from docy import basepath
from docy.extensions import MLAExtension
from docy.parse import parse


def convert_to_mla(md_filename):
    # Parse out the metadata
    metadata, mdtext = parse(md_filename)

    # Convert markdown to html
    html = markdown.markdown(
        mdtext, output_format="html5", extensions=[MLAExtension()])

    # Mess with style sheets
    css = re.sub(
        'INSERT_LAST_NAME', metadata['lastname'],
        open(os.path.join(basepath, 'css', 'mla.css'), 'r').read())

    # Render PDF
    HTML(string=html).write_pdf(
        re.sub('\.\w+$', '.pdf', md_filename),
        stylesheets=[
            os.path.join(basepath, 'css', 'reset.css'),
            CSS(string=css)])
