from pathlib import Path
import requests
from bs4 import BeautifulSoup
import csv

if __name__ == '__main__':
    input_csv_path = Path("./list_person_all_extended_utf8.csv")
    output_csv_path = Path("./index.csv")

    if Path(output_csv_path).exists():
        Path(output_csv_path).unlink()

    with open(str(input_csv_path.resolve()), mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)

        with open(str(output_csv_path.resolve()), mode='a', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(header)

        for row in reader:
            r = requests.get(row[13])
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'lxml')
            # remove copyrighted works
            if soup.find('div', class_="copyright") != None:
                continue
            
            with open(str(output_csv_path.resolve()), mode='a', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(row)
