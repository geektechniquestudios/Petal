from moviepy.editor import *
import math


def create_clips(vid: VideoFileClip):
    num_clips = math.ceil(vid.duration / 10)
    clips_list = []
    for x in range(num_clips):
        clips_list.append(vid.subclip(vid.duration / num_clips * x, vid.duration / num_clips * (x + 1)))
    return clips_list


def homogenize(clips_list):
    while len(clips_list) > 2:
        clips_list[1] = clips_list[0] + clips_list[1]
        clips_list.pop(0)

    while len(clips_list[0]) != len(clips_list[1]):  # make 2 same length
        if len(clips_list[0]) > len(clips_list[1]):
            clips_list[0].pop(-1)
        else:
            clips_list[1].pop(-1)

    return clips_list


def lace_clips(clips_list):
    temp_list = []
    for i in range(len(clips_list[0])):
        temp_list.extend([clips_list[0][i], clips_list[1][i]])
    return temp_list

