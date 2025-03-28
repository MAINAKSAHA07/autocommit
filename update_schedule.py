#!/usr/bin/env python3

import random
import subprocess
import os
from datetime import datetime

def generate_random_time():
    """Generate a random minute between 0 and 59."""
    return random.randint(0, 59)

def update_cron_schedule():
    """Update the cron schedule with random times."""
    try:
        # Generate random minutes for both AM and PM
        am_minute = generate_random_time()
        pm_minute = generate_random_time()
        
        # Get the current directory
        current_dir = os.getcwd()
        
        # Create the cron command
        cron_cmd = f'{am_minute} 0,{pm_minute} 12 * * * cd "{current_dir}" && /opt/homebrew/bin/python3 "{current_dir}/auto_commit.py" >> "{current_dir}/auto_commit.log" 2>&1'
        
        # Update crontab
        process = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE)
        process.communicate(input=cron_cmd.encode())
        
        # Log the new schedule
        with open('auto_commit.log', 'a') as f:
            f.write(f'\n[{datetime.now()}] Updated schedule to run at {am_minute:02d}:00 AM and {pm_minute:02d}:00 PM\n')
        
        print(f"Schedule updated to run at {am_minute:02d}:00 AM and {pm_minute:02d}:00 PM")
        return True
        
    except Exception as e:
        print(f"Error updating schedule: {str(e)}")
        return False

if __name__ == "__main__":
    update_cron_schedule() 