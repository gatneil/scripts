#!/bin/bash

# install dependencies
sudo apt install python-pip -y
sudo pip install numpy sumy
python -c "import nltk; nltk.download('punkt')"

# download data
wget https://tr24seven.blob.core.windows.net/text/7.tar.gz
tar -xzvf 7.tar.gz
grep -R "" 7/ | cut -d ":" -f 2 > text.txt
tail -n +$RANDOM text.txt | head -1000 > sampleText.txt

# do analysis
sumy lex-rank --length=10 --file=sampleText.txt > res$RANDOM.txt
