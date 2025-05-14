#!/bin/bash

LINK_ID="1BqT-PTSJD1Id0BHsffuUt_UGbYzig2C_"
OUTPUT_FILE="xpl.tar"

CONFIRM=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=$LINK_ID" -O- | sed -rn 's/.*name="confirm" value="([0-9A-Za-z_]+)".*/\1\n/p')
UUID=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=$LINK_ID" -O- | sed -rn 's/.*name="uuid" value="([0-9A-Za-z_-]+)".*/\1\n/p')

wget --no-check-certificate --load-cookies /tmp/cookies.txt \
"https://drive.usercontent.google.com/download?export=download&id=$LINK_ID&confirm=$CONFIRM&uuid=$UUID" \
-O $OUTPUT_FILE && rm -f /tmp/cookies.txt

mkdir -p models
mv $OUTPUT_FILE models/
cd models
tar -xf $OUTPUT_FILE
rm $OUTPUT_FILE
