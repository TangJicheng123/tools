from moviepy.editor import VideoFileClip


def copy_audio(source_video_file, target_video_file, output_video_file):
    video1 = VideoFileClip(source_video_file)
    video2 = VideoFileClip(target_video_file)

    audio = video1.audio

    video2 = video2.set_audio(audio)

    video2.write_videofile(output_video_file)
