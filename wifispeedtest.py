print(2+2)

import speedtest

s = speedtest.Speedtest()

bytes_num = 1048576 # 1024*1024 

dws = round(s.download()/bytes_num, 2)

ups = round(s.upload()/bytes_num, 2)

print(f'Download speed is: {dws} Mbps')
print(f'Upload speed is: {ups} Mbps')
