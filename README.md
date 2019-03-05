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
