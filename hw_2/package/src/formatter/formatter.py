def fmt_table(l):
    h = len(l)
    w = len(l[0]) if l else 0

    q = ' \\\\ \n'.join([' & '.join(map(str, row)) for row in l])

    return f'''
    \\begin{{tabular}}{{{'c'.join(['|'] * (w + 1))}}}
        {q}
    \\end{{tabular}}
    '''


def fmt_image(filename):
    return f'''
    \\begin{{figure}}
        \\includegraphics[width=\\linewidth]{{{filename}}}
    \\end{{figure}}
    '''