

from createToken import *
import sys


secret = int(sys.argv[1])

token = get_totp_token(secret)
print ("Auth Token: {0}".format(token))


