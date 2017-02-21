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
def OMplayer_play(file,delay):
    spdkprint(file)
    play_process = subprocess.Popen(['omxplayer','-p','-o','local',file],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE, close_fds = True)
    time.sleep(delay)
    play_process.stdin.write('q')
    play_process.stdin.flush()

def Audio_Loop():
    OMplayer_play("Pink_pcm.wav",7)
    OMplayer_play("Pink_ac3.ac3",7)
    OMplayer_play("Pink_dts.dtshd",7)

#-------------------------------------------------------------------------------
if __name__ == "__main__":

    #if len(sys.argv) < 2:
    #    print 'Audio Test'
    #    sys.exit()

    #if(sys.argv[1] == 'test'):
        Audio_Loop()
    
