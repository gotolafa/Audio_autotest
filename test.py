import re
import os
import sys
import shutil
import chardet
import time

#----------------------------------------------------------------------
def Audio_Loop():
    count = 0
    print "Start test"

    os.system('omxplayer -audio_fifo 10 -p -o hdmi Pink_pcm.wav')
    time.sleep(7)
    os.system('q')
    os.system('omxplayer -audio_fifo 10 -p -o hdmi Pink_ac3.ac3')
    time.sleep(7)
    os.system('q')
    os.system('omxplayer -audio_fifo 10 -p -o hdmi Pink_dts.dtshd')
    time.sleep(7)
    os.system('q')  
    

#----------------------------------------------------------------------
if __name__ == "__main__":

    #if len(sys.argv) < 2:
    #    print 'Audio Test'
    #    sys.exit()

    #if(sys.argv[1] == 'test'):
        Audio_Loop()
    
