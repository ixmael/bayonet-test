'''Data analysis functions
'''
import re

def get_total_transactions(cursor):
    '''Count the transactions
    '''
    query = 'SELECT transaction_status, COUNT(transaction_status) AS transactions FROM `transaction` GROUP BY transaction_status ORDER BY transactions;'
    cursor.execute(query)

    transactions = {}
    for r in cursor:
        transactions[r[0]] = r[1]
    
    return transactions

def get_email_frec(cursor):
    '''Email domain frecuency by transaction type
    '''
    transactions = {}

    query = 'SELECT id, transaction_status, email FROM transaction ORDER BY transaction_status;'
    cursor.execute(query)

    for r in cursor:
        if not r[1] in transactions:
            transactions[r[1]] = {}
        
        domain = r[2].rpartition('@')[2]

        if not domain in transactions[r[1]]:
            transactions[r[1]][domain] = 0
        
        transactions[r[1]][domain] += 1
    
    return transactions

def get_names_frec(cursor):
    '''Frecuency the last name and the firts name by transaction types
    '''
    transactions = {}

    query = 'SELECT id, transaction_status, cardholder_name FROM transaction ORDER BY transaction_status;'
    cursor.execute(query)

    for r in cursor:
        if not r[1] in transactions:
            transactions[r[1]] = {}

        if not 'names' in transactions[r[1]]:
            transactions[r[1]]['names'] = {}

        if not 'lastnames' in transactions[r[1]]:
            transactions[r[1]]['lastnames'] = {}

        names = re.sub(' +', ' ', r[2]).strip().split(' ', 1)

        if not names[0] in transactions[r[1]]['names']:
            transactions[r[1]]['names'][names[0]] = 0
        
        if not names[1] in transactions[r[1]]['lastnames']:
            transactions[r[1]]['lastnames'][names[1]] = 0
        
        transactions[r[1]]['names'][names[0]] += 1
        transactions[r[1]]['lastnames'][names[1]] += 1
    
    return transactions

def get_card_frec(cursor):
    '''Frecuency of the card ids by transaction type
    '''
    transactions = {}

    query = 'SELECT id, transaction_status, card_bin, card_last_4 FROM transaction ORDER BY transaction_status;'
    cursor.execute(query)

    for r in cursor:
        if not r[1] in transactions:
            transactions[r[1]] = {}

        if not 'card_bin' in transactions[r[1]]:
            transactions[r[1]]['card_bin'] = {}
        
        if not 'card_last_4' in transactions[r[1]]:
            transactions[r[1]]['card_last_4'] = {}
        
        if not r[2] in transactions[r[1]]['card_bin']:
            transactions[r[1]]['card_bin'][r[2]] = 0
        
        if not r[3] in transactions[r[1]]['card_last_4']:
            transactions[r[1]]['card_last_4'][r[3]] = 0
        
        transactions[r[1]]['card_bin'][r[2]] += 1
        transactions[r[1]]['card_last_4'][r[3]] += 1
    
    return transactions

def get_avg_amounts(cursor):
    '''Get the average amounts by transaction type
    '''
    transactions = {}

    query = 'SELECT transaction_status, AVG(transaction_amount) from transaction GROUP BY transaction_status;'
    cursor.execute(query)

    for r in cursor:
        if not r[0] in transactions:
            transactions[r[0]] = 0
        
        transactions[r[0]] = float(r[1])

    return transactions
