import os
from flask import Flask, request, send_from_directory, Response
from flask import jsonify
from flask import render_template
from dotenv import load_dotenv
import pymysql.cursors

from analysis import util

load_dotenv()

connection = pymysql.connect(
    user=os.environ.get("DATABASE_USER"),
    password=os.environ.get("DATABASE_PASSWORD"),
    host=os.environ.get("DATABASE_HOST"),
    database=os.environ.get("DATABASE_NAME"),
    cursorclass=pymysql.cursors.SSCursor
)

# set the project root directory as the static folder, you can set others.
app = Flask('bayonet',
    static_folder='static',
    static_url_path='/static'
)

@app.route('/metadata')
def get_metadata():
    with connection.cursor() as cursor:
        data = util.get_metadata(cursor)
        return jsonify(data)

    flask.abort(500)
    flask.abort(Response('Error'))

@app.route('/total-transacciones')
def get_total_transactions():
    with connection.cursor() as cursor:
        data = util.get_total_transactions(cursor)

        return jsonify(data)
    
    flask.abort(500)
    flask.abort(Response('Error'))

@app.route('/frecuencia-correos')
def get_email_frec():
    with connection.cursor() as cursor:
        data = util.get_email_frec(cursor)

        transactions = {}
        for transaction_type, emails in data.items():
            transactions[transaction_type] = sorted(emails.items(), key=lambda kv: kv[1], reverse=True)

        return jsonify(transactions)
    
    flask.abort(500)
    flask.abort(Response('Error'))

@app.route('/frecuencia-nombres')
def get_name_frec():
    with connection.cursor() as cursor:
        data = util.get_names_frec(cursor)

        transactions = {}
        for transaction_type, names in data.items():
            transactions[transaction_type] = {}
            transactions[transaction_type]['names'] = sorted(names['names'].items(), key=lambda kv: kv[1], reverse=True)
            transactions[transaction_type]['lastnames'] = sorted(names['lastnames'].items(), key=lambda kv: kv[1], reverse=True)

        return jsonify(transactions)
    
    flask.abort(500)
    flask.abort(Response('Error'))

@app.route('/frecuencia-tarjetas')
def get_card_frec():
    with connection.cursor() as cursor:
        data = util.get_card_frec(cursor)

        transactions = {}
        for transaction_type, names in data.items():
            transactions[transaction_type] = {}
            transactions[transaction_type]['card_bin'] = sorted(names['card_bin'].items(), key=lambda kv: kv[1], reverse=True)
            transactions[transaction_type]['card_last_4'] = sorted(names['card_last_4'].items(), key=lambda kv: kv[1], reverse=True)

        return jsonify(transactions)
    
    flask.abort(500)
    flask.abort(Response(''))

@app.route('/monto-promedio')
def get_avg_amount():
    with connection.cursor() as cursor:
        month = request.args.get('month')
        year = request.args.get('year')

        data = util.get_avg_amounts(cursor, month, year)

        return jsonify(data)
    
    flask.abort(500)
    flask.abort(Response('Error'))

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()
