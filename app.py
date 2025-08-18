from flask import Flask, render_template,jsonify
from database import load_jobs_from_db,load_job_from_db
from sqlalchemy import text
import os

app= Flask(__name__)

@app.route("/")
def hello_world():
  try:
    jobs=load_jobs_from_db()
    return render_template("home.html",jobs=jobs,company_name="AG")
  except Exception as e:
    print(f"Database error: {e}")
    # Return a simple page if database fails
    return render_template("home.html",jobs=[],company_name="AG")
@app.route("/jobs")
def list_jobs():
  try:
    jobs=load_jobs_from_db()
    return jsonify(jobs)
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@app.route("/job/<id>")
def show_job(id):
  try:
    job=load_job_from_db(id)
    return jsonify(job)
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@app.route("/debug")
def debug_info():
  db_env = os.environ.get('DB_CONNECTION_STRING', 'Not set')
  return jsonify({
    "db_connection_string": "Set" if db_env != 'Not set' else "Not set",
    "ca_pem_exists": os.path.exists('ca.pem')
  })

if __name__ =="__main__":
  print("Starting Flask app...")
  print(f"DB_CONNECTION_STRING set: {'Yes' if os.environ.get('DB_CONNECTION_STRING') else 'No'}")
  app.run(host='0.0.0.0', port=5000, debug=True)