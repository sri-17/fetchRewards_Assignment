#!/bin/bash
pwd=$(pwd)
ssh-keygen -t rsa -b 4096 -C $1 -f $pwd/$1_rsa -q -P ""
ssh-keygen -t rsa -b 4096 -C $2 -f $pwd/$2_rsa -q -P ""
# cat $pwd/$1_rsa.pub
# cat $pwd/$2_rsa.pub