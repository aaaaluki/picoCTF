#!/bin/sh

hexStream="53616c7465645f5fbf1f3543c1437d489ac5c700f4809146799c9d503b551476a3f06159293bee7c9e5183fb5c4a184c"
echo $hexStream | xxd -r -p > file.des3
openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123 2&> /dev/null
cat file.txt
