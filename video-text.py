# Import the necessary modules from the Pillow library.
# Pillow is a powerful image processing library for Python.
import subprocess
import os
import sys
from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(text, filename="output.png", width=800, height=600, font_path='./font/RubikGlitch-Regular.ttf', max_font_size=80, min_font_size=10):
    """
    Generates a PNG image with specified text on a black background.
    The font size is adjusted so the widest line fits the image width.
    """
    try:
        img = Image.new('RGB', (width, height), color=(0, 0, 0))
        d = ImageDraw.Draw(img)

        # Split text into lines
        lines = text.split('\n')

        # Find the largest font size that fits the widest line
        font_size = max_font_size
        while font_size >= min_font_size:
            try:
                font = ImageFont.truetype(font_path, font_size)
            except IOError:
                print("Font not found, using default Pillow font.")
                font = ImageFont.load_default()
                break  # Can't resize default font, so break

            line_widths = [d.textbbox((0, 0), line, font=font)[2] - d.textbbox((0, 0), line, font=font)[0] for line in lines]
            if max(line_widths) <= width * 0.95:  # Leave a small margin
                break
            font_size -= 1

        # Now measure heights with the chosen font
        line_sizes = [d.textbbox((0, 0), line, font=font) for line in lines]
        line_heights = [bbox[3] - bbox[1] for bbox in line_sizes]
        total_text_height = sum(line_heights)
        line_spacing = 10
        total_text_height += line_spacing * (len(lines) - 1)

        # Start drawing from vertical center
        y = (height - total_text_height) / 2

        for i, line in enumerate(lines):
            x = (width - (line_sizes[i][2] - line_sizes[i][0])) / 2
            d.text((x, y), line, fill=(255, 255, 255), font=font)
            y += line_heights[i] + line_spacing

        img.save(filename)
        print(f"Image '{filename}' saved successfully with font size {font_size}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
	text1 = "The end is near\nno one can stop it\n\nThe end is near\nno one can stop it"
	text2 = "S a n t a M u e r t e\nSantaMuerte\nS a n t a M u e r t e\nSantaMuerte\nS a n t a M u e r t e\nSantaMuerte\nS a n t a M u e r t e\nSantaMuerte\n"
	#create_image_with_text(text1, "output1.png")
	#create_image_with_text(text2, "output2.png")
    

	file1 = os.path.join(os.getcwd(), 'giphy.gif')
	file2 = os.path.join(os.getcwd(), 'sm-logo-scale.jpg')
	file3 = os.path.join(os.getcwd(), 'output2.png')
	video_dir = 'videos/Reductions'	

        #video_dir = 'videos/Beziers'
	video_files = []
	video_files = [f for f in os.listdir(video_dir) if os.path.isfile(os.path.join(video_dir, f)) and f.endswith('.mp4')]

	playlist_files = [os.path.join(video_dir, f) for f in video_files]
	#playlist_files = [ file2] + [os.path.join(video_dir, f) for f in video_files]




	parameters_vlc = [
		'--no-audio',
		'--fullscreen',
                '--crop=4:3', #crop for crt 
		'--image-duration=5',
		'--no-video-title-show',
		'--file-caching=2000',
                '--loop',
                '--random'
	]
	parameters_mpv = [
		'--no-audio',
		'--fs',
                '--loop-playlist',
                '--image-display-duration=5'
	]
	subprocess.run(['cvlc', *parameters_vlc, *playlist_files])
	#subprocess.run(['mpv', *parameters_mpv, *playlist_files])

