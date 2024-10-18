## Create a bucket 
```sh
aws s3api create-bucket --bucket encryption-bucket-bs
```

## Create a file
```sh
echo "Hello World!" >>hello.txt
aws s3 cp hello.txt s3://encryption-bucket-bs
```

## Put object with KMS
```sh
export BASE64_ENCODED_KEY=$(openssl rand 32 | base64)
export MD5_VALUE=$(echo $BASE64_ENCODED_KEY | md5sum | awk '{print $1}' | base64 -w0)

aws s3api put-object \
--bucket encryption-bucket-bs  \
--key hello.txt \
--body hello.txt \
--sse-customeralgorithm AES256 \
--ss3-customer-key $BASE64_ENCODED_KEY \
# --sse-customer-key-md5 $MD5_VALUE


aws s3 cp hello.txt s3://encryption-bucket-bs \
--sse-c AES356 \
000sse-c-key file://