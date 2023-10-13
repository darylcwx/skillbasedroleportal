import os
import subprocess
import threading

# Install Python dependencies from backend/requirements.txt
try:
    subprocess.check_call(["pip", "install", "-r", "backend/requirements.txt"])
    print("Installed Python dependencies from requirements.txt.")
except subprocess.CalledProcessError as e:
    print(f"Failed to install Python dependencies: {e}")

# Start up mysql service
service_name = "wampmysqld64"
subprocess.call(["sc", "start", service_name])
print(f"Started the '{service_name}' service.")

# Start up Flask in a separate thread
def start_flask():
    os.environ['FLASK_APP'] = 'backend/app.py'
    subprocess.call(["python", "-m", "flask", "run"])
    print("Started the Flask server.")

flask_thread = threading.Thread(target=start_flask)
flask_thread.start()

# Start up load_init_sql.py in a separate thread
def start_load_init_sql():
    subprocess.call(["python", "load_init_sql.py"])
    print("Started the load_init_sql.py script.")

load_sql_thread = threading.Thread(target=start_load_init_sql)
load_sql_thread.start()

# Start up npm in a separate thread
def start_npm():
    subprocess.run("npm i", shell=True, cwd="frontend/")
    subprocess.run("npm run dev", shell=True, cwd="frontend/")
    print("Started the npm process in another directory.")

npm_thread = threading.Thread(target=start_npm)
npm_thread.start()

try:
    # Wait for Flask thread to finish
    flask_thread.join()
    load_sql_thread.join()
    npm_thread.join()
    # Kill the load_init_sql.py thread when Flask thread finishes
    # load_sql_thread.kill()
    # print("Killed the load_init_sql.py thread.")
except KeyboardInterrupt:
    subprocess.run(["sc", "stop", service_name])
    print(f"Stopped the '{service_name}' service.")