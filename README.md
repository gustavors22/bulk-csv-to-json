# CSV to JSON Bulk Converter

This script converts all `.csv` files in a folder to `.json` files with the same names.

## How to Run

1. **Ensure you have Python 3 installed.**

2. **Open a terminal in the project directory.**

3. **Run the script with:**
   ```sh
   python bulk_csv_to_json.py <csv_folder> [--output <output_folder>] [--sep <separator>]

* <csv_folder>: Path to the folder containing your .csv files.
* --output or -o: (Optional) Path to the output folder for .json files. Defaults to a json subfolder inside <csv_folder>.
* --sep or -s: (Optional) CSV separator character. Default is ,.

## Example
Convert all CSVs in the data folder and save JSONs in a json subfolder:

python bulk_csv_to_json.py data

Specify a custom output folder and separator:

python bulk_csv_to_json.py data --output results --sep ";"

## Output
For each file.csv in the input folder, a file.json will be created in the output folder.
