import os
import time

frame = 1
num_frames = 10
linux_path = '/home/aditya/Programming/Capstone/Multi-Node-App/frame_data/'
alt_path = '/home/aditya/Programming/Capstone/Multi-Node-App/test_frames/'
fname_mw = 'Mike_Frame{}.json'.format(frame)
fname_p = 'Patrick_Frame{}.json'.format(frame)

while (frame <= num_frames):
    os.rename(alt_path + 'Mike_Frame{}.json'.format(frame), linux_path + 'Mike_Frame{}.json'.format(frame))
    os.rename(alt_path + 'Patrick_Frame{}.json'.format(frame), linux_path + 'Patrick_Frame{}.json'.format(frame))
    frame+=1
    time.sleep(0.5)