from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_text_to_video(video_path, text, output_path, fontsize=50, color='white', font=None, x=50, y=50):
    video_clip = VideoFileClip(video_path)
    text_duration = video_clip.duration
    
    # Create a text clip
    if font is not None:
        text_clip = TextClip(text, fontsize=fontsize, color=color, font=font).set_duration(text_duration)
    else:
        text_clip = TextClip(text, fontsize=fontsize, color=color).set_duration(text_duration)
    
    # Overlay text onto the video
    final_clip = CompositeVideoClip([video_clip.set_pos((0, 0)), text_clip.set_pos((x, y))], size=video_clip.size)
    
    # Write the final video to a file
    final_clip.write_videofile(output_path, codec='libx264', fps=24)

if __name__ == "__main__":
    video_path = '/Users/shivayapandey/Downloads/input2.mp4'  # Path to the input video
    output_path = '/Users/shivayapandey/Downloads/output_video2.mp4'  # Path to save the output video
    text = "made by shivaya"  # Text to overlay onto the video

    # Customize text properties
    fontsize = 50
    color = 'red'
    font = None  # Change this to the path of your font file if needed
    x = 80  # Adjust the horizontal position of the text (in pixels)
    y = 80  # Adjust the vertical position of the text (in pixels)
    
    add_text_to_video(video_path, text, output_path, fontsize, color, font, x, y)