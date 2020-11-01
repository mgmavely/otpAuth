# otpAuth
Sample OTPAuthenticator using twilio and python scripts

NOTE1: For python scripts to use twilio, one must run 'pip install twilio' in
terminal/cmd.  Additionally, when importing twillio libraries such as
twilio.rest used in this code, it may be required to run 'sudo pip3 install
twilio --upgrade'.
  
NOTE2: twillvar.py file is ommitted as it contains private details
to twilio account, which one would need to input themselves.  For consistency
with variables used in pyScript.py, make twilVar.py as follows:  
  
import os  
from twilio.rest import Client  
  
acc_sid = '[insert account SID here]'  
auth_tok = '[insert account authentication token here]'  
twilNum = '[insert twilio phone number here]'  
client = Client(acc_sid,auth_tok)  

if done correctly and both files are placed in the same directory, running the
pyscript.py file should send the authentication code to the inputted number
and run as desired.
