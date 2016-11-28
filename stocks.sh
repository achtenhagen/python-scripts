#!/bin/bash

date=`date +%Y-%m-%d`
wget "http://online.wsj.com/mdc/public/page/2_3021-activnyse-actives.html" -O "${date}.html"