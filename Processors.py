import re
import spacy
def preprocess(text):
    text = re.sub(r'[^\w\s\']',' ', text)
    # Replace all the white spaces, punctuations with a single space
    text = re.sub(r'[ \n]+', ' ', text)
    if "'s" in text:
        text = text.replace(" 's", "'s", text.count("'s"))
        text = text[:-2]
    # Replace all multiple spaces and \n characters with a single space
    return text.strip().lower()


def lemmatize(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    l = []
    for word in doc:
        if word.is_punct:
            pass
        else:
            l.append(word.lemma_)
    return " ".join(l)
