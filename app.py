
# Flask Library
from flask import Flask, request, jsonify #Imported request and jsonify as well, just in case


# Create App Object
app = Flask(__name__)


# List of Students
students = [
    {
        "id": 1,
        "name": 'tom'
    },
    {
        "id": 2,
        "name": "Jerry"
    },
    {
        "id": 3,
        "name": "Bugs Bunny"
    }
]

# Example endpoint
@app.route('/example')
def home():
    return "Welcome to the Flask API!"

#### ASSIGNMENT STARTS HERE ####

#I was unable to figure out how to run these, so the only thing I was able to do was debug them. I did my best based on what info I could find.

@app.route('/getall', methods = ['GET'])
def geta():
    return jsonify(students)

@app.route('/getone/<int:student_id>', methods = ['GET'])
def geto(student_id):
    student=next((student for student in students if student["id"] == student_id), None) #Finds the student given the ID
    return jsonify(item)

@app.route('/addstudent', methods = ['POST'])
def add_student():

    entry = request.get_json()

    if 'id' not in entry or 'name' not in entry:
        return jsonify({'error': 'Invalid input'}), 400

    new_student={
        'id': entry['id'],  #Updates the list by adding the user's inputs
        'name': entry['name']
    }

    students.append(new_student)

@app.route('/update', methods=['PUT'])
def update_student():
    data = request.get_json()
    student_id = data.get('id')
    new_name = data.get('name')

    for student in students:
        if item['id'] == item_id: #Loops through the list until the item is found
             item['name'] = new_name

    return jsonify({'message': 'Item not found'}), 404 #Exception handler


@app.route('/delete', methods = ['DELETE'])
def delete_student():
    data=request.getjson()
    student_id = data.get('id')

    students = [student for student in students if student['id'] != student_id] #Filters out the item with the specified ID





#### ASSIGNMENT ENDS HERE ####

if __name__ == '__main__':
    app.run(debug=True)
