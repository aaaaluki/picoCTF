#!/bin/sh

flag=$(cat KeygenMe.java | grep charAt | cut -d "'" -f2 | tac | sed 's/\n//g')

echo $flag | sed 's/ //g'
