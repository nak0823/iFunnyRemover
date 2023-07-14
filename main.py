from PIL import Image
import os

def remove_bottom(image_path, pixels_to_remove, output_directory):
    image = Image.open(image_path)

    width, height = image.size

    new_height = height - pixels_to_remove

    cropped_image = image.crop((0, 0, width, new_height))

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    filename = os.path.splitext(os.path.basename(image_path))[0]

    cropped_image.save(os.path.join(output_directory, f"{filename}_cropped.png"))

    print(f"Cropped image: {os.path.join(output_directory, f'{filename}_cropped.png')}")

directory_path = input("Enter the directory path: ")

pixels_to_remove = 22

output_directory = os.path.join(directory_path, "Cropped")

for filename in os.listdir(directory_path):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        file_path = os.path.join(directory_path, filename)

        remove_bottom(file_path, pixels_to_remove, output_directory)
