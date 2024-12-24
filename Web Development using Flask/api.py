import nlpcloud

API_key = "9c5cf1ed8cac67afac0506ac52cda89fb6de4cc9"

def NER(input,entity):
    client = nlpcloud.Client("finetuned-llama-3-70b", 
                         API_key, 
                         gpu=True)
    response = client.entities(input,searched_entity=entity)
    return response
