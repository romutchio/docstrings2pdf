import sys
import ast
import ast_visitor
import os
from collections import namedtuple
from pdf_represent import PdfFormatter


def save_pdf(directory, name, pdf):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(directory + '/' + name + '.pdf', 'w', encoding='utf-8') as f:
        f.write(pdf)


class PDF:
    def __init__(self):
        self.module_name = ''

    def create_path(self, filename):
        self.module_name = filename
        return filename + '.py'

    def get_info_from_module(self, filename):
        filename = self.create_path(filename)
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
        except (FileNotFoundError, AttributeError):
            sys.stderr.write('No such module')
            sys.exit()
        tree = ast.parse(code)
        pdf_doc = PdfFormatter()
        module = ast_visitor.Module_Parser(self.module_name, tree)
        classes = module.module_info
        return pdf_doc.module_to_pdf(classes)


if __name__ == '__main__':
    module = sys.argv[1]
    pdf = PDF()
    pdf_res = pdf.get_info_from_module(module)
    save_pdf('results/', pdf.module_name, pdf_res)
    print('PDF has been created successfully.')



