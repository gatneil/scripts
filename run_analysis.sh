#!/bin/bash

set -evx

# install dependencies
sudo apt update -y
sudo apt dist-upgrade -y
sudo apt install python-pip -y
sudo pip install numpy sumy
python -c "import nltk; nltk.download('punkt')"

# download data
wget https://tr24seven.blob.core.windows.net/text/7.tar.gz
tar -xzvf 7.tar.gz
grep -R "" 7/ | cut -d ":" -f 2 > text.txt
r=$RANDOM
tail -n +$r text.txt | head -1000 > sampleText.txt

# do analysis
sumy lex-rank --length=10 --file=sampleText.txt > res$r.txt

wget https://raw.githubusercontent.com/gatneil/scripts/master/tmp

scp res$r.txt negat@13.76.81.242:~/res/ -i tmp
