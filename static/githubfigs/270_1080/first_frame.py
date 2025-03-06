from moviepy.editor import VideoFileClip
import os
import glob

for video_path in glob.glob('*.mp4'):
    print("正在处理视频文件：", video_path)
    clip = VideoFileClip(video_path)  
    
    # 获取不包括扩展名的视频文件名
    video_name = os.path.splitext(video_path)[0]
    
    # 创建对应的 .jpg 文件名
    image_path = video_name + ".jpg"
    
    # 保存视频的第一帧为 .jpg 文件
    clip.save_frame(image_path, t=0)  