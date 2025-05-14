#!/bin/bash

FILE_ID="1BqT-PTSJD1Id0BHsffuUt_UGbYzig2C_"
FILE_NAME="xpl.tar"

CONFIRM=$(curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" | \
grep -o 'confirm=[^&]*' | sed 's/confirm=//')

curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CONFIRM}&id=${FILE_ID}" -o "${FILE_NAME}"

mkdir -p models
mv "${FILE_NAME}" models/
cd models
tar -xf "${FILE_NAME}"
rm "${FILE_NAME}"
