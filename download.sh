$FILE_ID = "1BqT-PTSJD1Id0BHsffuUt_UGbYzig2C_"
$FILE_NAME = "xpl.tar"

gdown --id $FILE_ID -O $FILE_NAME
New-Item -ItemType Directory -Force -Path "model"
Move-Item $FILE_NAME -Destination "model"
Set-Location "model"
tar -xf $FILE_NAME
Remove-Item $FILE_NAME
