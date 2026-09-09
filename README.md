# Python CSV Handling Examples

A collection of small Python scripts demonstrating how to read, write, and manipulate CSV files using Python's built-in `csv` module. Each script focuses on a specific CSV operation, making this a useful reference for common CSV handling patterns.

## 📁 Project Structure

```
python/
├── create_csv_file.py           # Create a CSV file from a list of dictionaries
├── read_csv_file.py             # Read and print CSV file contents
├── row_selection_csv.py         # Select specific rows from a CSV
├── column_selection_csv.py      # Select specific columns from a CSV
├── row_col_selection_csv.py     # Select specific rows and columns together
├── csv_dict_reading.py          # Read CSV files using DictReader
├── csv_to_csv_writing.py        # Copy/write data from one CSV to another
├── csv_to_csv_selective_writing.py  # Write selected columns to a new CSV
├── csv_to_csv_writing_dict.py   # Copy CSV data using DictReader/DictWriter
├── Data.csv                     # Sample source data
├── Dict_Data.csv                # Output from dict-based writing
├── New_Data.csv                 # Output from csv_to_csv_writing.py
└── New_Data_2.csv                # Output from csv_to_csv_selective_writing.py
```

## 📋 Requirements

- Python 3.9+
- No external dependencies — uses only the built-in `csv` module

## 🚀 Usage

Each script can be run independently:

```bash
python create_csv_file.py
python read_csv_file.py
python row_selection_csv.py
python column_selection_csv.py
python row_col_selection_csv.py
python csv_dict_reading
python csv_to_csv_writing.py
python csv_to_csv_selective_writing.py
python csv_to_csv_writing_dict.py
```

Make sure `Data.csv` exists in the same directory before running scripts that depend on it (`create_csv_file.py` generates it).

## 📖 Script Details

### `create_csv_file.py`
Creates `Data.csv` from a list of dictionaries using `csv.DictWriter`, writing a header row followed by the data rows.

### `read_csv_file.py`
Reads `Data.csv` using `csv.reader` and prints each row. Demonstrates optional reader parameters like `skipinitialspace` and `quoting`.

### `row_selection_csv.py`
Reads all rows into a list, then selects and prints a specific slice of rows (e.g., rows 2–4).

### `column_selection_csv.py`
Reads each row and prints only a slice of columns (e.g., the first 3 columns).

### `row_col_selection_csv.py`
Combines row and column selection — filters to specific rows, then slices columns within those rows.

### `csv_dict_reading`
Reads `Data.csv` using `csv.DictReader`, allowing access to fields by column name instead of index.

### `csv_to_csv_writing.py`
Reads from `Data.csv` and writes rows to `New_Data.csv`, demonstrating two different methods of writing rows (`writerows` vs. looping with `writerow`).

### `csv_to_csv_selective_writing.py`
Reads from `Data.csv` and writes only selected columns to `New_Data_2.csv`.

### `csv_to_csv_writing_dict.py`

Reads `Data.csv` with `DictReader` and writes it to `Dict_Data.csv` using `DictWriter`.

## 💡 Sample Data

`Data.csv` contains sample records with the following fields:

```
Name, Age, Skill, hobby
```

## 📝 Notes

This project is intended as a learning reference for Python's `csv` module — covering reading, writing, filtering rows/columns, and working with both `reader`/`writer` and `DictReader`/`DictWriter` interfaces.

## 📄 License

Free to use for learning and reference purposes.