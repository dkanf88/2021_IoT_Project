import picamera
import time

path = '/home/pi/src4/06_multimedia'
now_str = time.strftime("%Y%m%d_%H%M%S")
camera = picamera.PiCamera()
camera.resolution = (640, 480)
while(True):
    camera.start_preview()
    num = input('photo: 1, video: 2, exit: 9 >')
    if num != '9':
        if num == '1': 
            time.sleep(3)
            camera.capture(path+'/photo_' + now_str+'.jpg')
            print('사진촬영')
            continue
        elif num == '2': 
            camera.start_recording(path+'/video_'+now_str+'.h264' )
            input('press enter to stop recording')
            camera.stop_recording()
            continue
        else: continue
    
    else: break

camera.stop_preview()