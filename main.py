from PIL import Image

def compress_image(input_image, output_image, max_size):
    # Open the image
    with Image.open(input_image) as img:
        # Get the current size 
        width, height = img.size
        # Calculate the new size 
        if width > height:
            new_width = max_size
            new_height = int(height * max_size / width)
        else:
            new_height = max_size
            new_width = int(width * max_size / height)
        # Resize the image
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        # Save the compressed image
        img.save(output_image, optimize=True, quality=85)

max_size = 800
counter= 1
num_file= 16 #number of images to compress
while True:
    #name your images consecutive like E1 E2 
    input_image = f'E{counter}.png' #input image path
    output_image = f'output{counter}.png' #output image path
    compress_image(input_image, output_image, max_size)
    counter+=1
    if counter>num_file:
        break
