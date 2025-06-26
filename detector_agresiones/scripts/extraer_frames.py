import cv2
import os

def extract_frames_from_videos(video_dir, output_dir, label, frame_interval=5):
    os.makedirs(output_dir, exist_ok=True)
    video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.avi', '.mov'))]

    for video_file in video_files:
        video_path = os.path.join(video_dir, video_file)
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        saved = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % frame_interval == 0:
                filename = f"{label}_{os.path.splitext(video_file)[0]}_{saved:05}.jpg"
                cv2.imwrite(os.path.join(output_dir, filename), frame)
                saved += 1
            frame_count += 1
        cap.release()

if __name__ == "__main__":
    extract_frames_from_videos(
        video_dir="datasets/raw_videos/fight",
        output_dir="datasets/extracted_frames/fight",
        label="fight"
    )
    extract_frames_from_videos(
        video_dir="datasets/raw_videos/no_fight",
        output_dir="datasets/extracted_frames/no_fight",
        label="no_fight"
    )
