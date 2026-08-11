import os
from pypdf import PdfReader
files = [
    r'c:\Users\jon_e\Desktop\OCSweb\RECURSOS\GUIAS\GUÍAS\ESPAÑOL\ESPAÑOL.pdf',
    r'c:\Users\jon_e\Desktop\OCSweb\RECURSOS\GUIAS\GUÍAS\FÍSICA\FÍSICA.pdf',
    r'c:\Users\jon_e\Desktop\OCSweb\RECURSOS\GUIAS\GUÍAS\MATEMATICAS\DOC-20260417-WA0322..pdf',
    r'c:\Users\jon_e\Desktop\OCSweb\RECURSOS\GUIAS\GUÍAS\LITERATURA\LITERATURA.pdf',
    r'c:\Users\jon_e\Desktop\OCSweb\RECURSOS\GUIAS\GUÍAS\GEOGRAFÍA\GEOGRAFÍA.pdf',
    r'c:\Users\jon_e\Desktop\OCSweb\RECURSOS\GUIAS\GUÍAS\BIOLOGÍA\BIOLOGÍA.pdf',
    r'c:\Users\jon_e\Desktop\OCSweb\RECURSOS\GUIAS\GUÍAS\QUÍMICA\QUÍMICA.pdf',
    r'c:\Users\jon_e\Desktop\OCSweb\RECURSOS\GUIAS\GUÍAS\HISTORIA UNIVERSAL\HISTORIA UNIVERSAL.pdf',
    r'c:\Users\jon_e\Desktop\OCSweb\RECURSOS\GUIAS\GUÍAS\HISTORIA UNIVERSAL\HISTORIA DE MÉXICO.pdf',
]
for path in files:
    print('===', os.path.basename(path), '===')
    try:
        reader = PdfReader(path)
        print('PAGES', len(reader.pages))
        text = '\n'.join(page.extract_text() or '' for page in reader.pages[:4])
        print(text[:12000])
    except Exception as e:
        print('ERR', e)
    print('\n')
