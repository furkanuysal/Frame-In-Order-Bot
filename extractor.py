import cv2
import os

# Path of the video
video_path = 'example.mp4'

# Open the video
video = cv2.VideoCapture(video_path)

# Process video and extract frames
if video.isOpened():
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    save_folder = 'extracted_frames'
    os.makedirs(save_folder, exist_ok=True)

    for frame_index in range(0, frame_count, 24):  # Extract a frame in every 24 frames
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = video.read()

        if ret:
            save_path = os.path.join(save_folder, f"frame_{frame_index // 24 + 1}.jpg")
            cv2.imwrite(save_path, frame)
        else:
            break

    video.release()
    cv2.destroyAllWindows()
else:
    print("Video file could not be opened.")
