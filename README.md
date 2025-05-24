# slack-channel-archiver
# Slack Channel Auto-Archiver Bot

This bot automatically archives public Slack channels with no messages in the last 30 days.

## Setup

1. Create a Slack App here: https://api.slack.com/apps
2. Add these OAuth scopes:
   - `channels:read`
   - `channels:join`
   - `channels:manage`
   - `channels:history`
3. Install the app to your workspace.
4. Copy your **Bot User OAuth Token** (starts with `xoxb-...`).

## Deploy with GitHub Actions

1. Fork this repo or create your own.
2. Add a GitHub secret:
   - Name: `SLACK_BOT_TOKEN`
   - Value: your Slack Bot User OAuth Token
3. GitHub Actions will run the bot daily at 3 AM UTC.
4. You can also trigger it manually via the "Actions" tab.

## Customize

- Change `INACTIVITY_DAYS` in `archive_inactive_channels.py` to adjust the threshold.
- Add filters to exclude specific channels if needed.

---

*Happy automating!*
