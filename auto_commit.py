#!/usr/bin/env python3

import os
import random
import string
from datetime import datetime
import subprocess
import sys

def generate_random_content():
    """Generate random text content."""
    # Generate a random length between 100 and 500 characters
    length = random.randint(100, 500)
    # Generate random text using letters, numbers, and spaces
    content = ''.join(random.choices(string.ascii_letters + string.digits + ' \n', k=length))
    return content

def git_operations():
    """Perform Git operations."""
    try:
        # Generate random content
        content = generate_random_content()
        
        # Create a timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"random_content_{timestamp}.txt"
        
        # Write content to file
        with open(filename, 'w') as f:
            f.write(content)
        
        # Git commands
        commands = [
            ['git', 'add', filename],
            ['git', 'commit', '-m', f'Automated commit: {timestamp}'],
            ['git', 'push']
        ]
        
        # Execute Git commands
        for cmd in commands:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error executing {cmd}: {result.stderr}")
                return False
        
        print(f"Successfully committed and pushed {filename}")
        return True
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    # Check if we're in a Git repository
    if not os.path.exists('.git'):
        print("Error: Not a Git repository. Please run this script in a Git repository.")
        sys.exit(1)
    
    # Perform Git operations
    success = git_operations()
    sys.exit(0 if success else 1) 