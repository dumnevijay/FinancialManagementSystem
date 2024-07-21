import subprocess

def start_mysql_windows():
    try:
        # This will start the MySQL service
        subprocess.run(["net", "start", "MySQL"], check=True)
        print("MySQL server started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start MySQL server: {e}")

start_mysql_windows()
