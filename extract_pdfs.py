import os
from pypdf import PdfReader
base = r'c:\Users\jon_e\Desktop\OCSweb\RECURSOS\GUIAS\GUÍAS'
for root, dirs, files in os.walk(base):
    for f in files:
        if not f.lower().endswith('.pdf'):
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, base)
        try:
            reader = PdfReader(path)
            print('FILE:', rel)
            print('PAGES:', len(reader.pages))
            text = ''
            for i, page in enumerate(reader.pages[:8]):
                t = page.extract_text() or ''
                text += f'\n--- PAGE {i+1} ---\n{t}'
            print(text[:8000])
            print('\n==== END ====' )
        except Exception as e:
            print('ERR', rel, e)
            print('\n==== END ====' )
