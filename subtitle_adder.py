from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip

# Add video file
video = VideoFileClip("Example.mp4")

# Add subtitles
generator = lambda txt: TextClip(txt, fontsize=48, color='white')
subtitles = SubtitlesClip("Example.srt", generator)

# Add subtitles to video
video_with_subtitles = CompositeVideoClip([video, subtitles.set_position(('center', 'bottom'))])

# Generate the video with subtitles
video_with_subtitles.write_videofile("Example_Subtitles.mp4", codec='libx264', audio_codec='aac', fps=video.fps)
