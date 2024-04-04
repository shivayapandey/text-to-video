# 📹 Video Text Overlay ✨

This project is a Python script that allows you to overlay text onto a video file. It uses the `moviepy` library to create a new video with the specified text superimposed on the original video. 🎥📝

## 🌟 Features

1. **Text Overlay**: Add text to a video file. 📜
2. **Customizable Text Properties**: Adjust the font size, color, font style, and position of the text. 🎨
3. **Video Output**: Save the modified video with the text overlay to a new file. 💾

## 📋 Requirements

- Python 3.x 🐍
- moviepy 🎬

## 🚀 Installation

1. Clone the repository:


git clone https://github.com/shivayapandey/text-to-video.git

2. Navigate to the project directory:


cd video-text-overlay

3. Install the required dependencies:


pip install moviepy

## 🎬 Usage

1. Open the Python script in a text editor. 📝

2. Modify the following variables according to your requirements:

- `video_path`: The path to the input video file. 📂
- `output_path`: The path to save the output video file with the text overlay. 💾
- `text`: The text you want to overlay onto the video. 📝
- `fontsize`: The font size of the text (default is 50). 🔍
- `color`: The color of the text (default is 'white'). 🎨
- `font`: The path to a custom font file (optional, leave as `None` for the default font). 🖌️
- `x`: The horizontal position of the text (in pixels). ↔️
- `y`: The vertical position of the text (in pixels). ↕️

3. Run the script:


python video_text_overlay.py

The script will process the input video and create a new video file with the specified text overlay at the given position. 🎥✨





## Examples

### Input Video


https://github.com/shivayapandey/text-to-video/assets/143429039/c43778fd-c8eb-4c3f-9d4c-6f23b6f7ef2e



### Output Video with Text Overlay


https://github.com/shivayapandey/text-to-video/assets/143429039/4c525678-c695-450a-8083-38ccbae07553


### Input Video


https://github.com/shivayapandey/text-to-video/assets/143429039/d318e30b-ca1a-488a-bab5-47576f416f2b





### Output Video with Text Overlay



https://github.com/shivayapandey/text-to-video/assets/143429039/5241e304-6a73-4185-8043-f4d1e50354a4





In the above examples, the text "Your text here" is overlaid onto the input video with a font size of 50, white color, and positioned at (50, 50) pixels.

You can customize the text, font properties, and position to achieve different text animation effects.
## 🤝 Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. 🙌

## 📄 License

This project is licensed under the [MIT License](LICENSE). 📜

