import os
import csv
from dotenv import load_dotenv
import pymysql.cursors
from dateutil.parser import parse

load_dotenv(verbose=True)

if __name__ == "__main__":
    values = []
    # print()

    with open('dataset.csv', 'r', encoding='utf8', errors='ignore') as datafile:
        csv_reader = csv.DictReader(datafile, delimiter=',')
        for data in csv_reader:
            data['transaction_time'] = parse(data['transaction_time']).isoformat()
            data_values = '(NULL, "{transaction_status}", "{transaction_time}", "{email}", "{consumer_name}", "{cardholder_name}", "{card_bin}", "{card_last_4}", {transaction_amount})'.format(**data)
            values.append(data_values)
    
    if len(values) > 0:
        query = "INSERT INTO transaction VALUES {}".format(','.join(values))
    
        connection = pymysql.connect(host=os.environ.get("DATABASE_HOST"),
            user=os.environ.get("DATABASE_USER"),
            password=os.environ.get("DATABASE_PASSWORD"),
            db=os.environ.get("DATABASE_NAME"),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        
        with connection.cursor() as cursor:
            # Create a new record
            cursor.execute(query)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
