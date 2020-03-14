from moviepy.editor import *
import math


def create_clips(vid: VideoFileClip):
    num_clips = math.ceil(vid.duration / 30)
    clips_arr = []
    for x in range(num_clips):
        clips_arr.append(vid.subclip(vid.duration / num_clips * x, vid.duration / num_clips * (x + 1)))
    return clips_arr


def homogenize(clips_arr):
    while len(clips_arr) > 2:
        clips_arr[1] = clips_arr[0] + clips_arr[1]
        clips_arr.pop(0)

    while len(clips_arr[0]) != len(clips_arr[1]):  # make 2 same length
        if len(clips_arr[0]) > len(clips_arr[1]):
            clips_arr[0].pop(-1)
        else:
            clips_arr[1].pop(-1)

    return clips_arr


def lace_clips(clips_arr):
    temp_list = []
    for i in range(len(clips_arr[0])):
        temp_list.extend([clips_arr[0][i], clips_arr[1][i]])
    return temp_list

