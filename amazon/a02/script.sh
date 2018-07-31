#!/bin/bash
### Creating buckets to simulate lots of stuff
aws s3 mb s3://correctora02bucketfoo; aws s3 mb s3://correctora02bucketbar; aws s3 mb s3://correctora02bucketbuz 
# 1
aws s3 mb s3://correctora02bucketreal
aws s3 ls | grep correctora02bucketreal

# 1 s3api
aws s3api create-bucket --bucket correctora02buckets3apireal --region us-west-1 --create-bucket-configuration LocationConstraint=us-west-1
aws s3api list-buckets --region us-west-1 | grep correctora02buckets3apireal | awk {' print $2 " " $4'}

# 2
echo "Test data" > TestData.txt
aws s3 cp ./TestData.txt s3://correctora02bucketreal/

# 2 s3api
aws s3api put-object --bucket correctora02buckets3apireal --body TestData.txt --key TestData.txt

# 3
aws s3 ls s3://correctora02bucketreal

# 3 s3api 
aws s3api list-objects --bucket correctora02buckets3apireal

# 4
rm -f ./TestData.txt
aws s3 sync s3://correctora02bucketreal .

# 4 s3api
rm -f ./TestData.txt
aws s3api list-objects --bucket correctora02buckets3apireal --output text | grep CONTENTS | awk {'print $3'} | xargs -L1 -I {} aws s3api get-object --bucket correctora02buckets3apireal --key {} {}

# 5
aws s3 rm s3://correctora02bucketreal/TestData.txt
aws s3 rb s3://correctora02bucketreal

# 5 s3api
aws s3api delete-object --bucket correctora02buckets3apireal --key TestData.txt
aws s3api delete-bucket --bucket correctora02buckets3apireal --region us-west-1

### clear simulation buckets after running the script
aws s3api delete-bucket --bucket correctora02bucketfoo --region us-west-1; aws s3api delete-bucket --bucket correctora02bucketbar --region us-west-1; aws s3api delete-bucket --bucket correctora02bucketbuz --region us-west-1;
