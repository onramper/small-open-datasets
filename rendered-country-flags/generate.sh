echo "module.exports={" > index.js
for f in flags/*
do
 echo "Processing $f"
 filename=$(basename $f)
 encoded=$(base64 $f -w 0)
 echo "\"${filename%.*}\":\"data:image/png;base64,${encoded}\"," >> index.js
done
sed -i '$ s/,$/}/' index.js
