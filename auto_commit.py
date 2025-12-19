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
        # Set up environment for git commands
        env = os.environ.copy()
        env['GIT_TERMINAL_PROMPT'] = '0'  # Disable credential prompts
        
        # Add the file
        result = subprocess.run(['git', 'add', filename], check=True, capture_output=True, text=True, env=env)
        
        # Commit with timestamp
        commit_message = f"Automated commit: {filename.replace('random_content_', '').replace('.txt', '')}"
        result = subprocess.run(['git', 'commit', '-m', commit_message], check=True, capture_output=True, text=True, env=env)
        print(result.stdout)
        
        # Push to remote
        result = subprocess.run(['git', 'push'], check=True, capture_output=True, text=True, env=env)
        print(result.stdout)
        
        print(f"Successfully committed and pushed {filename}")
        return True
    except subprocess.CalledProcessError as e:
        # e.stdout / e.stderr are strings because we use text=True above
        stderr = e.stderr if isinstance(e.stderr, str) or e.stderr is None else e.stderr.decode()
        stdout = e.stdout if isinstance(e.stdout, str) or e.stdout is None else e.stdout.decode()
        error_msg = stderr if stderr else str(e)
        print(f"Error executing {e.cmd}: {error_msg}")
        if stdout:
            print(f"Output: {stdout}")
        return False
    except Exception as e:
        print(f"Unexpected error in git_commit_and_push: {str(e)}")
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
        # Log start time
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting automated commit process")
        
        # Change to script directory to ensure we're in the right place
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        
        # Create random file
        filename = create_random_file()
        print(f"Created file: {filename}")
        
        # Commit and push
        if git_commit_and_push(filename):
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Commit process completed successfully")
        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Commit process failed")
        # Note: Schedule is managed by cron, not updated by this script
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error in main execution: {str(e)}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    # Ensure we're in the script's directory (important for cron)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if we're in a Git repository
    if not os.path.exists('.git'):
        print(f"Error: Not a Git repository. Current directory: {os.getcwd()}")
        sys.exit(1)
    
    main() 