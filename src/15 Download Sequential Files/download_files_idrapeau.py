import urllib.parse
import urllib.request

def download_files(sequence_url, output_directory):
  url_components = urllib.parse.urlparse(sequence_url)
  input_path = url_components.path

  url_components_2 = sequence_url.split("/")

  #print(url_components_2)

  base_url = sequence_url.partition(url_components_2[-1])[0]

  #print(base_url)

  # All of the file names are printed here
  request_url_1 = urllib.request.urlopen(base_url)
  print(request_url_1.read())

  #request_url = urllib.request.urlopen(sequence_url)
  #print(request_url.read())
  #urllib.request.urlretrive(sequence_url, output_directory)
  #print(url_components)



download_files('http://699340.youcanlearnit.net/image001.jpg', './images')