import boto3  #AWS

import secrets #Random numbers
import uuid

bucket_name = input("Enter bucket name: ")

s3 = boto3.client('s3')

request = s3.create_bucket(Bucket = bucket_name)

print(request)

numOfFiles = 1 + secrets.randbelow(6)

print("Number of files: " + str(numOfFiles))

for i in range(numOfFiles):
    print(f"i: {i}")
    filename = f"file_{i}.txt"  # Generating a filename for each file
    output_path = f"/tmp/{filename}"  # Specifying the output path for the file

    # Writing a unique UUID to each file
    with open(output_path, "w") as f:
        f.write(str(uuid.uuid4()))  # Write a random UUID to the file

    # Open and read the file in binary mode, then upload it to S3
    with open(output_path, 'rb') as f:  # 'rb' mode for reading binary data
        s3.put_object(                # Uploading the file to S3
            Bucket=bucket_name,           # Bucket to upload to
            Key=filename,                 # Key (filename) for the object in the bucket
            Body=f                        # File content
        )