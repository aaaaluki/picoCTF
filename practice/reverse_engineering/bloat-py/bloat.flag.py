import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

def happy_func(happychance):
  if happychance == 'happychance':
    return True
  else:
    print('That password is incorrect')
    sys.exit(0)

def decode_contents(file_contents):
  return xor_smth(file_contents.decode(), 'rapscallion')

def ask_input():
  return input('Please enter correct password for flag: ')

def read_file():
  return open('flag.txt.enc', 'rb').read()

def welcome_flag():
  print('Welcome back... your flag, user:')

def xor_smth(file_decoded, rapscallion):
    i = 0
    while len(rapscallion) < len(file_decoded):
        rapscallion = rapscallion + rapscallion[i]
        i = (i + 1) % len(rapscallion)        
    return "".join([chr(ord(d) ^ ord(r)) for (d, r) in zip(file_decoded, rapscallion)])

file_contents = read_file()
happychance = ask_input()
happy_func(happychance)
welcome_flag()
flag = decode_contents(file_contents)
print(flag)
sys.exit(0)

