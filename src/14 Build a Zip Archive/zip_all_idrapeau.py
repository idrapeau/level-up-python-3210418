import zipfile
import pathlib

def zip_all(input_directory, file_extensions, output_path):
  directory = pathlib.Path(input_directory)

  with zipfile.ZipFile(output_path, mode="w") as archive:
    for extension in file_extensions:
      glob_pattern = "*" + extension
      for file_path in directory.rglob(glob_pattern):
        archive.write(file_path, arcname=file_path.relative_to(directory))

  # Testing code
  '''
  with zipfile.ZipFile(output_path, mode="r") as archive:
    archive.printdir()
  '''


zip_all('src/14 Build a Zip Archive/my_stuff', ['.jpg', '.txt'], 
        'src/14 Build a Zip Archive/my_stuff.zip')