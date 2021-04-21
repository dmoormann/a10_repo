import yaml

with open(r'./mylist.yml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
#    fruits_list = yaml.load(file, Loader=yaml.FullLoader)
    documents = yaml.full_load(file)

    for item, doc in documents.items():
        print(item, ":", doc)
#    print(fruits_list)
