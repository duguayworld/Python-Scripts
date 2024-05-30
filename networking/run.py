import subprocess


def run_scripts():
    while True:
        # Run the first script
        subprocess.run(["python", "rawinjection.py"])

        # Run the second script
        subprocess.run(["python", "rawsniffer.py"])


if __name__ == "__main__":
    run_scripts()
