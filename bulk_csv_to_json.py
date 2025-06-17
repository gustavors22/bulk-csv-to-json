#!/usr/bin/env python3
"""
csv2json_bulk.py

Converts all .csv files in a folder to .json
└── data/
    ├── sales.csv     ->  sales.json
    ├── customers.csv ->  customers.json
    └── products.csv  ->  products.json

Usage:
    python csv2json_bulk.py /path/to/csv_folder [--output /path/to/jsons]
"""
import csv
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any

def read_csv(path: Path, *, delimiter: str = ",") -> List[Dict[str, Any]]:
    """Reads a CSV and returns a list of dictionaries."""
    with path.open(newline="", encoding="latin1") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return list(reader)

def save_json(data: List[Dict[str, Any]], destination: Path) -> None:
    """Saves the list of dictionaries as a prettified JSON."""
    with destination.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def convert_csv_folder(input_folder: Path, output_folder: Path, delimiter: str = ",") -> None:
    """Processes all CSVs in `input_folder` and creates equivalent JSONs in `output_folder`."""
    if not input_folder.is_dir():
        raise ValueError(f"Folder not found: {input_folder}")
    output_folder.mkdir(parents=True, exist_ok=True)

    for csv_path in input_folder.glob("*.csv"):
        data = read_csv(csv_path, delimiter=delimiter)
        json_path = output_folder / f"{csv_path.stem}.json"
        save_json(data, json_path)
        print(f"✅  {csv_path.name} → {json_path.relative_to(output_folder.parent)}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Converts all CSV files in a folder to JSON.")
    parser.add_argument("csv_folder", type=Path, help="Folder containing the .csv files")
    parser.add_argument("--output", "-o", type=Path, help="Folder to save the JSON files (default: <csv_folder>/json)")
    parser.add_argument("--sep", "-s", default=",", help="CSV delimiter (default: ,)")
    args = parser.parse_args()

    input_folder = args.csv_folder
    output_folder = args.output or input_folder / "json"

    convert_csv_folder(input_folder, output_folder, delimiter=args.sep)

if __name__ == "__main__":
    main()
