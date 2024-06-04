import json

def save_dictionary(dictionary, output_path):
  with open(output_path, 'w') as output_file:
    json.dump(dictionary, output_file)

def load_dictionary(input_path):
  with open(input_path, 'r') as input_file:
    return json.load(input_file)
  
sample_dict = {1: 'a', 2: 'b', 3: 'c'}
save_dictionary(sample_dict, 'sample_dict.json')
retrieved_dict = load_dictionary('sample_dict.json')
print(retrieved_dict)
