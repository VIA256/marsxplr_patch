# MARSP  ATCHM  ARSPA  TCHMA    RSPAT  CHMAR  SPATC  HMARS  P   A
# T C H  M   A  R   S  P        A   T  C   H    M    A      R   S
# P   A  TCHMA  RSPAT  CHMAR    SPATC  HMARS    P    A      TCHMA
# R   S  P   A  T C        H    M      A   R    S    P      A   T
# T   C  H   M  A  RS  PATCH    M      A   R    S    PATCH  M   A
# version 1.2





import os

def terminate():
    print('press ENTER to terminate script')
    input()
    quit()

#37da7 - 37dde (228775 - 228830)
print('IMPORTANT: this script must be placed in the same directory as Mars Explorer.exe, and be run as administrator, or it will not work')
print('this script makes changes to "Mars Explorer_Data/Assembly - UnityScript.dll".\nmaking a backup is suggested.')
print('do you want to apply this patch now? (Yy / Nn)')
if(input().lower() != 'y'):
    print('patch cancelled')
    terminate()

try:
    if(os.name == 'nt'):
        fname = 'Mars Explorer_Data\\Assembly - UnityScript.dll'
    else:
        fname = 'Mars Explorer_Data/Assembly - UnityScript.dll'
    f = open(fname, 'rb')
except:
    print(f'failed to open {fname}. no changes were made')
    terminate()

data = bytearray(f.read())
f.close()

newurl = bytes('73.189.4.24/upd3', 'ascii')
i = 228775
while(i <= 228830):
    data[i] = 0
    i += 1
i = 228775
j = 0
while(j < len(newurl)):
    data[i] = newurl[j]
    i += 2
    j += 1

#at address 00007f51 (32593):
#gameversion 2.22 (400E147B(be) = 7B140E40(le)) -> 2.3 (40133333(be) = 33331340(le))
i = 32593
gameverle = b'\x33\x33\x13\x40'
for b in gameverle:
    data[i] = b
    i += 1

#@ba44: botcount < 10->50
data[0xba44] = 0xff
#@ba9a: botcount != 10->50
data[0xba9a] = 0xff

try:
    f = open(fname, 'wb')
    f.write(bytes(data))
    f.close()
except:
    print(f'failed writing to {fname}. no changes were made. (try running as administrator?)')
    terminate()

f = open(fname, 'rb')
data = f.read()
f.close()
i = 228775
while(i <= 228830):
    i += 2

print('patch completed successfully')
terminate()
