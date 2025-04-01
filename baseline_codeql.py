import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q')
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # 🚨 Vulnerable to SQL Injection
    sql = f"SELECT * FROM users WHERE name = '{query}'"
    cursor.execute(sql)
    
    results = cursor.fetchall()
    return {'results': results}
