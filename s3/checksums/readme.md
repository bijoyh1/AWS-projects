## Create a new s3 bucket


```md
aws s3 mb s3://checksums-examples-bs-1234
````

## Create a file that we wil ldo a checksum on

```echo "Hello Mars" > myfile.txt
```

## Get a checksum of a file
 md4sum myfile.txt

## 8ed2d86f12620cdba4c976ff6651637f myfile.txt


## Upload our file to s3
aws s3 cp myfile.txt s3://checksums-examples-bs-1234
aws s3api head-object --bucket checksums-examples-bs-1234 --key myfile.txt

## Lets upload a file with a different kind of checksum

``` sh
aws s3api put-object \
--bucket="checksums-examples-bs-1234" \
--body="myfile.txt" \
--key="myfilesha1.txt" \
--checksum-algorithm="SHA1" \
--checksum-sha1="wozMLF4hQDaAYBTfn7Q2NPPncLI="
```

rhash --crc32 --simple myfile.txt 
## e7c80b87  myfile.txt