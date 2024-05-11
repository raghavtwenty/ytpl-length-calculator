"""
Application Name: Youtube Playlist Length Calculator
Author: Raghava | Github: @raghavtwenty
Date Created: Feb 25, 2023 | Last Updated: May 11, 2023
Version Info: 1.0
Language: Python | Version: 3.10.14  64-bit
"""

# Required imports
from googleapiclient.discovery import build
from flask import Flask, render_template
from flask import request
from requests import get

import datetime
import os
import re
import dotenv

dotenv.load_dotenv()

# Set the youtube api key
yt_api_key = os.getenv("YT_API_KEY")


# Build using youtube api version 3 and api key generated
youtube = build("youtube", "v3", developerKey=yt_api_key)


# Flask
app = Flask(__name__)


# ----- Total time calculation
@app.route("/calculated_view", methods=["POST"])
def total_time_cal():

    global normal_convert, x2_convert

    try:
        # Start and end video
        start_vid = abs(int(request.form.get("start_video")))
        end_vid = abs(int(request.form.get("end_video")))

        if (start_vid and end_vid) != None:
            # Time initialization
            hr = 0
            min = 0
            sec = 0

            # Use regular expression to extract hours, minutes, seconds
            hours_pattern = re.compile(r"(\d+)H")
            minutes_pattern = re.compile(r"(\d+)M")
            seconds_pattern = re.compile(r"(\d+)S")

            # Iterate for each video
            for video_time in videos_duration[start_vid - 1 : end_vid]:
                hours = hours_pattern.search(video_time)
                minutes = minutes_pattern.search(video_time)
                seconds = seconds_pattern.search(video_time)

                hours = int(hours.group(1)) if hours else 0
                minutes = int(minutes.group(1)) if minutes else 0
                seconds = int(seconds.group(1)) if seconds else 0

                # Increment hours, minutes, seconds
                hr += hours
                min += minutes
                sec += seconds

            # Total time in seconds
            total_seconds = hr * 60 * 60 + min * 60 + sec
            # Convert seconds to hours and minutes
            normal_convert = datetime.timedelta(seconds=round(total_seconds))

            # 1.25x
            x125_convert = datetime.timedelta(seconds=round(total_seconds / 1.25))

            # 1.5x
            x15_convert = datetime.timedelta(seconds=round(total_seconds / 1.5))

            # 1.75x
            x175_convert = datetime.timedelta(seconds=round(total_seconds / 1.75))

            # 2.0x
            x2_convert = datetime.timedelta(seconds=round(total_seconds / 2))

            # Final Show
            return render_template(
                "calculated_view.html",
                NC_PL=normal_convert,
                x125_PL=x125_convert,
                x15_PL=x15_convert,
                x175_PL=x175_convert,
                x2_PL=x2_convert,
            )

    except:
        # If user enters out of range video value, render invalid html page
        return render_template("invalid_vid_no.html")


# ----- Retrieve video details
# Video ask Route
def yt_vid_details(pl_all_vid_id):

    global total_videos_count, videos_duration

    videos_duration = []

    # Iterate for each video
    for video in pl_all_vid_id:
        vid_req = youtube.videos().list(part="contentDetails", id=video)

        # Storing it in the response variable
        vid_response = vid_req.execute()
        vid_res_items = vid_response["items"]

        for vid_res_item in vid_res_items:
            # For each video item extract duration and append it into videos duration
            remove_pl = vid_res_item["contentDetails"]["duration"]
            videos_duration.append(remove_pl[2:])  # Removes front PL string

    # Total number of videos
    total_videos_count = len(videos_duration)


# ----- Retrieve playlist details
def pl_details(pl_id):

    global pl_all_vid_id
    pl_all_vid_id = []

    nextPageToken = None  # Next page token
    while True:
        playlist_req = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=pl_id,
            maxResults=50,  # Max videos that can be retrieved
            pageToken=nextPageToken,  # Next page reference
        )

        # Storing it in the response variable
        pl_response = playlist_req.execute()
        pl_response_items = pl_response["items"]

        # Take the video id of the entire playlist, append to the list
        temp_pl_all_vid_id = [
            pl_res_item["contentDetails"]["videoId"]
            for pl_res_item in pl_response_items
        ]
        pl_all_vid_id.extend(temp_pl_all_vid_id)

        # Get the next page reference
        nextPageToken = pl_response.get("nextPageToken")

        # If not next page reference is found then break
        if not nextPageToken:
            # Call the video details function to get the details about the video
            yt_vid_details(pl_all_vid_id)
            break


# ----- Main function
@app.route("/video_ask", methods=["POST"])
def main():

    # Getting the playlist input from the user
    yt_pl_link = request.form.get("ytpl_link").strip()

    # Validate the youtube link
    try:
        # Extract the playlist id from the link
        yt_pl_id = yt_pl_link.split("=")[1]

        # Pass the playlist id to the playlist detail function to get the playlist information
        pl_details(yt_pl_id)

        # pass to calculated view template
        return render_template("video_ask.html", VIDEO_COUNT=total_videos_count)

    except:
        # If not yt link, return invalid page
        return render_template("invalid_link.html")


# Default Home Route
@app.route("/")
def home():
    return render_template("index.html")


# ----- Calling the current file main function
if __name__ == "__main__":
    app.run()
