# Bayonet test
The Bayonet test is create to analize data contained in a CSV file.

This proyect is developed with Python3. You can install dependencies in the host or an virtual eviroment. The dependencies are listed in *requeriments.txt*. Execute next command to install with:
```bash
pip install -r requeriments.txt
```

The proyect requires a *.env* file to provide parameters to connect to database. An example of the content of the file is in *.env.test*.

## Set up a database
This step is to populate a MySQL database from the csv's data.

```bash
python database.py /path/to/file/dataset.csv
```

## Data Analysis
This step is to analyze data in the database. There are the follow tools:
1. Number of transactions for each transaction type.
2. Frecuency of the emails' domains for each transaction type.
3. Frecuency of names and last names for each transaction type.
4. Frecuency of card_bin and card_last_4 for each transaction type.
5. Average of the amount for each transaction type.

```bash
# 1. number of transactions
python data_analysis.py total_transactions

# 2. Frecuency of the emails' domains
python data_analysis.py email_frec

# 3. Frecuency of the names and lastnames
python data_analysis.py names_frec

# 4. Frecuency of the card_bin and card_last_4
python data_analysis.py card_frec

# 5. Amount average
python data_analysis.py average_amounts
```
