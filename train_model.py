import spacy
import  random
from spacy.util import minibatch,compounding

def build_spacy_model(train,model):
    if model is not None:
        nlp=spacy.load(model)
        print("Loaded Model '%s'" %model)


    else:
        nlp=spacy.blank("en")
        print("Created blank 'en' model")

    TRAIN_DATA =train
    if 'ner' not in nlp.pipe_names:
        ner=nlp.create_pipe("ner")
        nlp.add_pipe("ner",last=True)

    else:
        nr=nlp.get_pipe("ner")


    for _, annotation in  TRAIN_DATA:
        for ent in annotation.get("entity"):
            ner.add_label(ent[2])

    other_pipes=[pipe for pipe in nlp.pipe_names if pipe!="ner"]
    with nlp.disable_pipes(*other_pipes):
        if model is None:
            optimizer=nlp.begin_training()
        for i in range(2):
            print("Starting iteration"+ str(i))
            random.shuffle(TRAIN_DATA)
            losses={}
            for text, annotation in  TRAIN_DATA:
                try:
                    nlp.update([text],
                               [annotation],
                               drop=0.2,
                               sgd=optimizer,
                               losses=losses)
                except Exception as e:
                    pass
            print(losses)

    nlp.to_disk("model")
    return nlp