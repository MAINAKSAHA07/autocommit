import time
import subprocess
from datetime import datetime

def make_commit():
    """Run the auto_commit.py script."""
    try:
        subprocess.run(['python3', 'auto_commit.py'], check=True)
        print(f"Commit made at {datetime.now()}")
    except subprocess.CalledProcessError as e:
        print(f"Error making commit: {e}")

def main():
    print(f"Making immediate commit... Current time: {datetime.now()}")
    make_commit()
    
    print(f"Waiting 5 minutes for next commit... Current time: {datetime.now()}")
    time.sleep(300)  # Wait for 5 minutes (300 seconds)
    make_commit()

if __name__ == "__main__":
    main() 