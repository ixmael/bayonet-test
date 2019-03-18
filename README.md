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
This step is to analyze data in the database.

This implementation is in the dir */part2* and uses python3. The modules required are in */part2/requeriments.txt*. 

This require the instalation of modules:
```bash
pip install -r requeriments.txt
```

There are the follow tools:
```bash
# 1. Number of transactions for each transaction type.
python data_analysis.py total_transactions

# 2. Frecuency of the emails' domains for each transaction type.
python data_analysis.py email_frec

# 3. Frecuency of names and last names for each transaction type.
python data_analysis.py names_frec

# 4. Frecuency of card_bin and card_last_4 for each transaction type.
python data_analysis.py card_frec

# 5. Average of the amount for each transaction type.
python data_analysis.py average_amounts
```

## Data Visualization
This step is to display the information of previous step.

This implementation is in dir */part3* and uses python3 (backend) and VueJs (frontend). The modules required for backend are in */part3/requeriments.txt*. The frontend is in */part3/client-web*.

**The next instructions are required to be executed in the dir */part3*.**

The backend require the instalation of modules:
```bash
pip install -r requeriments.txt
```

To start the server:
```
python server.py
```
this project has the deafult settings of Flask and the ip to provide its service is http://127.0.0.1:5000.

**The front end require that the next steps executed in */part3/client-web*.**
The instalation of packages for the frontend:
```bash
yarn install
```

To develop use:
```bash
yarn run build:dev
```

To generate the production bundle:
```bash
yarn run build
```
