Docy
====

Transform markdown to MLA PDFs.

Architecture
------------

To transform markdown into a formatted PDF, the raw markdown is converted to html using any needed modifications to a markdown parser. This html is paired with the appropriate stylesheets and passed to a converter that renders it to a PDF. Finally, some post-processing is applied to the PDF as needed.

The specific extensions to the markdown parser, the stylesheets applied to the html, and the post-processing functions are all determined by a configuration object that is created from command line arguments and other options.

Style
-----

All code in the docy repository is [Pep8](http://www.python.org/dev/peps/pep-0008/) compliant. All code passes the [PyFlakes](https://pypi.python.org/pypi/pyflakes) static code checker without warning.
`pep8 docy` and `pyflakes docy` should have **zero** output. If non-compliant code is commited (code that generates output for either of the two command above), you will be mocked.
