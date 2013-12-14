#!/usr/bin/env python
'''
Merge together a pdf document containing only front pages with a separate
document containing only back pages and save the result into a new document.

@author: Matt Garriott
'''

import argparse
import os
from pyPdf import PdfFileReader, PdfFileWriter

def merge(fppath, bppath, outputpath, no_delete, fed_backwards):
  fpfile = PdfFileReader(open(fppath))
  bpfile = PdfFileReader(open(bppath))

  outputfile = PdfFileWriter()

  outputpages = []
  for i in range(fpfile.getNumPages()):
    backpages = True
    try:
      outputpages.append(fpfile.getPage(i))
      if backpages:
        if fed_backwards:
          print 'i = %d / backpage = %d' % (i, bpfile.getNumPages() - i - 1)
          outputpages.append(bpfile.getPage(bpfile.getNumPages() - i - 1))
        else:
          outputpages.append(bpfile.getPage(i))
    except IndexError:
      backpages = False

  if not no_delete:
    outputpages = [page for page in outputpages if page.extractText() != '']

  [outputfile.addPage(page) for page in outputpages]

  outputfile.write(open(os.path.expanduser(outputpath), 'w'))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Merge front and back pages located in separate ' +
                                                'PDF documents into one PDF document.')

  parser.add_argument('-f', '--front-pages', required=True,
                     help='The path to the PDF containing the front pages')
  parser.add_argument('-b', '--back-pages', required=True,
                     help='The path to the PDF containing the back pages')
  parser.add_argument('-o', '--output-file', default='~/Desktop/merged.pdf',
                     help='The path to save the completed pdf file, default is ~/Desktop/merged.pdf')
  parser.add_argument('-nd', '--no-delete', default=False, action='store_true',
                     help='Prevent blank pages from being deleted from the finished document.')
  parser.add_argument('--fed-backwards', default=False, action='store_true',
                     help='If you were lazy and fed the document in backwards on the seconds side, use this flag.')

  args = parser.parse_args()

  merge(args.front_pages, args.back_pages, args.output_file, args.no_delete, args.fed_backwards)


