from PIL import Image

def png_to_jpg_with_black_background(png_path, jpg_path):
    """
    Converts a PNG image to a JPG image with a black background.

    Args:
        png_path (str): The path to the input PNG file.
        jpg_path (str): The path to save the output JPG file.
    """
    try:
        # Open the PNG image
        png_image = Image.open(png_path).convert('RGBA')

        # Create a new image with a black background
        # It's the same size as the PNG
        black_background = Image.new('RGB', png_image.size, (0, 0, 0))

        # Paste the PNG image onto the black background
        black_background.paste(png_image, (0, 0), png_image)

        # Save the result as a JPEG
        black_background.save(jpg_path, 'JPEG')

        print(f"Successfully converted '{png_path}' to '{jpg_path}'")
    except FileNotFoundError:
        print(f"Error: The file '{png_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example Usage ---
# Replace 'input.png' with the path to your PNG file
# Replace 'output.jpg' with the desired output path
png_to_jpg_with_black_background('sm-logo.png', 'sm-logo.jpg')