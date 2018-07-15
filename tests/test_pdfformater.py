import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))
import pdfformater

class TestPdfFormatter(unittest.TestCase):

    def test_replace_spec_symbols(self):
        result = pdfformater.replace_spec_symbols('(Hello world)')
        self.assertEqual(result, '\\(Hello world\\)')

    def test_to_head(self):
        result = pdfformater.to_head('Some text to head', 40)
        self.assertEqual(result, '\n/Helv-Bold 15 Tf\n0 -25 Td\n0.3254 0.2196 0.478 rg\n(Some text to head) Tj\n')

    def test_to_class(self):
        result = pdfformater.to_class('Some text to class', 40)
        self.assertEqual(result, '\n/Helv-Bold 15 Tf\n0 -25 Td\n0.505 0.349 0.713 rg\n(Some text to class) Tj\n')

    def test_to_subhead(self):
        result = pdfformater.to_subhead('Some text to subhead', 40)
        self.assertEqual(result, '\n/Helv-Bold 12 Tf\n0.6 0.4588 0.7882 rg\n40 -25 Td\n(Some text to subhead) Tj\n')

    def test_to_page_description(self):
        result = pdfformater.to_page_description('Some text to description', 40)
        self.assertEqual(result, '\n/Helv-Italic 12 Tf\n40 20 Td\n(Some text to description) Tj\n')


    def test_to_text(self):
        single = pdfformater.to_page_description('Single string', 40)
        two = pdfformater.to_page_description('First string\nSecond string', 40)
        self.assertEqual(single, '\n/Helv-Italic 12 Tf\n40 20 Td\n(Single string) Tj\n')
        self.assertEqual(two, '\n/Helv-Italic 12 Tf\n40 20 Td\n(First string\nSecond string) Tj\n')

    def test_to_page(self):
        self.maxDiff = None
        result = pdfformater.to_page('Hello world')
        expect ='''%PDF-1.2
%вгПУ

1 0 obj
<<
	/Type /Catalog
	/Pages 2 0 R
>>
endobj

2 0 obj
<<
	/Type /Pages
	/Kids [3 0 R]
	/Count 1
>>
endobj

3 0 obj
<<
	/Type /Page
	/Parent 2 0 R
	/Resources
	<<
		/Font
		<<
			/Helv
			<<
				/Type /Font
				/Subtype /Type1
				/BaseFont /Helvetica
			>>
			/Helv-Bold
			<<
				/Type /Font
				/Subtype /Type1
				/BaseFont /Helvetica-Bold
			>>
			/Helv-Italic
			<<
				/Type /Font
				/Subtype /Type1
				/BaseFont /Helvetica-Oblique
			>>
		>>
	>>
	/MediaBox [0 0 600 45]
	/Contents 4 0 R
>>
endobj

4 0 obj <</Length 20>> stream
BT
Hello world
ET
endstream endobj
xref
0 5
0000000000 65535 f
0000000015 00000 n
0000000064 00000 n
0000000121 00000 n
0000000433 00000 n
trailer
<<
    /Root 1 0 R
    /Size 5
>>
startxref
506
%%EOF'''
        self.assertEqual(result, expect)

    def test_get_page_height(self):
        text = '''hello
        world
        and
        person
        who
        is
        reading
        it
        just
        at
        this
        particular
        moment'''
        result = pdfformater.get_page_height(text)
        self.assertEqual(result, 95)
