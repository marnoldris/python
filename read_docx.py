
import docx

def get_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append('    ' + paragraph.text)
    return '\n\n'.join(full_text)
