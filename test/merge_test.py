import unittest, pyPdf, sys, os.path
from mock import Mock

SRC = os.path.join(os.path.dirname(__file__), '..', 'src')
sys.path.append(SRC)
import merge

class MockPdfReader:
  def __init__(self):
    self.pages = [None] * 3

  def getNumPages(self):
    return len(self.pages)

  def getPage(self, page_num): pass

class MockPdfWriter:
  def __init__(self):
    self.pages = []

  def write(self, a_file): pass

  def addPage(self, page): self.pages.append(page)

class MergeTest(unittest.TestCase):
  def setUp(self):
    # Stub the global open method inside the merge module
    merge.open = Mock(return_value=True)

    self.front_pages = MockPdfReader()
    self.back_pages = MockPdfReader()
    self.outfile = MockPdfWriter()

    merge.PdfFileReader = Mock(side_effect=[self.front_pages, self.back_pages])
    merge.PdfFileWriter = Mock(return_value=self.outfile)

  def test_merged_file_contains_all_pages(self):
    merge.merge('fake_doc1', 'fake_doc2', 'fake_out', True, False)

    expected_len = len(self.front_pages.pages) + len(self.back_pages.pages)
    self.assertEqual(expected_len, len(self.outfile.pages))

if __name__ == '__main__':
  unittest.main()
