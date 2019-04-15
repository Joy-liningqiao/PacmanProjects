b'import binascii
int=int
range=range
len=len
pow=pow
False=False
open=open
iter=iter
Exception=Exception
str=str
None=None
OSError=OSError
sum=sum
getattr=getattr
True=True
list=list
binascii.unhexlify=binascii.unhexlify
binascii.b2a_base64=binascii.b2a_base64
binascii.hexlify=binascii.hexlify
import math
math.log=math.log
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzUc(msg,pubkey):
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczUg=int(math.log(pubkey[1],256))
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczUa=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczUg+1
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczgU=\'%%0%dx\'%(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczUa*2)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczga=msg.encode()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczaU=[]
 for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczag in range(0,len(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczga),pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczUg):
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUzg=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczga[pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczag:pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczag+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczUg]
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUzg+=b\'\\x00\'*(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczUg-len(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUzg))
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUza=int(binascii.hexlify(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUzg),16)
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUgz=pow(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUza,*pubkey)
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUga=binascii.unhexlify((pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczgU%pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUgz).encode())
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczaU.append(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUga)
 return b\'\'.join(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEczaU)
"""
submission_autograder.py: Local autograder client.
See README.md for a summary of how this program works.
Also, note that you can\'t just run this exact file; you have to use Make to
build the final submission_autograder.py file, then run that.
The build process (Makefile) #includes header.py and rsa.py here:
* header.py replaces the print statement with the Python 3 print() function.
* header.py replaces open with codecs.open; this must be done in header.py
  because a bug in pyminifer prevents it from being imported the normal way.
* rsa.py imports binascii and math.
* rsa.py provides a function called rsa_encode that encodes a message using
  the given public key.
"""
import base64
import hashlib
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEUaz=hashlib.sha256
import json
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEUag=json.dumps
import logging
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaz=logging.critical
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgUa=logging.debug
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgzU=logging.basicConfig
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgza=logging.DEBUG
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgUz=logging.CRITICAL
import os
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU=os.path
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEazg=os.listdir
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEaUz=os.environ
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEazU=os.getcwd
import platform
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEaUg=platform.uname
import re
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEagz=re.match
import shutil
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEagU=shutil.copyfile
import subprocess
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEUa=subprocess.PIPE
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEUg=subprocess.Popen
import sys
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEag=sys.argv
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEgU=sys.executable
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEga=sys.stdout
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEaU=sys.exit
import tempfile
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUEg=tempfile.mkdtemp
import time
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUga=time.gmtime
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUgE=time.strftime
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUEa=time.time
import urllib.request
import zipfile
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUaE=zipfile.ZipFile
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUaz=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUEa()
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUag=\'reinforcement\'
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgzU={\'tutorial\':\'https://inst.eecs.berkeley.edu/~cs188/fa18/assets/files/tutorial.zip\',\'search\':\'https://inst.eecs.berkeley.edu/~cs188/fa18/assets/files/search.zip\',\'multiagent\':\'https://inst.eecs.berkeley.edu/~cs188/fa18/assets/files/multiagent.zip\',\'reinforcement\':\'https://inst.eecs.berkeley.edu/~cs188/fa18/assets/files/reinforcement.zip\',\'bayesnets\':\'https://inst.eecs.berkeley.edu/~cs188/fa18/assets/files/bayesNets2.zip\',\'tracking\':\'https://inst.eecs.berkeley.edu/~cs188/fa18/assets/files/tracking.zip\',\'classification\':\'https://inst.eecs.berkeley.edu/~cs188/fa18/assets/files/classification_sp16.zip\',\'machinelearning\':\'https://inst.eecs.berkeley.edu/~cs188/fa18/assets/files/machinelearning.zip\'}
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgza={\'tutorial\':[\'shopSmart.py\',\'buyLotsOfFruit.py\',\'addition.py\'],\'search\':[\'searchAgents.py\',\'search.py\'],\'multiagent\':[\'multiAgents.py\'],\'reinforcement\':[\'analysis.py\',\'qlearningAgents.py\',\'valueIterationAgents.py\'],\'bayesnets\':[\'factorOperations.py\',\'inference.py\',\'bayesAgents.py\'],\'tracking\':[\'bustersAgents.py\',\'inference.py\'],\'classification\':[\'perceptron.py\',\'answers.py\',\'solvers.py\',\'search_hyperparams.py\',\'features.py\'],\'machinelearning\':[\'nn.py\',\'models.py\',\'perceptron.py\']}
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgUz=False
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgUa=\'1.4.0\'
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgaz=20000000 if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUag==\'machinelearning\' else 5000000
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgaU=[pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEgU or \'python\',\'autograder.py\',\'--mute\',\'--no-graphics\',\'--edx-output\']
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcazU=79
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcazg=\'%A, %B %d, %Y, %H:%M:%S\'
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcaUz=(33751518165820762234153612797743228623,56285023496349038954935919614579038707)
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcaUg=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgzU[pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUag].replace(\'https://\',\'http://\')
pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcagz=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgza[pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUag]
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzUa(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcga,width=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcazU,indent=0,right_margin=5):
 print(\' \'*indent+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcga+\'.\'*(width-len(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcga)-right_margin-indent),end=\'\')
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEga.flush()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzac(msg=\'DONE\',indent=1):
 print(\' \'*indent+msg)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEga.flush()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzaU(file_path,block_size=65536):
 if not pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.isfile(file_path):
  return \'(not file)\'
 if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.getsize(file_path)>pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgaz:
  return \'(file too big)\'
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcagU=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEUaz()
 with open(file_path,\'rb\')as f:
  for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUzg in iter(lambda:f.read(block_size),b\'\'):
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcagU.update(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUzg)
 return pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcagU.hexdigest()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUcz(file_path,mode=\'r\'):
 if not pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.isfile(file_path):
  return \'(not file)\'
 with open(file_path,mode)as f:
  return f.read()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUca():
 print(\'-\'*pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcazU,end=\'\
\
\')
 print(\'CS 188 Local Submission Autograder\')
 print(\'Version \'+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgUa,end=\'\
\
\')
 print(\'-\'*pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcazU,end=\'\
\
\')
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUzc():
 if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgUz:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcUg=\'submission_autograder.log\'
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgzU(format=\'%(asctime)s - %(levelname)s - %(message)s\',level=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgza,stream=open(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcUg,\'w\'))
 else:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgzU(format=\'\
ERROR - %(message)s\',level=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgUz)
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUza():
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcUa=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.dirname(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.realpath(__file__))
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcgU=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEazU()
 if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcgU!=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcUa:
  print(\'WARNING - Your current directory does not appear to be the project directory\')
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUac():
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzUa(\'Setting up environment\')
 try:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcga=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUEg(prefix=\'cs188-\')
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgUa(\'Temporary directory created at \'+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcga)
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzac()
  return pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcga
 except Exception as e:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaz(\'Could not create temp directory: \'+str(e))
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEaU(104)
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUaz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUagz,dest_dir):
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzUa(\'Downloading autograder\')
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgUa(\'Downloading from \'+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUagz)
 try:
  f=urllib.request.urlopen(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUagz)
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcaU=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.join(dest_dir,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.basename(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUagz))
  with open(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcaU,\'wb\')as pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcag:
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcag.write(f.read())
 except Exception as e:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaz(\'Download failed: \'+str(e))
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEaU(101)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgUa(\'Downloaded to \'+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcaU)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzac()
 return pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzcaU
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgacz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacU,dest_dir):
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzUa(\'Extracting autograder\')
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgUa(\'Extracting \'+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacU)
 with pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUaE(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacU)as f:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUcg=f.namelist()
  if len(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUcg)==0:
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaz(\'ZIP archive contains no files\')
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEaU(102)
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUca=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.join(dest_dir,f.namelist()[0])
  try:
   f.extractall(dest_dir)
  except Exception as e:
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaz(\'Extraction from zip file failed: \'+str(e))
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEaU(105)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgUa(\'Extracted inner directory \'+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUca)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzac()
 return pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUca
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgacU(dest_dir):
 print(\'Preparing student files:\')
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUcg=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgza[pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUag]
 for f in pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUcg:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzUa(f,width=40,indent=2)
  if not pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.isfile(f):
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaz(\'Could not find required file: \'+f)
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEaU(201)
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEagU(f,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.join(dest_dir,f))
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzac(\'OK\')
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgazc(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacg):
 print(\'Running tests (this may take a while):\')
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUgc=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag=\'\'
 try:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUga=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEUg(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcgaU,stdout=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEUa,cwd=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacg)
  for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac in iter(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUga.stdout.readline,b\'\'):
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac.decode()
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUgc+=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac.strip()
   if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEagz(r\'Question q\\d+$\',pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac):
    pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzUa(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac,width=40,indent=2)
   elif pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEagz(r\'### Question q\\d+: \\d+/\\d+ ###\',pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac):
    pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzac(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac.split(\': \')[1].strip(\'#\'))
   elif \'*** NOTE: Make sure to complete\' in pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac:
    pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzac(\'skipped\')
   elif pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEagz(r\'Total: \\d+/\\d+$\',pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac):
    pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac.split(\': \')[1]
   if \'ImportError\' in pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac:
    print(\'\
WARNING - Your code seems to have caused an ImportError\')
    print(\'          Make sure all of your code is in the files listed above\')
    print(\'          No additional files are allowed by the submission autograder\')
 except Exception as e:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaz(\'Autograder invocation failed: \'+str(e))
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEaU(103)
 finally:
  if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUga.poll()is None:
   try:
    pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUga.kill()
   except OSError:
    pass
 return pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUgc,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgazU(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacg,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUgc,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag):
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzUa(\'Generating submission token\')
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgcU=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEazg(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacg)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgca=[pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzaU(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.join(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacg,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcga))for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcga in pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgcU]
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgUc=[pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUcz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEgaU.join(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacg,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcga))for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcga in pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcagz]
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgUa={\'project\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUag,\'local_time\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUgE(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcazg),\'gmt_time\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUgE(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcazg,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUga()),\'duration_sec\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczUEa()-pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUaz,\'score\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag,\'raw_output\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUgc,\'self_contents\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUcz(__file__),\'current_dir\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEazU(),\'current_dir_ls\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEazg(\'.\'),\'work_dir\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacg,\'work_dir_ls\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgcU,\'work_dir_checksums\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgca,\'work_dir_student_files\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgUc,\'env\':str(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEaUz),\'os\':pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEaUg()}
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgac=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcUag+\'.token\'
 with open(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgac,\'wb\')as f:
  f.write(binascii.b2a_base64(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzUc(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEUag(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgUa),pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcaUz)))
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzac()
 return pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgac
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgaUc(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgac):
 print(\'\
\'+\'-\'*pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcazU,end=\'\
\
\')
 print(\'Final score: \'+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag)
 print(\'Token file: \'+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgac,end=\'\
\
\')
 print(\'Please make sure that this score matches the result produced by autograder.py.\',end=\'\
\')
 print(\'To submit your grade, upload the generated token file to Gradescope.\',end=\'\
\
\')
 print(\'If you encounter any problems, notify the course staff via Piazza.\',end=\'\
\
\')
 print(\'-\'*pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcazU)
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgaUz():
 if len(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEag)>1:
  print(\'This program does not accept any arguments.\')
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYczEaU(1)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUca()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUzc()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUza()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgaU=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUac()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacU=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgUaz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEcaUg,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgaU)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacg=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgacz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacU,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgaU)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgacU(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacg)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUgc,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgazc(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacg)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgac=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgazU(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzacg,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUgc,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgaUc(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzgac)
if __name__==\'__main__\':
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgaUz()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczU(choices):
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzaUc=sum(w for c,w in choices)
 r=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.uniform(0,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzaUc)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzaUg=0
 for c,w in choices:
  if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzaUg+w>=r:
   return c
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzaUg+=w
 assert False,"Shouldn\'t get here"
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczg(p=0.5):
 return pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.random()<p
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacUz(value,p=0.5):
 return value if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczg(p)else None
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacUg(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUczg,n,nonempty=False):
 if nonempty:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzagc=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(1,n)
 else:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzagc=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(n)
 return[pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUczg()for _ in range(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzagc)]
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacgz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUczg,n,attr):
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzagU=collections.OrderedDict()
 while len(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzagU)<n:
  v=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUczg()
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzagU[getattr(v,attr)]=v
 return pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzagU.values()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacgU():
 def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazcU():
  def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazcg(w):
   if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczg(0.9):
    return w
   return pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([\'`{}`\',\'_{}_\',\'*{}*\']).format(w)
  return \' \'.join(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazcg(w)for w in loremipsum.get_sentence().split())
 def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazUc():
  return \'{0} {1}\'.format(\'#\'*pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(1,7),loremipsum.get_sentence())
 def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazUg():
  return \'```{0}```\'.format(\'\
\'.join(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacUg(loremipsum.get_sentence,4)))
 def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazgc():
  return \'\
\'.join(\'* \'+s for s in pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacUg(loremipsum.get_sentence,4))
 def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazgU():
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUczg=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczU([(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazcU,7),(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazUc,1),(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazUg,1),(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazgc,1)])
  return pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUczg()
 return \'\
\
\'.join(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacUg(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEazgU,4,nonempty=True))
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUcz():
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcza=names.get_full_name()
 first_name,last_name=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcza.lower().split(\' \')
 return User(name=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacUz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcza,0.5),email=\'{0}{1}{2}{3}@{4}\'.format(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([first_name,first_name[0]]),pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice(string.ascii_lowercase)if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczg()else \'\',pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([last_name,last_name[0]]),pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(10)if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczg()else \'\',pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([\'berkeley.edu\',\'gmail.com\'])),is_admin=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczg(0.05))
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUcg():
 return Course(offering=\'{0}/{1}/{2}{3}\'.format(\'cal\',pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([\'cs61a\',\'ds88\']),pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([\'sp\',\'su\',\'fa\']),str(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(100)).zfill(2)),institution=\'UC Berkeley\',display_name=\'{0} {1}{2}\'.format(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([\'CS\',\'Data Science\']),pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(100),pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([\'\',\'A\'])),active=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczg(0.3))
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUzc(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacz):
 if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczg(0.5):
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcgz=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([\'Hog\',\'Hog Contest\',\'Maps\',\'Ants\',\'Scheme\'])
 else:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcgz=\'{0} {1}\'.format(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([\'Homework\',\'Lab\',\'Quiz\']),str(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(15)).zfill(2))
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcga=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacz.offering+\'/\'+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcgz.lower().replace(\' \',\'\')
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcaz=(datetime.datetime.utcnow().replace(hour=0,minute=0,second=0,microsecond=0)-datetime.timedelta(seconds=1))
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcaz=(pytz.timezone("America/Los_Angeles").localize(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcaz).astimezone(pytz.utc))
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcag=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcaz+datetime.timedelta(days=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(-100,100))
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzcg=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcag+pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([datetime.timedelta(minutes=15),datetime.timedelta(days=1)])
 return Assignment(name=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcga,course_id=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacz.id,display_name=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcgz,due_date=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUcag,lock_date=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzcg,max_group_size=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(1,3),revisions_allowed=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczg(0.3),files={\'fizzbuzz.py\':original_file})
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUzg(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazc,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacz):
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzca=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczU([(\'student\',100),(\'grader\',2),(\'staff\',20),(\'instructor\',2)])
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzgc=\'\'.join(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice(string.digits)for _ in range(8))
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzga=\'{0}-{1}\'.format(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacz.offering.split(\'/\')[1],\'\'.join(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice(string.ascii_lowercase)for _ in range(3)))
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzac=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(30)
 return Enrollment(user_id=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazc.id,course_id=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacz.id,role=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzca,sid=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacUz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzgc,0.4),class_account=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacUz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzga,0.4),section=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacUz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzac,0.4))
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUgc(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazc,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazg):
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzag={\'file_contents\':{\'fizzbuzz.py\':modified_file,\'moby_dick\':\'Call me Ishmael.\'},\'analytics\':{}}
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgcz=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczg(0.1)
 if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgcz:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzag[\'file_contents\'][\'submit\']=\'\'
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca=Backup(created=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazg.due_date-datetime.timedelta(seconds=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(-100000,100)),submitter_id=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazc.id,assignment_id=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazg.id,submit=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgcz)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca.messages=[Message(kind=k,contents=m)for k,m in pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUzag.items()]
 return pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUgz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca):
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgzc=datetime.datetime.now()-datetime.timedelta(minutes=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(100))
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUcg=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca.files()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgza=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice(list(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUcg))
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzagc=len(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUcg[pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgza].splitlines())
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzagc)+1
 return Comment(created=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgzc,backup_id=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca.id,author_id=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca.submitter.id,filename=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgza,line=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUac,message=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacgU())
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagcz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcza,kind="autograder"):
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgzc=datetime.datetime.now()-datetime.timedelta(minutes=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(100))
 if kind=="composition":
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(2)
 else:
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.uniform(0,100)
 return Score(created=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgzc,backup_id=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca.id,assignment_id=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca.assignment.id,grader_id=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcza.id,kind=kind,score=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag,message=loremipsum.get_sentence())
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagcU(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcaU):
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgzc=datetime.datetime.now()-datetime.timedelta(minutes=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.randrange(100))
 return GradingTask(created=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgzc,backup=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca,assignment=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca.assignment,course=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca.assignment.course,grader=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcaU)
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagzc():
 print(\'Seeding users...\')
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgac=[User(email=\'okstaff@okpy.org\',is_admin=True)]
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgac.extend(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacgz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUcz,30,\'email\'))
 db.session.add_all(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgac)
 db.session.commit()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagzU():
 print(\'Seeding courses...\')
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgaz=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacgz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUcg,4,\'offering\')
 db.session.add_all(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgaz)
 db.session.commit()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagUc():
 print(\'Seeding assignments...\')
 for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacz in Course.query.all():
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacg=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacgz(functools.partial(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUzc,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacz),5,\'name\')
  db.session.add_all(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacg)
 db.session.commit()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagUz():
 print(\'Seeding enrollments...\')
 for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazc in User.query.all():
  for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacz in Course.query.all():
   if not pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaczg(0.9):
    continue
   db.session.add(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUzg(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazc,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUacz))
 db.session.commit()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzUg():
 for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazc in User.query.all():
  print(\'Seeding backups for user {0}...\'.format(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazc.email))
  for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazg in Assignment.query.all():
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUagc=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacUg(functools.partial(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUgc,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazc,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUazg),30)
   db.session.add_all(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUagc)
  db.session.commit()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzUa():
 print(\'Seeding version...\')
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUagz=\'https://github.com/Cal-CS-61A-Staff/ok-client/releases/download/v1.5.4/ok\'
 ok=Version(name=\'ok-client\',current_version=\'v1.5.4\',download_link=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUagz)
 db.session.add(ok)
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzgU():
 print(\'Seeding comments...\')
 for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca in Backup.query.filter_by(submit=True).all():
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgczU=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEacUg(functools.partial(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEaUgz,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca),6)
  db.session.add_all(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgczU)
 db.session.commit()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzga():
 print(\'Seeding scores...\')
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcza=User.query.filter_by(is_admin=True).first()
 for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca in Backup.query.filter_by(submit=True).all():
  if pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice([True,False]):
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagcz(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcza)
   db.session.add(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEzUag)
 db.session.commit()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzaU():
 print(\'Seeding queues...\')
 for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcUz in Assignment.query.filter(Assignment.id%2==0):
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcUa=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcUz.course.get_staff()
  if not pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcUa:
   print("No staff for ",pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcUz.course)
   continue
  pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcaz=Backup.query.filter_by(submit=True,assignment=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcUz)
  for pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca in pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcaz.all():
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcaU=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.choice(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcUa)
   pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzcU=pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagcU(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEUgca,pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgcaU.user)
   db.session.add(pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzcU)
 db.session.commit()
def pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzag():
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEgzca.pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzag(0)
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagzc()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagzU()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagUc()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYEagUz()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzUg()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzgU()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzaU()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzga()
 pAMwLbjTdBtxWXkHSnePGIDJRvmQVurCqNsKhyiFoOflYcEzUa()
'
