import subprocess
import os

def run_script(script_name):
    try:
        # Run the script using subprocess
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

if __name__ == "__main__":
    # Specify the list of script names to run in sequence
    script_names = ['linkedin_post.py']

    # Get the current working directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Iterate through the list of script names
    for script_name in script_names:
        # Construct the full path to the script
        script_path = os.path.join(current_directory, script_name)

        # Run the script
        run_script(script_path)

        # Add a comment indicating that the script has been executed
        print(f"Script {script_name} executed successfully.")

    # Script will exit after running all scripts

