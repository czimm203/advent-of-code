#!/bin/bash

day=$1

mkdir $day
mkdir ${day}/bin
touch ${day}/main.cpp
touch ${day}/test.txt
touch ${day}/input.txt
cp ./Makefile ./${day}

