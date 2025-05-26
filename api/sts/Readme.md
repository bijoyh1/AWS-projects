## Create a user with no permissions and generate access key
```sh
aws iam create-user --user-name sts-machine-user

aws iam create-access-key --user-name sts-machine-user --output table
```
Copy the access key and secret here
````sh
aws configure
````
Then edit credentials file to change away from default profile


Test who you are:
````sh
aws sts get-caller-identity --profile sts
````

Make sure you dont have access to S3

````sh
aws s3 ls --profile sts
````

## Create a role 

```sh
aws iam put-user-policy \
    --user-name bijoy \
    --policy-name StsAssumePolicy \
    --policy-document file://policy.json

```
## Use new user credentials and assume role
```sh
aws iam put-user-policy \
--user-name sts-machine-user \
--policy-name StsAssumePolicy \
--policy-document file://policy.json

```sh
aws sts assume-role \
    --role-arn arn:aws:iam::905315126713:role/sts-fun-bs-StsRole-BcEudQKE8dkL \
    --role-session-name s3-sts-fun \
    --profile sts
```


## Read buckets
``` s3
aws s3 ls --profile assumed 
```

## Cleanup
```sh 
aws iam delete-user-policy --user-name sts-machine-user --policy-name StsAssumePolicy 

aws iam delete-access-key --access-key-id AKIA5FSH4RW4SFR4GXLS --user-name sts-machine-user

aws iam delete-user --user-name sts-machine-user

aws 

```
