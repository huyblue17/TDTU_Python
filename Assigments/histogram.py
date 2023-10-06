import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image):
    # Tính toán histogram
    histogram, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

    # Tính toán hàm tích lũy của histogram
    cdf = histogram.cumsum()
    cdf_normalized = cdf * histogram.max() / cdf.max()

    # Ánh xạ giá trị mức xám mới bằng cách sử dụng hàm tích lũy chuẩn hóa
    image_equalized = np.interp(image.flatten(), bins[:-1], cdf_normalized).reshape(image.shape)

    return image_equalized

# Đọc ảnh xám từ file
image = plt.imread('park.jpg')

# Chuyển đổi ảnh sang mức xám
image_gray = np.mean(image, axis=2)

# Áp dụng Histogram Equalization
image_equalized = histogram_equalization(image_gray)

# Hiển thị ảnh gốc
plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title('Original Image')

# Biểu đồ độ sáng pixel ảnh gốc
plt.subplot(2, 2, 2)
pixel_intensity_original = np.arange(256)
histogram_original, _ = np.histogram(image_gray.flatten(), bins=256, range=[0, 256])
plt.plot(pixel_intensity_original, histogram_original, color='b')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('Pixel Intensity (Original Image)')

# Hiển thị ảnh đã chỉnh sửa
plt.subplot(2, 2, 3)
plt.imshow(image_equalized, cmap='gray')
plt.title('Equalized Image')

# Biểu đồ độ sáng pixel ảnh đã chỉnh sửa
plt.subplot(2, 2, 4)
pixel_intensity_equalized = np.arange(256)
histogram_equalized, _ = np.histogram(image_equalized.flatten(), bins=256, range=[0, 256])
plt.plot(pixel_intensity_equalized, histogram_equalized, color='r')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('Pixel Intensity (Equalized Image)')

plt.tight_layout()
plt.show()