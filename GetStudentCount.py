from flask import Flask, jsonify
import pymssql

app = Flask(__name__)

# Define the database connection details
config = {
    'server': 'studentsvrm16583466.database.windows.net',
    'database': 'studentdbm16583466',
    'username': 'sqladmin',
    'password': 'Sanjana@123',
}

# Define a route to fetch the student count by country
@app.route('/student-count-by-country', methods=['GET'])
def get_student_count_by_country():
    try:
        # Establish the connection to the database
        conn = pymssql.connect(
            server=config['server'],
            user=config['username'],
            password=config['password'],
            database=config['database']
        )
        
        cursor = conn.cursor()
        
        # Execute the query to get the count of students by country
        cursor.execute('SELECT Country, COUNT(*) AS StudentCount FROM Students GROUP BY Country')
        
        # Fetch the result
        rows = cursor.fetchall()
        
        # Convert the result to a list of dictionaries
        result = [{'Country': row[0], 'StudentCount': row[1]} for row in rows]
        
        # Close the connection
        conn.close()
        
        # Return the result as a JSON response
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
