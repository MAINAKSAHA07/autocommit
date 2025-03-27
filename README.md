# Automated Git Commit Script

This script automatically generates random text files, commits them to a Git repository, and pushes them to GitHub on a daily basis.

## Prerequisites

- Python 3.x
- Git installed and configured
- A GitHub repository set up with remote origin
- Git credentials configured (either via SSH key or personal access token)

## Setup Instructions

1. Clone this repository or copy the `auto_commit.py` script to your desired Git repository.

2. Make the script executable:
   ```bash
   chmod +x auto_commit.py
   ```

3. Test the script manually first:
   ```bash
   ./auto_commit.py
   ```

4. Set up a cron job to run the script daily:

   Open your crontab:
   ```bash
   crontab -e
   ```

   Add the following line to run the script daily at midnight:
   ```bash
   0 0 * * * cd /path/to/your/repo && /usr/bin/python3 /path/to/your/repo/auto_commit.py >> /path/to/your/repo/auto_commit.log 2>&1
   ```

   Replace `/path/to/your/repo` with the actual path to your repository.

## How It Works

The script:
1. Generates random text content (100-500 characters)
2. Creates a timestamped file with the random content
3. Commits the file to Git with a timestamped commit message
4. Pushes the changes to the remote repository

## Troubleshooting

- Check the log file specified in your cron job for any errors
- Ensure your Git credentials are properly configured
- Verify that the repository has a remote origin set up
- Make sure you have write permissions in the repository directory

## Notes

- The script will only work when run from within a Git repository
- Each run creates a new file with a unique timestamp
- Failed operations will be logged in the specified log file 