# Automated Git Commit Script

This script automatically creates and commits random text files to a Git repository at regular intervals.

## Features

- Creates random text files with unique timestamps
- Commits files to Git repository
- Pushes changes to GitHub
- Runs automatically on a schedule
- Logs all activities

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-directory>
   ```

2. Make the script executable:
   ```bash
   chmod +x auto_commit.py
   ```

3. Set up Git credentials:
   - Configure your GitHub credentials
   - Make sure you have proper SSH keys set up

4. Test the script manually:
   ```bash
   ./auto_commit.py
   ```

5. The cron job is already set up to run hourly during April and May 2025.

## File Structure

- `auto_commit.py`: Main script that handles file creation and Git operations
- `auto_commit.log`: Log file containing all commit activities
- `random_content_*.txt`: Generated files with random content

## Troubleshooting

If commits are not being made:
1. Check the log file: `cat auto_commit.log`
2. Verify cron is running: `crontab -l`
3. Check Git status: `git status`
4. Verify GitHub connection: `git remote -v`

## Requirements

- Python 3.x
- Git
- GitHub account with proper permissions
- Cron (for scheduling)

## Logging

All activities are logged to `auto_commit.log` with timestamps and details of each operation.

## Security Notes

- Git credentials are required for pushing to GitHub
- Make sure your SSH keys are properly configured
- Keep your repository private if needed

## Maintenance

To modify the schedule:
1. Edit the cron job: `crontab -e`
2. Update the timing pattern as needed
3. Save and exit

To stop automated commits:
1. Remove the cron job: `crontab -r`
2. Or edit the cron job to remove the specific entry 