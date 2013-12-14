import unittest, pyPdf, sys, os.path
from mock import Mock

SRC = os.path.join(os.path.dirname(__file__), '..', 'src')
sys.path.append(SRC)
import merge

class MockPdfReader:
  def __init__(self, pages=([None] * 3)):
    self.pages = pages

  def getNumPages(self):
    return len(self.pages)

  def getPage(self, page_num):
    return self.pages[page_num]

class MockPdfWriter:
  def __init__(self):
    self.pages = []

  def write(self, a_file): pass

  def addPage(self, page): self.pages.append(page)

class MockPage:
  def __init__(self, text=''):
    self.text = text

  def extractText(self): return self.text

class MergeTest(unittest.TestCase):
  def setUp(self):
    def side_effect(arg, *args): return(arg)

    # Stub the global open method inside the merge module
    merge.open = Mock(side_effect=side_effect)

    merge.PdfFileReader = Mock(side_effect=side_effect)

    # Create a pdf writer and add a handle to self
    def create_writer():
      self.outfile = MockPdfWriter()
      return self.outfile

    merge.PdfFileWriter = Mock(side_effect=create_writer)

  def test_merged_file_contains_all_pages(self):
    front_pages = MockPdfReader()
    back_pages = MockPdfReader()

    merge.merge(front_pages, back_pages, 'fake_out', True, False)

    expected_len = len(front_pages.pages) + len(back_pages.pages)
    self.assertEqual(expected_len, len(self.outfile.pages))

  def test_merged_file_contains_pages_in_correct_order(self):
    pass

  def test_merging_removes_blank_pages(self):
    front_pages = MockPdfReader([MockPage('not_blank'), MockPage()])
    back_pages = MockPdfReader([MockPage(), MockPage('not_blank')])

    merge.merge(front_pages, back_pages, 'fake_out', False, False)
    self.assertEqual(2, len(self.outfile.pages))

if __name__ == '__main__':
  unittest.main()
