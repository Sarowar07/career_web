from flask import Flask, render_template,jsonify
app= Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 1,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location': 'Kolkata, India',
    'salary': 'Rs. 1,20,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location': 'Hyderabad, India',
    'salary': 'Rs. 1,50,000'
  },
  {
    'id':4,
    'title':'Business Analyst',
    'location': 'Delhi, India',
    'salary': 'Rs. 2,00,000'
  },
]
@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS,company_name="AG")
@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ =="__main__":
  app.run(host='0.0.0.0',debug=True)