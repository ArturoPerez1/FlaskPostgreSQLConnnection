from flask import Flask, request, jsonify
from src.database.db_postgresql import get_connection
from psycopg.rows import dict_row

app = Flask(__name__)

@app.post("/prueba")
def prueba():
    new_user = request.get_json()
    username = new_user['username']
    email = new_user["email"]
    password = new_user['password']
    conn = get_connection()
    cur = conn.cursor(row_factory=dict_row)
    
    cur.execute('INSERT INTO users (username, email, password) values (%s, %s, %s) RETURNING *',
                (username, email, password))
    
    new_created_user = cur.fetchone()
    print(new_created_user)
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(new_created_user)

if __name__ == '__main__':
    app.run(debug=True)