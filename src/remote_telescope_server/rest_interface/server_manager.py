import subprocess


def start_server():
    subprocess.Popen(["uvicorn", "rest_server:telescope_server",
                    "--reload", "--host", "0.0.0.0", "--port", "8000"])


def stop_server():
    subprocess.run(["pkill", "uvicorn"])
