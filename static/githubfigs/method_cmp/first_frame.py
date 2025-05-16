import cv2
import os

video_dir = '/Users/bytedance/Desktop/merge/merge2/'

for filename in os.listdir(video_dir):
    if filename.endswith('.mp4'):
        video_path = os.path.join(video_dir, filename)
        img_path = os.path.join(video_dir, filename.rsplit('.', 1)[0] + '.jpg')
        
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(img_path, frame)
            print(f'Saved first frame of {filename} as {img_path}')
        else:
            print(f'Failed to read {filename}')
        cap.release()
