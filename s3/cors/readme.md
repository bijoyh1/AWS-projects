## Create bucket
```sh
aws s3api create-bucket --bucket cors-bucket-bs
```

## Turn off public access block from ACLs
```sh
aws s3api put-public-access-block --bucket cors-bucket-bs --public-access-block-configuration BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false
```

## Create a bucket policy
```sh
aws s3api put-bucket-policy --bucket cors-bucket-bs --policy file://bucket.json
```

## Turn on static website hosting
```sh
aws s3api put-bucket-website --bucket cors-bucket-bs --website-configuration file://website.json
```

## Upload index.html file and incude a resource that would be cross-origin
```sh
aws s3 cp index.html s3://cors-bucket-bs
```

## Create bucket
```sh
aws s3api create-bucket --bucket cors-bucket-bs1
```

http://cors-bucket-bs.s3-website-us-east-1.amazonaws.com

## Turn off public access block from ACLs
```sh
aws s3api put-public-access-block --bucket cors-bucket-bs1 --public-access-block-configuration BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false
```

## Create a bucket policy
```sh
aws s3api put-bucket-policy --bucket cors-bucket-bs1 --policy file://bucket-policy.json
```

## Turn on static website hosting
```sh
aws s3api put-bucket-website --bucket cors-bucket-bs1 --website-configuration file://website.json
```

## Upload index.html file and incude a resource that would be cross-origin
```sh
aws s3 cp index.html s3://cors-bucket-bs
```

## Add CORS file to S3

aws s3api put-bucket-cors --bucket cors-bucket-bs --cors-configuration file:///workspace/AWS-projects/s3/cors/cors.json