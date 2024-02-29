import cv2
import matplotlib.pyplot as plt

def convert_color_space(image, conversion_flag):
    return cv2.cvtColor(image, conversion_flag)

def show_images(image_dict):
    plt.figure(figsize=(15, 15))
    for idx, (title, img) in enumerate(image_dict.items()):
        plt.subplot(1, len(image_dict), idx+1)
        if img.ndim == 2:
            plt.imshow(img, cmap='gray')
        else:
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(title)
    plt.show()


if __name__ == "__main__":
    image_path = "../img/Lenna.png"
    original_image = cv2.imread(image_path)

    conversions = {
        'Original': original_image,
        'Gray': cv2.COLOR_BGR2GRAY,
        'HSV': cv2.COLOR_BGR2HSV,
        'YCrCb': cv2.COLOR_BGR2YCrCb
    }
    converted_images =  {key: convert_color_space(original_image, value)  if key != 'Original' else value       for key, value in conversions.items()}


    show_images(converted_images)
