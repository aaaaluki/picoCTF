#!/bin/sh

openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
cat flag.txt
