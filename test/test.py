from src.ClipManager import *


# test1 : cut vid in half and stick it back together switched
def test1(clip):
    part1: VideoClip = clip.subclip(0, clip.duration / 2)
    part2 = clip.subclip(clip.duration / 2, clip.duration)

    finished_video = concatenate_videoclips([part2, part1])
    finished_video.write_videofile("./test-video/output-test1.mp4")


# second test : mesh two vids of different res together
def test2(__clip1, __clip2):
    finished_video = concatenate_videoclips([__clip1, __clip2])
    finished_video.write_videofile("./test-video/output-test2.mp4")


def test3(clip):
    normalize_resolutions(clip)


#clip1 = VideoFileClip("../input-videos/clip1.mp4")
clip2 = VideoFileClip("../input-videos/clip2.mp4")
clip3 = VideoFileClip("../input-videos/clip3.mp4")

# test1(clip1)
# test2(clip3, clip2)
test3("../input-videos/clip2.mp4")

# Test 2 failed, meaning this tool has trouble with varying resolutions
