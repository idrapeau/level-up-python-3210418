import urllib.parse
import urllib.request
import re

def download_files(sequence_url, output_directory):
  url_components = sequence_url.split("/")

  #print(url_components)

  base_url = sequence_url.partition(url_components[-1])[0]

  #print(base_url)

  file_name_1 = url_components[-1]
  print(file_name_1)

  # Split the file name into the name and extension
  file_name_components = file_name_1.split(".")
  print(file_name_components)
  # Remove the numbers from the name
  file_name_components[0] = ''.join(re.findall(r'[a-zA-Z]+', file_name_components[0]))
  print(file_name_components)

  # Initialize a list of file names
  file_name_list = [file_name_1]

  #file_path = output_directory + "/" + file_name
  #print(file_path)

  # All of the file names are printed here
  request_url = urllib.request.urlopen(base_url)
  request_url_txt = request_url.read()
  request_url_txt = str(request_url_txt)
  #print(request_url_txt)

  request_url_txt = request_url_txt.replace(file_name_1, "")

  while file_name_components[0] in request_url_txt:
    # Find a file name of the correct format and add it to the list
    start_index = request_url_txt.find(file_name_components[0])
    end_index = request_url_txt.find(file_name_components[1]) + 3
    next_file_name = request_url_txt[start_index:end_index]
    file_name_list.append(next_file_name)

    # I might want to verify that this has found a valid file name

    # Remove the file name that was added to the list
    request_url_txt = request_url_txt.replace(next_file_name, "")

  # Download all files on the list
  # TODO: Download the files to the specified output directory
  for file_name in file_name_list:
    file_url = base_url + "/" + file_name
    urllib.request.urlretrieve(file_url, file_name)



download_files('http://699340.youcanlearnit.net/image001.jpg', './images')