# Chinese Zodiac Test
![test workflow](https://github.com/jachurchill/chinese-zodiac/actions/workflows/test-and-coverage.yml/badge.svg)
![coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/jachurchill/2be2fd8265d0df1ada2565f4e7456a8c/raw/covbadge.json)

Chinese Zodaic Test is an example of automated testing on a simple program that calculates the Chinese zodiac year given a Gregorian calendar year. As this is to be an example of automated testing and coverage, the tests written in pytest as well as a coverage report generated with coverage.py are run with a [GitHub action](https://github.com/jachurchill/chinese-zodiac-test/actions/workflows/python-app.yml).
For clearer presentation the action badge is displayed here to show the success of the workflow including the tests. Further the workflow will generate a coverage badge based on the results of the coverage report.

## Instalation

Checkout the repository from github and install the requirements using pip

```bash
git clone https://github.com/jachurchill/chinese-zodiac-test.git
pip install -r requirements.txt
```

## Usage

To run the program run the main python file.

```bash
python3 chinese_zodiac.py
```

Output will look like:

```bash
1935: 乙亥 (yĭ-hài, Wood Pig; yin - year 12 of the cycle)
1938: 戊寅 (wù-yín, Earth Tiger; yang - year 15 of the cycle)
1968: 戊申 (wù-shēn, Earth Monkey; yang - year 45 of the cycle)
1972: 壬子 (rén-zĭ, Water Rat; yang - year 49 of the cycle)
1976: 丙辰 (bĭng-chén, Fire Dragon; yang - year 53 of the cycle)
2022: 壬寅 (rén-yín, Water Tiger; yang - year 39 of the cycle)
```

Tests can be run standalone with pytest. To run the tests with coverage report 

```bash
coverage run --source=. -m pytest
```

Coverage report can then be viewed with 

```bash
coverage report
```
