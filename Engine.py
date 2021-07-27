from ML_pipeline import json_spacy
from ML_pipeline import text_extractor
from ML_pipeline import train_model
from ML_pipeline import predict_model
from ML_pipeline import utils


train=json_spacy.convert_data_to_spacy("C:\Program Files\Entity_Recognition_in_Resumes.json")

print("Done. Converted into spacy format")

print("Checking if previously built spacy model exists. If not, we will train a new one")
test_text=text_extractor.convert_pdf_to_text("D:\Downloads\Resume_Parser_Code_Data\Resume_Parser\output\Alice_Clark_CV.pdf")
model=utils.check_existing_model("nlp_model")

model=train_model.build_spacy_model(train,model)

predict_model.predict("D:\Downloads\Resume_Parser_Code_Data\Resume_Parser\output\Alice_Clark_CV.pdf")
mine = text_extractor.convert_pdf_to_text('D:\Downloads\Resume_Parser_Code_Data\Resume_Parser\output\Alice_Clark_CV.pdf')
print(mine)
print(test_text)
