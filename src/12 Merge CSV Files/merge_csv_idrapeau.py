import csv

def merge_csv(input_list, output_file):
  merged_field_names = []
  merged_entries = []
  first_row = True

  for file_name in input_list:
    with open(file_name, mode='r') as input_file:
      csv_reader = csv.DictReader(input_file)
      for row in csv_reader:
        # Add all field names to the merged field list if they aren't there already
        if first_row:
          field_names = ",".join(row)
          field_names = field_names.split(",")
          for name in field_names:
            if name not in merged_field_names:
              merged_field_names.append(name)
          first_row = False
        # Add each entry to the merged entry list
        merged_entries.append(row)
    input_file.close()
    # Reset first_row for the next file
    first_row = True

  # Write the merged lists to a csv file
  with open(output_file, mode='w') as merged_output:
    output_writer = csv.DictWriter(merged_output, fieldnames = merged_field_names)

    output_writer.writeheader()
    for output_row in merged_entries:
      output_writer.writerow(output_row)


if __name__ == '__main__':
  merge_csv(['src/12 Merge CSV Files/class1.csv', 'src/12 Merge CSV Files/class2.csv'],
             'src/12 Merge CSV Files/all_students.csv')