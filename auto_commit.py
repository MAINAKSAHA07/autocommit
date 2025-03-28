#!/usr/bin/env python3

import os
import random
import string
import subprocess
import time
from datetime import datetime, timedelta
import sys

def generate_random_content():
    """Generate random text content."""
    length = random.randint(100, 500)
    return ''.join(random.choices(string.ascii_letters + string.digits + '\n', k=length))

def create_random_file():
    """Create a file with random content and current timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"random_content_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        f.write(generate_random_content())
    
    return filename

def git_commit_and_push(filename):
    """Commit and push the file to GitHub."""
    try:
        # Add the file
        subprocess.run(['git', 'add', filename], check=True)
        
        # Commit with timestamp
        commit_message = f"Automated commit: {filename.replace('random_content_', '').replace('.txt', '')}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        
        # Push to remote
        subprocess.run(['git', 'push'], check=True)
        
        print(f"Successfully committed and pushed {filename}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing {e.cmd}: {e.stderr.decode() if e.stderr else str(e)}")
        return False

def update_schedule():
    """Update the cron schedule with new random times."""
    try:
        # Generate random minutes for morning and evening
        morning_minute = random.randint(0, 59)
        evening_minute = random.randint(0, 59)
        
        # Create the cron command
        cron_cmd = f"{morning_minute} 0,{evening_minute} 12 * * * cd \"{os.getcwd()}\" && /opt/homebrew/bin/python3 \"{os.path.join(os.getcwd(), 'auto_commit.py')}\" >> \"{os.path.join(os.getcwd(), 'auto_commit.log')}\" 2>&1"
        
        # Update crontab
        subprocess.run(['crontab', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['echo', cron_cmd, '|', 'crontab', '-'], shell=True)
        
        print(f"Schedule updated to run at {morning_minute}:00 AM and {evening_minute}:00 PM")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error updating schedule: {e.stderr.decode() if e.stderr else str(e)}")
        return False

def main():
    """Main function to create random file and push to GitHub."""
    try:
        # Create random file
        filename = create_random_file()
        
        # Commit and push
        if git_commit_and_push(filename):
            # Update schedule for next run
            update_schedule()
            print("Schedule updated for next run")
    except Exception as e:
        print(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    # Check if we're in a Git repository
    if not os.path.exists('.git'):
        print("Error: Not a Git repository. Please run this script in a Git repository.")
        sys.exit(1)
    
    main() 