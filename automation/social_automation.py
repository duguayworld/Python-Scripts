import subprocess
import time
import os

def run_script(script_name):
    try:
        # Run the script using subprocess
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

if __name__ == "__main__":
    # Specify the list of script names to run in sequence
    script_names = ['/home/bnzo/PycharmProjects/pythonProject/Automation/FBAutomation/FBautomation.py']

    # Get the current working directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Infinite loop to run the scripts every hour
    while True:
        for script_name in script_names:
            # Construct the full path to the script
            script_path = os.path.join(current_directory, script_name)

            # Run the script
            run_script(script_path)

        # Sleep for one hour before running the scripts again
        time.sleep(3600)
