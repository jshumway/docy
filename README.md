Docy
====

Transform markdown to MLA PDFs.

Architecture
------------

To transform markdown into a formatted PDF, the raw markdown is converted to html using any needed modifications to a markdown parser. This html is paired with the appropriate stylesheets and passed to a converter that renders it to a PDF. Finally, some post-processing is applied to the PDF as needed.

The specific extensions to the markdown parser, the stylesheets applied to the html, and the post-processing functions are all determined by a configuration object that is created from command line arguments and other options.
