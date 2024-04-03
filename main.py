from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_text_to_video(video_path, text, output_path):
    video_clip = VideoFileClip(video_path)
    text_duration = video_clip.duration
    
    # Create a text clip
    text_clip = TextClip(text, fontsize=50, color='white').set_duration(text_duration)
    
    # Overlay text onto the video
    final_clip = CompositeVideoClip([video_clip, text_clip])
    
    # Write the final video to a file
    final_clip.write_videofile(output_path, codec='libx264', fps=24)

if _name_ == "_main_":
    video_path = '/Users/krishkatyal/Downloads/input.mp4'  # Path to the input video
    output_path = '/Users/krishkatyal/Downloads/output_video.mp4'  # Path to save the output video
    text = "Your text here"  # Text to overlay onto the video

    add_text_to_video(video_path, text, output_path)