# importing from flask module the Flask class, the render_template function, the request function, url_for 
# and redirect function to redirect to index home page after updating the app database
from flask import Flask, render_template, request, url_for, redirect, jsonify 
# Mongoclient is used to create a mongodb client, so we can connect on the localhost 
# with the default port
from pymongo import MongoClient
# ObjectId function is used to convert the id string to an objectid that MongoDB can understand
from bson.objectid import ObjectId
# Instantiate the Flask class by creating a flask application
app = Flask(__name__)
# Create the mongodb client
client = MongoClient("mongodb://mongouser:mongopassword@flaskmongodb.spancorp.internal:27017/")

# Get and Post Route
@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":   # if the request method is post, then insert the todo document in todos collection
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index')) # redirect the user to home page
    all_todos = todos.find()    # display all todo documents
    return render_template('index.html', todos = all_todos) # render home page template with all todos

#Delete Route
@app.post("/<id>/delete/")
def delete(id): #delete function by targeting a todo document by its own id
    todos.delete_one({"_id":ObjectId(id)}) #deleting the selected todo document by its converted id
    return redirect(url_for('index')) # again, redirecting you to the home page 

# Add the health check endpoint here
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200      #If problem, remove this line and uncomment comment block below
    '''
    try:
        # Check MongoDB connection
        client.server_info()
        return jsonify({
            "status": "healthy",
            "database": "connected"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }), 500
    '''
db = client.flask_database # creating your flask database using your mongo client 
todos = db.todos # creating a collection called "todos"


# The dunder if __name__ code block
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True) #running your server on development mode, setting debug to True
