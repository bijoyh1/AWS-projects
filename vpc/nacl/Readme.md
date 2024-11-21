## Get VPC ID
```sh
aws ec2 describe-vpcs \
--filters "Name=tag:Name,Values=nacl-example-vpc" \
--query "Vpcs[*].VpcId" \
--output text
```
## NACL

```sh
aws ec2 create-network-acl --vpc-id vpc-0c0d7415fb92ba2c5
```