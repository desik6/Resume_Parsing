import json
import os
import logging




def convert_data_to_spacy(JSON_file_path):
    try:
        training_data=[]
        lines=[]
        with open(JSON_file_path,"r",encoding="utf-8") as f:
            lines=f.readlines()

        for line in lines:
            data=json.loads(line)
            text=data["content"]
            entities=[]
            for annotation in data["annotation"]:
                point=annotation["points"][0]
                labels=annotation["label"]
                if not isinstance(labels,list):
                    labels=[labels]

                for label in labels:
                    entities.append((point["start"],point["end"]+1,label))

            training_data.append((text, {"entity": entities}))

        return training_data
    except Exception as e:
        logging.exception("Unable to process"+JSON_file_path+"\n"+"error="+str(e))
        return None