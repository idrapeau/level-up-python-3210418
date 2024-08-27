import urllib.parse
import urllib.request
import re
import os

def download_files(sequence_url, output_directory):
  # Create the output directory if it does not already exist
  if not os.path.isdir(output_directory):
    os.makedirs(output_directory)

  url_components = sequence_url.split("/")
  base_url = sequence_url.partition(url_components[-1])[0]
  file_name_1 = url_components[-1]

  # Split the file name into the name and extension
  file_name_components = file_name_1.split(".")
  # Remove the numbers from the name
  file_name_components[0] = ''.join(re.findall(r'[a-zA-Z]+', file_name_components[0]))

  # Scan the url to find the names of the other files
  request_url = urllib.request.urlopen(base_url)
  request_url_txt = str(request_url.read())

  file_url = base_url + "/" + file_name_1
  file_path = output_directory + "/" + file_name_1

  try:
    urllib.request.urlretrieve(file_url, file_path)
  except:
    print("Download failed (likely due to an invalid file name or path)")
  else:
    # Remove the file name that was added to the list
    request_url_txt = request_url_txt.replace(file_name_1, "")

  while file_name_components[0] in request_url_txt:
    # Find a file name of the correct format and add it to the list
    start_index = request_url_txt.find(file_name_components[0])
    end_index = request_url_txt.find(file_name_components[1]) + len(file_name_components[1])
    file_name = request_url_txt[start_index:end_index]
    
    # Download the file to the specified output directory
    file_url = base_url + "/" + file_name
    file_path = output_directory + "/" + file_name

    try:
      urllib.request.urlretrieve(file_url, file_path)
    except:
      print("Download failed (likely due to an invalid file name or path)")
    else:
      # Remove the file name that was added to the list
      request_url_txt = request_url_txt.replace(file_name, "")



download_files('http://699340.youcanlearnit.net/image001.jpg', './images')