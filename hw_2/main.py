from formatter import fmt_table, fmt_image
from pdflatex import PDFLaTeX


if __name__ == '__main__':
    l = [
        [1, 2, 3],
        ['4', '5', '6'],
        ['foo', True, None]
    ]
    tex = f'''
    \\documentclass{{article}}
    \\usepackage{{graphicx}}
    \\begin{{document}}
    {fmt_table(l)}
    {fmt_image('resources/plane.jpg')}
    \\end{{document}}
    '''

    with open('artifacts/output.tex', 'w') as f:
        print(tex, file=f)

    pdfl = PDFLaTeX.from_binarystring(tex.encode('utf-8'), 'artifacts/output')
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=False)
