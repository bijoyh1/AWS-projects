## Create bucket
```sh
aws s3api create-bucket --bucket acl-examples-bs
```

## Turn off public access block from ACLs
```sh 
aws s3api put-public-access-block --bucket acl-examples-bs --public-access-block-configuration BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=true,RestrictPublicBuckets=true
```

## Get the public access settings
```sh
aws s3api get-public-access-block --bucket acl-examples-bs
```

## Set Ownership control to bucket owner
```sh
aws s3api put-bucket-ownership-controls --bucket acl-examples-bs --ownership-controls Rules=[{ObjectOwnership=BucketOwnerPreferred}]
```

## Set full permissions for second user
```sh
aws s3api put-bucket-acl --bucket acl-examples-bs --access-control-policy file:///workspace/AWS-projects/s3/acl/policy.json
```
## Access bucket from other account
```sh
aws s3 ls s3://acl-examples-bs
```