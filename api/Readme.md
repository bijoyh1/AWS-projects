## Create a user with no permissions and generate access key
```sh
aws iam create-user --user-name bijoy

aws iam create-access-key --user-name bijoy
```
## AWS Configure, copy access key and secret

## Create a role 

```sh
aws iam put-user-policy \
    --user-name bijoy \
    --policy-name StsAssumePolicy \
    --policy-document file://policy.json

```
## Use new user credentials and assume role

```sh
aws sts assume-role \
    --role-arn arn:aws:iam::905315126713:role/sts-fun-bs-StsRole-kwzgrusk9W3O \
    --role-session-name s3-sts-fun \
    --profile sts
```

## Read buckets
``` s3
aws s3 ls --profile assumed 
```

## Cleanup
```sh 
aws iam delete-user-policy --user-name bijoy --policy-name StsAssumePolicy 

aws iam delete-access-key --access-key-id AKIA5FSH4RW4SFR4GXLS --user-name bijoy

aws iam delete-user --user-name bijoy

aws 

```
