from src.ClipManager import *
import os
import logging

clips_list = []

delete temp videos from prev run. Should go at end, but causes but
for vid in os.listdir("../conformed-videos/"):
    os.remove("../conformed-videos/" + vid)

try:
    i = 0
    for vid in os.listdir("../input-videos/"):  # makes a copy of each video the same resolution, can be configured in ClipManager
        normalize_resolutions(vid, i)
        i += 1
    for vid in os.listdir("../input-videos/"):  # gets all videos from folder, cuts them into pieces, and adds them to list
        clips_list.append(create_clips(VideoFileClip("../input-videos/" + vid)))  # clips_list is 2d list; each index conntains the pieces of one video
except Exception as e:
    logging.exception(e)

clips_list = homogenize(clips_list)  # Makes clips into 2 even stacks of clips
laced_clips = lace_clips(clips_list)  # list becomes one-dimensional as 2 stacks of clips are weaved together evenly
concatenate_videoclips(laced_clips)\
    .write_videofile("../vid-to-upload/vid_to_upload.mp4")  # should have name generated based on tags from source videos
