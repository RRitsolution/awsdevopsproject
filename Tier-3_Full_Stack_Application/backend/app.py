from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# --- MySQL Configurations ---
# 'db' is the name of the database service in docker-compose.yml
app.config['MYSQL_HOST'] = 'db'
# 'root' is the default MySQL user for this setup
app.config['MYSQL_USER'] = 'root'
# 'password' is the password we set in the docker-compose file
app.config['MYSQL_PASSWORD'] = 'root'
# 'peopledb' is the database name we will use
app.config['MYSQL_DB'] = 'peopledb'

mysql = MySQL(app)

# Define the API endpoint that the frontend will call
@app.route('/people')
def get_people():
    try:
        # Create a cursor to execute SQL queries
        cur = mysql.connection.cursor()
        # Execute a SQL query to select all names and ages from the 'people' table
        cur.execute("SELECT name, age FROM people")
        # Fetch all the results from the query
        people_data = cur.fetchall()
        cur.close()

        # Convert the data into a list of dictionaries for JSON
        people_list = []
        for name, age in people_data:
            people_list.append({'name': name, 'age': age})

        return jsonify(people_list) # Return the data as a JSON response

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to connect to database or fetch data"}), 500

if __name__ == '__main__':
    # 'host=0.0.0.0' makes the app accessible from outside the container
    app.run(host='0.0.0.0', port=5000)
