# PDFMerger #

Ever had to scan a bunch of double sided papers? You end up with two separate
PDF files. One containing the front-sides of the pages, the other, the
back-sides.

PDFMerger allows you to merge these two files into a single PDF document.

## Dependencies ##

- Python 2.7+
- [PyPDF](https://pypi.python.org/pypi/PyPDF2/1.19)
- [Mock](https://pypi.python.org/pypi/mock/) (to run the test suite)

*Note PyPDF is NOT compatible with Python3, and consequently, neither is
PDFMerger*

You can easily install the dependencies using pip:

    pip install pyPdf

    # And if you want to run the tests
    pip install mock

If you are running multiple versions of python you may need to specify the
python2 version of pip: `pip-2.7`

## Usage ##

PDFMerger is command line tool. To run from it from the app's root directory:

    python2 src/merge.py --help

    usage: merge.py [-h] -f FRONT_PAGES -b BACK_PAGES [-o OUTPUT_FILE] [-nd]
                    [--fed-backwards]

    Merge front and back pages located in separate PDF documents into one PDF
    document.

    optional arguments:
      -h, --help            show this help message and exit
      -f FRONT_PAGES, --front-pages FRONT_PAGES
                            The path to the PDF containing the front pages
      -b BACK_PAGES, --back-pages BACK_PAGES
                            The path to the PDF containing the back pages
      -o OUTPUT_FILE, --output-file OUTPUT_FILE
                            The path to save the completed pdf file, default is
                            ~/Desktop/merged.pdf
      -nd, --no-delete      Prevent blank pages from being deleted from the
                            finished document.
      --fed-backwards       If you were lazy and fed the document in backwards on
                            the seconds side, use this flag.

### Fed Backwards ###

Running a group of pages through an automatic scanner has the side effect that
the pages end up in reverse order. Instead of manually reshuffling these
papers before scanning the back sides, you can scan the back pages just like
this and pass the `--fed-backwards` flag. The pages in the finalized document
will be placed in the correct order. Pretty neat, right?

## Running the Tests ##

If you'd like to run the test suite, ensure the `mock` dependency is
installed and execute the following from the app's root directory:

    python2 test/merge_test.py

## Contributing ##

If you are interested in contributing to PDFMerger please ensure your
commits follow a few simple guidelines.

- Write tests, both for new functionality and for bug fixes.
- Avoid trailing whitespace.
- Format commit messages in the imperative present tense.

## License ##

BSD 2-Clause (see LICENSE file).
