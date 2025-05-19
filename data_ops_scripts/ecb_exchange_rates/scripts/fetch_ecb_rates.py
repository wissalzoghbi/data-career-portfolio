#!/usr/bin/env python3
"""
fetch_ecb_rates.py
------------------
Downloads the ECB daily EUR exchange rates, extracts the date
plus USD, GBP, JPY, and prints them.

Next steps: save to CSV + logging.
"""
import csv
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET
import requests

ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
MAJORS = ["USD", "GBP", "JPY"]

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)
CSV_FILE = DATA_DIR / "exchange_rates.csv"

def fetch_xml(url: str) -> str:
    """Download the raw XML text from the ECB endpoint."""
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.text


def parse_rates(xml_text: str) -> tuple[datetime, dict]:
    """Return (date, {currency: rate}) parsed from ECB XML."""
    root = ET.fromstring(xml_text)

    namespace = {
        "gesmes": "http://www.gesmes.org/xml/2002-08-01",
        "eurofxref": "http://www.ecb.int/vocabulary/2002-08-01/eurofxref",
    }

    cube_daily = root.find(".//eurofxref:Cube/eurofxref:Cube", namespace)
    date_str = cube_daily.attrib["time"]

    rates = {child.attrib["currency"]: float(child.attrib["rate"])
             for child in cube_daily}

    return datetime.fromisoformat(date_str).date(), rates

def append_csv(date_val, rates_dict):
    """Append one row (date,rates) if date not already present."""
    header = ["date"] + MAJORS
    row    = [date_val.isoformat()] + [rates_dict[c] for c in MAJORS]

    # If file doesn't exist, write header + row
    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(row)
        return "created"

    # If date already recorded, do nothing
    with CSV_FILE.open("r", newline="") as f:
        existing_dates = {line.split(",")[0] for line in f.readlines()[1:]}
    if date_val.isoformat() in existing_dates:
        return "skipped"

    # Otherwise append
    with CSV_FILE.open("a", newline="") as f:
        csv.writer(f).writerow(row)
    return "appended"
def main() -> None:
    xml_text = fetch_xml(ECB_URL)
    date_val, rates = parse_rates(xml_text)

    print(f"ECB rates for {date_val}:")
    for cur in MAJORS:
        print(f"  1 EUR = {rates[cur]:.4f} {cur}")

    status = append_csv(date_val, rates)
    if status == "created":
        print(f"✅  Created {CSV_FILE.name} and wrote first row.")
    elif status == "appended":
        print(f"✅  Appended new row to {CSV_FILE.name}.")
    else:
        print(f"ℹ️  Rates for {date_val} already in {CSV_FILE.name}; no action.")

if __name__ == "__main__":
    main()