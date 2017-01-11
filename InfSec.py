import binascii, time, sys, os
if sys.version[0]=="3": # Check version (different input commands)
    raw_input=input
def rotateleft(x): # Rotates 3 digits to the left
    x=str(x)
    return x[3:]+x[:3]
def getBin(mystr): # Turns number to 8 bit binary
    return (bin(ord(mystr))[2:]).zfill(8)
def xor(x,y): # Returns the XOR between the two
    x = int(x,2)
    y = int(y,2)
    tmp = bin(x ^ y)[2:]
    return str(tmp).zfill(8)
def rotateXor(x1,x2): # AKA 'F' function
    x = rotateleft(x1)
    return xor(x,x2)
def makeMac(bins,ukey): # Makes the MAC
    tmp1 = rotateXor(bins[0],ukey)
    tmp2 = rotateXor(xor(bins[1],tmp1),ukey)
    tmp3 = rotateXor(xor(bins[2],tmp2),ukey)
    tmp4 = rotateXor(xor(bins[3],tmp3),ukey)
    return tmp4

def fFunc(val,ukey): # Gets a string and key and sends to makeMac
    binNums = [getBin(val[0]),getBin(val[1]),getBin(val[2]),getBin(val[3])]
    binkey = getBin(ukey)
    return makeMac(binNums,binkey)

def myfunc(input1,ukey,ans): # Looks for collisions with the found MAC
    count=0
    str1='abcdefghijklmnopqrstuvwxyz'
    for c in str1:
        for d in str1:
            for e in str1:
                for f in str1:
                    str2 = c+d+e+f
                    if( (fFunc(str2,ukey)==ans) and (str2!=input1) ):
                        count+=1

    return count

def printheader():

  print(' __   _ _______ ___ _______     ______ _______ __   ___  ______ __   __ ')
  print(' \ \ | |____   |_  |   __  |   |  __  |   __  |  | /_  ||____  |\ \ / / ')
  print('  \ \| |    | |  |_|| |  | |   | |  | || |  | || |   | |     | ||  V /  ')
  print(' __\ ` |    | |     | | _| |  _| |  | || |  | || |___| |_____| || |\ \ ')
  print('|______|    |_|     |_||___| |___|  |_||_|  |_||_______/________|_| \_\ ')

  print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
  print('        | Info Sec Hash ver 2.0 | by Roy Katz & Shiran Tayar  |')
  print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
  print('')
  print('Welcome to Shiran & Roy\'s project.')

def main():
  printheader()
  input1 = raw_input('To start, Please enter 4 small letters:')
  ukey = raw_input('Please enter a key:')
  ans = fFunc(input1,ukey)

  print("Output in binary: %s \nOutput as char: %s " % (ans, chr((int(ans,2)))))

  start_time = time.time()
  coll = myfunc(input1,ukey,ans)
  end_time = time.time()
  everyoption = 26*26*26*26
  tmp = 1. * coll/everyoption

  print("\nOverall collisions: %i out of %i options \nRatio is: %f" %(coll, everyoption, tmp))
  print("--- %s seconds runtime ---" % (end_time - start_time))
  os.system("pause")

main()
