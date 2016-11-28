#!/bin/bash

function get_stocks() {
	date=`date +%Y-%m-%d`
	wget "http://online.wsj.com/mdc/public/page/2_3021-activnyse-actives.html" -O "${date}.html"
}

x=0
while [[ $x -le 60 ]]; do
	get_stocks
	sleep 3
	x=`expr $x + 1`
done