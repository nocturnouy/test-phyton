
import subprocess
import os
import sys




# --- Main execution block ---
if __name__ == "__main__":

	video_dir = 'videos/tv'	

	video_files = [f for f in os.listdir(video_dir) if os.path.isfile(os.path.join(video_dir, f)) and f.endswith('lse-1.mp4')]

	playlist_files = [os.path.join(video_dir, f) for f in video_files]




	parameters_vlc = [
		'--fullscreen',
		'--avcodec-dr',
		
		'--audio',
		'--gain=4',
		'--sout-mono-downmix',
		'--equalizer-preamp=20',
		'--gain-value=4'
                '--crop=4:3', #crop for crt 
		'--no-video-title-show',
		'--file-caching=2000',
                '--loop'
	]

	subprocess.run(['cvlc', *parameters_vlc, *playlist_files])


