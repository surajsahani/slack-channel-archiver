import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=SLACK_BOT_TOKEN)
INACTIVITY_DAYS = 30

def is_channel_inactive(channel_id):
    try:
        now_ts = time.time()
        oldest_ts = now_ts - (INACTIVITY_DAYS * 24 * 60 * 60)
        history = client.conversations_history(channel=channel_id, oldest=oldest_ts, limit=1)
        messages = history.get("messages", [])
        return len(messages) == 0
    except SlackApiError as e:
        print(f"Error checking history for {channel_id}: {e.response['error']}")
        return False

def archive_old_channels():
    try:
        response = client.conversations_list(types="public_channel", limit=1000)
        for channel in response["channels"]:
            if channel.get("is_archived", False):
                continue
            channel_id = channel["id"]
            channel_name = channel["name"]
            if not channel.get("is_member", False):
                try:
                    client.conversations_join(channel=channel_id)
                except SlackApiError as e:
                    print(f"Could not join channel {channel_name}: {e.response['error']}")
            if is_channel_inactive(channel_id):
                print(f"Archiving inactive channel: #{channel_name}")
                try:
                    client.conversations_archive(channel=channel_id)
                except SlackApiError as e:
                    print(f"Failed to archive {channel_name}: {e.response['error']}")
    except SlackApiError as e:
        print(f"Failed to list channels: {e.response['error']}")

if __name__ == "__main__":
    archive_old_channels()
