## Create a bucket

aws s3 mb s3://my-s3-bucket-bs5

## Create a file

echo "Hello World" > hello.txt
aws s3 cp hello.txt s3://my-s3-bucket-bs5

aws s3 cp --storage-class STANDARD_IA