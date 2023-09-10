# step 1
import os
from scipy.io import loadmat
import imageio

# step 2
path = 'D:/AAA/'

# step 3
xMin = 111
xMax = 222
yMin = 333
yMax = 444

# step 4
trajectory = loadmat(path + 'trajectory.mat')
xx = trajectory[:, 0]
yy = trajectory[:, 1]

# step 5   
video = imageio.get_reader(path + 'video.mp4', 'ffmpeg')

# step 6
if video.count_frames() == len(xx) and video.count_frames() == len(yy):    
    print(video.count_frames())

# step 7        
    for frameNum in range(video.count_frames()):

# step 8            
        if xx[frameNum] > xMin and xx[frameNum] < xMax and yy[frameNum] > yMin and yy[frameNum] < yMax:
            image = video.get_data(frameNum)
            imageio.imwrite('image' + str(frameNum) + '.jpg', image)

# step 9     
video.close()
