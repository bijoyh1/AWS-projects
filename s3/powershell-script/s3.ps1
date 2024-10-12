Import-Module AWS.Tools.S3

$region = "us-east-1"

$bucketName = Read-Host -Prompt "Enter the S3 bucket name"

Write-Host "AWS Region: $region"
Write-Host "S3 Bucket: $bucketName"

function bucketExists 
{
    $exists = Get-S3Bucket -BucketName $bucketName -ErrorAction SilentlyContinue
    return $null -ne $exists
}

if (-not (bucketExists))
{
    New-S3Bucket -BucketName $bucketName -Region $region
}
else
{
    Write-Host "Bucket already exists..."
}

#Create new fil

$fileName = 'myfile.txt'
$fileContent = 'Hello World!'
Set-Content -Path $fileName -Value $fileContent

Write-S3Object -BucketName $bucketName -File $fileName