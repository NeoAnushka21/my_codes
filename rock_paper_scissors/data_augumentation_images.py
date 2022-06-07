import Augmentor

from keras.preprocessing.image import ImageDataGenerator

""" Applying augmentation on images- increase the dataset and make it more generic to avoid overfitting"""

p_paper = Augmentor.Pipeline(r"/home/neosoft/Downloads/RPS_testing/paper")
p_paper.zoom(probability=0.3, min_factor=0.3, max_factor=1.2)
p_paper.flip_top_bottom(probability=0.4)
p_paper.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
p_paper.sample(500)

p_rock = Augmentor.Pipeline(r"/home/neosoft/Downloads/RPS_testing/rock")
p_rock.zoom(probability=0.3, min_factor=0.3, max_factor=1.2)
p_rock.flip_top_bottom(probability=0.4)
p_rock.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
p_rock.sample(500)

p_scissors = Augmentor.Pipeline(r"/home/neosoft/Downloads/RPS_testing/scissors")
p_scissors.zoom(probability=0.3, min_factor=0.3, max_factor=1.2)
p_scissors.flip_top_bottom(probability=0.4)
p_scissors.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
p_scissors.sample(500)
