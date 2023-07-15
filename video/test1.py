import cv2


def flip_video_frames(input_path, output_path):
    # 打开输入视频文件
    video_capture = cv2.VideoCapture(input_path)

    # 获取视频的基本信息
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 创建输出视频写入对象
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        # 读取视频的一帧
        ret, frame = video_capture.read()

        if not ret:
            break

        # 左右翻转图像
        flipped_frame = cv2.flip(frame, 1)

        # 写入翻转后的帧到输出视频
        video_writer.write(flipped_frame)

    # 释放资源
    video_capture.release()
    video_writer.release()


# 测试函数
input_video_path = './1.mp4'
output_video_path = 'output_video.mp4'
flip_video_frames(input_video_path, output_video_path)
