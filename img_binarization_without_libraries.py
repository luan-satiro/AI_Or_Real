from PIL import Image

def binarize_image_manual(image_path, output_path="binarized_output.png", threshold=127):
    try:
        # Open the image using Pillow
        img = Image.open(image_path)
        # Convert to grayscale (L mode) to work with single pixel values
        img = img.convert('L')

        # Get pixel data and image dimensions
        pixels = img.load()
        width, height = img.size

        # Iterate over all pixels and apply the manual binarization
        for y in range(height):
            for x in range(width):
                # Get the pixel value (0-255)
                pixel_value = pixels[x, y]
                # Apply the threshold logic
                if pixel_value > threshold:
                    pixels[x, y] = 255  # Set to white
                else:
                    pixels[x, y] = 0   # Set to black

        # Save the resulting binary image
        img.save(output_path)
        print(f"Binarization complete. Image saved to {output_path}")
        return output_path

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")