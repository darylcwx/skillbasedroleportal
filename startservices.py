import os
import subprocess
import threading
from colorama import Fore, Style

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

flask_thread = threading.Thread(target=start_flask)
flask_thread.start()
print("Started the Flask server.")

# Start up load_init_sql.py in a separate thread
def start_load_init_sql():
    subprocess.call(["python", "load_init_sql.py"])

load_sql_thread = threading.Thread(target=start_load_init_sql)
load_sql_thread.start()
print("Started the load_init_sql.py script.")

# Start up npm in a separate thread
def start_npm():
    subprocess.run("npm i", shell=True, cwd="frontend/")
    subprocess.run("npm run dev", shell=True, cwd="frontend/")
    print(f"\n{Fore.YELLOW}Press Ctrl+C again to confirm exit.{Style.RESET_ALL}")

npm_thread = threading.Thread(target=start_npm)
npm_thread.start()
print("Started the npm process in another directory.")

try:
    # Wait for Flask thread to finish
    flask_thread.join()
    load_sql_thread.join()
    npm_thread.join()
except KeyboardInterrupt:
    subprocess.run(["sc", "stop", service_name])
    print(f"\n{Fore.YELLOW}startservices has terminated.{Style.RESET_ALL}")