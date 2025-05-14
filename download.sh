#!/bin/bash

FILE_ID="1BqT-PTSJD1Id0BHsffuUt_UGbYzig2C_"
FILE_NAME="xpl.tar"

gdown --id $FILE_ID -O $FILE_NAME

mkdir -p models
mv $FILE_NAME models/
cd models
tar -xf $FILE_NAME
rm $FILE_NAME
