import re
import os
import sys
import shutil
import chardet
import time
import subprocess
#-------------------------------------------------------------------------------
global play_process
#-------------------------------------------------------------------------------
def Audio_Loop():
    count = 0
    print "Start test"

    play_process = subprocess.Popen(['omxplayer','-p','Pink_pcm.wav'],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE, close_fds = True)
    #os.system('omxplayer -audio_fifo 10 -p -o hdmi Pink_pcm.wav')
    time.sleep(7)
    play_process.stdin.write('q')
    play_process.stdin.flush()
    play_process = subprocess.Popen(['omxplayer','-p','Pink_ac3.ac3'],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE, close_fds = True)
    #os.system('omxplayer -audio_fifo 10 -p -o hdmi Pink_ac3.ac3')
    time.sleep(7)
    play_process.stdin.write('q')
    play_process.stdin.flush()
    play_process = subprocess.Popen(['omxplayer','-p','Pink_dts.dtshd'],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE, close_fds = True)
    #os.system('omxplayer -audio_fifo 10 -p -o hdmi Pink_dts.dtshd')
    time.sleep(7)
    play_process.stdin.write('q')
    play_process.stdin.flush()
    

#-------------------------------------------------------------------------------
if __name__ == "__main__":

    #if len(sys.argv) < 2:
    #    print 'Audio Test'
    #    sys.exit()

    #if(sys.argv[1] == 'test'):
        Audio_Loop()
    
