#!/bin/bash

FILE_ID="1BqT-PTSJD1Id0BHsffuUt_UGbYzig2C_"
OUTPUT_FILE="xpl.tar"

curl -L -o $OUTPUT_FILE "https://drive.google.com/uc?export=download&id=${FILE_ID}"

mkdir -p models
mv $OUTPUT_FILE models/
cd models
tar -xf $OUTPUT_FILE
rm $OUTPUT_FILE
