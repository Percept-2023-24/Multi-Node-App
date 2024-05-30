import os
import time
import json

frame = 1
num_frames = 30
linux_path = '/home/aditya/Programming/Capstone/Multi-Node-App/frame_data/'
alt_path = '/home/aditya/Programming/Capstone/Multi-Node-App/test_frames3/'
fname_mw = 'Mike_Frame{}.json'.format(frame)
fname_p = 'Patrick_Frame{}.json'.format(frame)

time.sleep(3)
while (frame <= num_frames):
    os.rename(alt_path + 'Mike_Frame{}.json'.format(frame), linux_path + 'Mike_Frame{}.json'.format(frame))
    # time.sleep(0.1)
    os.rename(alt_path + 'Patrick_Frame{}.json'.format(frame), linux_path + 'Patrick_Frame{}.json'.format(frame))
    frame+=1
    time.sleep(.3)

frame = 1
while (frame <= num_frames):
    os.rename(linux_path + 'Mike_Frame{}.json'.format(frame), alt_path + 'Mike_Frame{}.json'.format(frame))
    os.rename(linux_path + 'Patrick_Frame{}.json'.format(frame), alt_path + 'Patrick_Frame{}.json'.format(frame))
    frame+=1

# fname = '/home/aditya/Programming/Capstone/Multi-Node-App/test.json'

# try: 
#     data = json.load(open(fname, 'r'))
#     angle = data['Angle']   
#     print(angle)
# except JSONDecodeError as e:
#     print('file empty')