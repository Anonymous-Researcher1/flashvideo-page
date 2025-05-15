for file in *.mp4
do
  ffmpeg -i "$file" -vf "scale=-1:1080" -c:v libx264 -preset veryslow -crf 23 "./compressed_videos/${file%.*}.mp4"
done