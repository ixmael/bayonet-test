import os
from dotenv import load_dotenv
import pymysql.cursors
import argparse

from analysis import util

load_dotenv()

connection = pymysql.connect(
    user=os.environ.get("DATABASE_USER"),
    password=os.environ.get("DATABASE_PASSWORD"),
    host=os.environ.get("DATABASE_HOST"),
    database=os.environ.get("DATABASE_NAME"),
    cursorclass=pymysql.cursors.SSCursor
)

if __name__ == "__main__":
    choices = ('total_transactions', 'email_frec', 'names_frec', 'card_frec', 'average_amounts',)

    parser = argparse.ArgumentParser(description='Analyze the data from the database.')
    parser.add_argument('task', type=str, choices=choices, help='The analysis task')
    args = parser.parse_args()

    with connection.cursor() as cursor:
        if args.task == 'total_transactions':
            transactions = util.get_total_transactions(cursor)
            for k, v in transactions.items():
                print(k, v)
        
        elif args.task == 'email_frec':
            transactions = util.get_email_frec(cursor)
            for k, v in transactions.items():
                print(k)
                for k, v in sorted(v.items(), key=lambda kv: kv[1], reverse=True):
                    print('\t{}: {}'.format(k, v))
        
        elif args.task == 'names_frec':
            transactions = util.get_names_frec(cursor)
            for transaction, names in transactions.items():
                print(transaction)
                
                print('\tNames')
                for k, v in sorted(names['names'].items(), key=lambda kv: kv[1], reverse=True):
                    print('\t\t{}: {}'.format(k, v))
                
                print('\tLastnames')
                for k, v in sorted(names['lastnames'].items(), key=lambda kv: kv[1], reverse=True):
                    print('\t\t{}: {}'.format(k, v))
        
        elif args.task == 'card_frec':
            transactions = util.get_card_frec(cursor)
            #print(transactions)
            for transaction_status, cards in transactions.items():
                print(transaction_status)

                print('\tCARD_BIN')
                for k, v in sorted(cards['card_bin'].items(), key=lambda kv: kv[1], reverse=True):
                    print('\t\t{}: {}'.format(k, v))
                
                print('\tCARD_LAST_4')
                for k, v in sorted(cards['card_last_4'].items(), key=lambda kv: kv[1], reverse=True):
                    print('\t\t{}: {}'.format(k, v))
        
        elif args.task == 'average_amounts':
            transactions = util.get_avg_amounts(cursor)
            for transaction_status, amount in transactions.items():
                print('{}: {}'.format(transaction_status, amount))
