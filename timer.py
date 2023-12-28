import time
import subprocess

def run_script():
    # Define python script to run
    subprocess.run(["python", "post_frame.py"])

def main():
    while True:
        run_script()
        time.sleep(5 * 60)  #Wait 5 minutes to run

if __name__ == "__main__":
    main()
