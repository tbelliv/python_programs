import pandas as pd
import openpyxl

def convert_file(input_file, output_file):

  # Read Excel file
  df = pd.read_excel(input_file)  

  # Write to CSV file with UTF-8 encoding and BOM
  df.to_csv(output_file, index=False, encoding='utf-8-sig')

# Call function and pass both paths
convert_file(r"path.csv")
