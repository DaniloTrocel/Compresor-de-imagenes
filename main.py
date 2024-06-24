from PIL import Image
import os 


def compress_image(image_folder):
    try:
        for file in os.listdir(image_folder):
            file_name, file_extension =os.path.splitext(image_folder + file)
            print('Comprimineto archivo: ', file_name + file_extension)

            if file_extension == '.jpg':
                file_compressed = Image.open(image_folder + file)
                file_compressed.save(file_name + 'comprimido.jpg', 
                                     quality=20, 
                                     optimize=True) 
    except Exception as e:
        print(f"Error: {e}")    

if __name__ == "__main__":
    compress_image('F:/Users/Administrador/Desktop/Jujutsu kaisen/')