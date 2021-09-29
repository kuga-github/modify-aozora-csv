# modify-aozora-csv
Remove copyrighted books from the original book list of [Aozora Bunko](https://www.aozora.gr.jp).

## Getting started
### Requirements
* Python 3.x
* requests
* beautifulsoup4
### Run
```bash
python aozora.py
```
### File configuration
* `aozora.py`: source code to remove copyrighted books from the original book list
* `list_person_all_extended_utf8.csv`: original book list
* `index.csv`: modified book list

## License
* `aozora.py`: [MIT License](https://github.com/kuga-github/modify-aozora-csv/blob/main/LICENSE)
* `list_person_all_extended_utf8.csv`: (c) Aozora Bunko [(Licensed under CC BY 2.1 JP）](https://creativecommons.org/licenses/by/2.1/jp/deed.en)
* `index.csv`: Created by modifying `list_person_all_extended_utf8.csv` (c) Aozora Bunko [(Licensed under CC BY 2.1 JP）](https://creativecommons.org/licenses/by/2.1/jp/deed.en)
