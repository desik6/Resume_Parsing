import spacy
import re


def extract_name(string):
    r1=unicode(string)
    nlp=spacy.load("xx_ent_wiki_sm")
    doc=nlp(r1)
    for ent in doc.ents:
        if(ent.label_=="PER"):
            print(ent.text)
            break


def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

