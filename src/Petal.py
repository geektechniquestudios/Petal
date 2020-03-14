from src.ClipManager import *
import os
import logging


clips_list = []

try:
    for vid in os.listdir("../input-videos"):  # gets all videos from folder and adds them to list
        clips_list.append(create_clips(VideoFileClip("../input-videos/" + vid)))
except Exception as e:
    logging.exception(e)

clips_list = homogenize(clips_list)

laced_clips = lace_clips(clips_list)  # list becomes one-dimensional


finished_video = concatenate_videoclips(laced_clips)

print(finished_video.duration)
finished_video.write_videofile("../vid-to-upload/vid_to_upload.mp4")  # should have name generated based on tags from source videos
