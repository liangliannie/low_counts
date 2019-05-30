import Augmentor
import numpy as np
import matplotlib.pylab as plt

corrupted = np.random.rand(5,400,400)
origin = np.random.rand(1,400,400)
images = [[image for image in corrupted] + [origin[0]]]

p = Augmentor.DataPipeline(images)
# p.rotate(1, max_left_rotation=5, max_right_rotation=5)
# p.flip_top_bottom(0.5)
# p.zoom_random(1, percentage_area=0.5)
p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
augmented_images = p.sample(1)
corrupted = np.stack([augmented_images[0][i] for i in range(5)])
origin = np.stack([augmented_images[0][i] for i in range(5,6)])

print(corrupted.shape, origin.shape)

# print(len(augmented_images))
# plt.figure(1)
# plt.imshow(corrupted[2])
# plt.figure(2)
# plt.imshow(augmented_images[0][2])
# plt.show()