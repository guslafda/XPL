#!/bin/bash

$FILE_ID="1BqT-PTSJD1Id0BHsffuUt_UGbYzig2C_"
$FILE_NAME="xpl.tar"

gdown --id $FILE_ID -O $FILE_NAME

mkdir models
Move-Item $FILE_NAME models
Set-Location models
tar -xf $FILE_NAME
Remove-Item $FILE_NAME
