import av

video_path = "./people1.mp4"
container = av.open(video_path)

for frame in container.decode(video=0):
    frame.to_image().save('./img/frame-%04d.jpg' % frame.index)