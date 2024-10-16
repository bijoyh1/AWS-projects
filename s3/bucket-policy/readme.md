## Create bucket
```sh
aws s3api create-bucket --bucket bucket-policy-examples-bs
```

## Set bucket policy
```sh
aws s3api put-bucket-policy --bucket bucket-policy-examples-bs --policy file:///workspace/AWS-projects/s3/bucket-policy/policy.json
```