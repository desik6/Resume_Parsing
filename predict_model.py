import spacy
from ML_pipeline import text_extractor

def predict(path):
    nlp=spacy.load("model")
    test_text=text_extractor.convert_pdf_to_text(path)
    for text in test_text:
        text=text.replace('\n',' ')
        doc=nlp(text)
        for ent in doc.ents:
            print(f'{ent.label_.upper():{30}}-{ent.text}')
            