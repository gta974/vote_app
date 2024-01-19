

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, send_file, jsonify
import controller.db_stuffs as db_stuffs
# import controller.get_stats as get_stats

# app = Flask(__name__,template_folder="templates") 
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__,)

def push_vote_in_DB(vote, ip):
    '''
    on insert le vote dans la base de donnees
    '''
    print(vote, " ", ip)
    db_stuffs.push_vote(vote, ip)

def get_stat_on_votes(ip):
    '''
    '''
    stats = db_stuffs.get_stats(ip)
    # print(nombre_de_votes)
    return stats

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
# def accueil():
#     ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) 
#     # return 'Hello World, your ip is : ' + ip
#     return render_template("index.html", message="hello")
def index():
    return render_template("index.html", message="Hello")
 
@app.route('/process', methods=['POST']) 
def process(): 
    data = request.get_json() # retrieve the data sent from JavaScript 
    # process the data using Python code 
    vote = data['value']
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    push_vote_in_DB(vote, ip)
    stats = get_stat_on_votes(ip)
    print('stats : ')
    print(stats)
    message = 'Vous avez vote pour ' + vote + '<BR>'
    message += 'Vous avez vote ' + str(stats[0]) + ' fois<BR>'
    message += 'Il y a eu ' + str(stats[1]) + ' votes au total<BR>'
    message += 'Classement :<BR>'
    nombre_de_votes = int(stats[1])
    for item in stats[2]:
        message += item[0] + ' a recueilli : ' + str(round(int(item[1]) / nombre_de_votes * 100, 2)) + ' % des votes<BR>'
    print(message)
    return jsonify(result=message) # return the result to JavaScript
    # return render_template("index.html", message=message)
    # return render_template("process.html")
    # return render_template("index.html", message="not a skp file or a blender file.")

@app.route('/result', methods=['POST']) 
def result(): 
    data = request.get_json() # retrieve the data sent from JavaScript 
    # process the data using Python code 
    vote = data['value']
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    # push_vote_in_DB(vote, ip)
    stats = get_stat_on_votes(ip)
    print('stats : ')
    print(stats)
    message = 'Il y a eu ' + str(stats[1]) + ' votes au total<BR>'
    message += 'Classement :<BR>'
    nombre_de_votes = int(stats[1])
    for item in stats[2]:
        message += item[0] + ' a recueilli : ' + str(round(int(item[1]) / nombre_de_votes * 100, 2)) + ' % des votes<BR>'
    print(message)
    return jsonify(result=message)

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0', port=2000,debug=True)
