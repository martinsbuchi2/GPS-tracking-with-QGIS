from PIL import Image
import os

def create_gif(image_folder, output_file, duration=500):
    """
    Creates an animated GIF from a series of images.
    
    Parameters:
        image_folder (str): The folder containing the image files.
        output_file (str): The output GIF file path.
        duration (int): Duration for each frame in milliseconds (default is 500ms).
    """
    # Get all image files from the folder, sorted by name
    images = [os.path.join(image_folder, file) for file in sorted(os.listdir(image_folder)) if file.endswith(('png', 'jpg', 'jpeg'))]
    
    if not images:
        print("No images found in the specified folder.")
        return

    # Open the images and store them in a list
    frames = [Image.open(image) for image in images]

    # Save the first image with the rest as an animated GIF
    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0  # 0 means the GIF will loop infinitely
    )

    print(f"GIF saved successfully at {output_file}")

# Example usage
if __name__ == "__main__":
    # Specify the folder containing the time-series images
    image_folder = "c:\\Users\\Marti\\Pictures\\GPS_Track\\Images"
    
    # Specify the output GIF file path
    output_file = "output_animation.gif"
    
    # Call the function to create the GIF
    create_gif(image_folder, output_file, duration=10)
