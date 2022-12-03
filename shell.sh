#!/bin/bash
echo hello world!
(python3 ./main.py $1)&
(python3 ./web.py $1)&

