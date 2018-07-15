import unittest
import ast
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))
from pdf_represent import PdfFormatter
import doc2pdf
import ast_visitor

class TestPdfRepresent(unittest.TestCase):
    def test_module_to_pdf(self):
        self.maxDiff = None
        code='''class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart'''
        expect = '''%PDF-1.2
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
	/MediaBox [0 0 600 195]
	/Contents 4 0 R
>>
endobj

4 0 obj <</Length 481>> stream
BT

/Helv-Italic 12 Tf
40 175 Td
(Docstrings to complex module) Tj

/Helv-Bold 15 Tf
0 -25 Td
0.3254 0.2196 0.478 rg
(NAME) Tj

/Helv-Bold 12 Tf
0.6 0.4588 0.7882 rg
40 -25 Td
(complex) Tj

/Helv-Bold 15 Tf
-40 -25 Td
0.3254 0.2196 0.478 rg
(CLASSES) Tj

/Helv-Bold 15 Tf
40 -25 Td
0.505 0.349 0.713 rg
(class Complex) Tj

/Helv-Bold 12 Tf
0.6 0.4588 0.7882 rg
40 -25 Td
(METHODS:) Tj

/Helv-Bold 12 Tf
0.6 0.4588 0.7882 rg
0 -25 Td
(__init__\(self, realpart, imagpart\)) Tj

ET
endstream endobj
xref
0 5
0000000000 65535 f
0000000015 00000 n
0000000064 00000 n
0000000121 00000 n
0000000434 00000 n
trailer
<<
    /Root 1 0 R
    /Size 5
>>
startxref
969
%%EOF'''
        tree = ast.parse(code)
        module = ast_visitor.Module_Parser('complex', tree)
        classes = module.module_info
        pdf = PdfFormatter()
        result = pdf.module_to_pdf(classes)

        self.assertEqual(result, expect)

