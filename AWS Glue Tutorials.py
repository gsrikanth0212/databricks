# Databricks notebook source
1. Spark Architecture
2. Glue Architecture
3. Glue Performance Optimization techniques
4. Pyspark Optimization techniques
5. SQL Optimization techniques
6. Python Optimization techniques

# COMMAND ----------

AWS Glue Project

1. Create VPC end points for S3 and Glue (make sure select appropriate VPC)
2. Create S3 bucket and objects and add some data to it
3. Go to AWS lakeformation cosole, add your user accounts as administrators
4. Create Data lake locations, register the location by choosing the S3 bucket path
5. Keep the default role, this role used by lake formation to access the data from S3
6. Create the database, choose the location to store all the data
7. Disable use only IAM access control
8. Create table under this database, this table is catalog for the data stored in S3 bucket
9. Provide the location where data is stored, go to the folder level
10. Provide data format
11. Upload json schema file or create schema
12. We can also create table by using crawler
13. Till now, we don't have access to this table but we can grant the access to table as you are local administrator
14. We can choose the table level permissions
15. We can use athena for querying the table
16. Go to athena console, Configure S3 location from Settings
17. Go to the editor and run SQL quries
18. Data Access Control: We can give create table, select snd other access to specific user to access the tables
	We can give access at column level and row level for the users
19. Data Filters can be used to give access at row level and column level
20. Go to the Data Filters in Lake Formation, Create Data filters, select the database and table
	select the columns and specify the condition to give access at row level
21. To use these filters, Go to data lake permissions, grant access, select the users, select the database, tables and data filters
22. Create Work groups for Athena
23. Go to work groups in athena console, create work group
24. Choose the location for athena from S3 bucket
25. The user need to register the location for athena in their account
26. Classifiers are used by crawler to read the data in datastore, recognize the format of the data in datastore and generate the schema
27. Crawler automatically user built-in classifier. We can also use custom classifier
28. Using Glue crawler with JDBC Connection
29. We can run crawler On demand, Schedule and pipline and workflow
30. Create role for Glue, Select AWSGlueServiceRole
31. Grant Permissions for this role for the database, table and apply data access control from Lake Formation
32. Go AWS Glue Console, Create database connection to connect the JDBC datastore
33. Go to crawlers, add crawler and select the datastore as JDBC
34. Select the role and select the target datastore
35. Select the crawler and run the crawler, the table will be created
36. Table schema version on updates and comparision
37. Crawler can automatically partition the data
38. Do some changes to schema in data store and run the crawler again
39. We will see new version of table in data catalog, We can compare the Schema versions
40. The glue crawler to access the S3, the IAM role need to be given access to S3 bucket that you are trying to access
	go to the plicies and check for the resource and give s3 bucket ARN
41. We can add more table properties for a table
42. Create Glue job
43. Create Glue workflow by using sequence of glue jobs
 
https://www.linkedin.com/pulse/how-setup-aws-gluepyspark-job-development-environment-akhilesh-singh

AWS Glue job Optimization Part-1
	1. Memory Optimization (Run time optimization)
	2. Capacity Optimization 
Relies intensively on cluster memory

Technique Push Down Predicates
	Effectively leverages data partitions in Glue job
	data partition is must in order to leverage this technique
	
	Ex:
	Customer table
	id, gender, married?, age, graduate, profession, workexperience, spending, familysize
	First level of partition is on spending
	Second level of partition is on profession
	
	
	# Reading data in dyncamic frame
	df = glueContext.create_dynamic_frame.form_catalog(database = "", table_name = "")	
	df = Filter.apply(df, f=lambda x: x["spending"] == "High")

	# Above two lines process all the records in each line
	# We can solve this by using pushdown predicate

	df = glueContext.create_dynamic_frame.from_catalog(database="", table_name="", push_down_predicate = "(spending = 'High')")
	# In a single line, it will process only filtered data

	df = glueContext.create_dynamic_frame.from_catalog(database="", table_name="", push_down_predicate = "(spending = 'High') and profession = 'Engineer'")

	Go to AWS Glue Console:
	*We have partitioned data in S3 bucket 
 	*We have database created in catalog
	*We have table created in catalog
	*Launch developer end points to use sagemaker notebook to do line by line execution
	*Under developer end point there is sagemaker notebook

	import sys
	from awsglue.transforms import *
	from awsglue.utils import getResolvedOptions
	from pyspark.context import SparkContext
	from awsglue.context import GlueContext

	glueContext = GlueContext(SparkContext.getOrCreate())
	
	customer_df = glueContext.create_dynamic_frame.from_catalog(database="", table_name="")
	customer_df.count()
	customer_df = Filter.apply(customer_df, f= lambda x: x["spending"] == "High")
	customer_df.count()
	
	customer_df = glueContext.create_dynamic_frame.from_catalog(database = "", table_name="", push_down_predicate = "(spending == 'High')")
	customer_df.count()

	customer_df = glueContext.create_dynamic_frame.from_catalog(database = "", table_name = "", push_down_predicate = "(spending == 'High' and profession = 'Engineer')")	
	customer_df.count()


AWS Glue job Optimization part 2
	Parallel Reads and writes with JDBC data sources
	Help improves the performance
	
	table_name = fooddemand
	Columns = [Trxid, week, Centerid, mealid, checkoutprice, baseprice]

	# Single query read
	food_df = glueContext.create_dynamic_frame.form_catalog(database = "mydb", table_name = "fooddemand")
	
	# Potential for parallel reads
	food_df = glueContext.create_dynamic_frame.from_catalog(database = "", table_name = "fooddemand",
						additional_options = {'hashfield' : 'week', 'hashpartitions : 5'})

	Quicktips:
	*We can also use hashexpressions (SQL Expression) inplace of hashfield
	*Use hashexpression/Hashfield which does even distribution of values to spread the data between partitions
	*Can also use create_dynamic_frame.from_options 
		
	#single query write
	glueContext.write_dynamic_frame.from_jdbc_conf(df, catalog_connection = "glue_connection",
							connection_options = {"dbtable": "tbl", "databse": "fooddemand"}, 
							redshif_tmp_dir = "S3_uri")


	glueContext.write_dynamic_frame.from_options(frame = df, connection_type = "redshift/postgresql/mysql",
							connection_options = {"user": uname,
							"password": pwd, "url": "jdbc_url", "dbtable": "fooddemand",
							"redshiftTmpDir": "s3_uri"})

	
	#Parallel inserts (Only .from_options)
	glueContext.write_dynamic_frame.from_options(frame = df, connection_type = "redshift/postgresql/mysql",
							connection_options = {"user": uname,
							"password": pwd, "url": "jdbc_url", "dbtable": "fooddemand",
							"redshiftTmpDir": "s3_uri",
							"bulkSize" : "<number>"})
	

	Amazon RDS -----> SageMaker Notebook (Developer End Point) -----> Amazon Redshift
	
	import sys
	import awsglue.transforms import *
	import awsglue.utils import getResolvedOptions
	import pyspark.context import SparkContext
	import awsglue.context import GlueContext
	import awsglue.job import Job
	import time
	
	glueContext = GlueContext(SparkContext.getOrCreate())
	
	food_df = glueContext.create_dynamic_frame.from_catalog(database = "", table_name = "fooddemand")
	food_df1 = glueContext.create_dynamic_frame.from_catalog(database = "", table_name = "fooddemand",
				additional_options = {'hashfield' : 'week', 'hashpartitions' : '5'})

	food_df.count()
	food_df1.count()

	import boto3
	import json
	
	secret_name = "secret_manager_arn"
	region_name = "eu_west-1"
	session = boto3.session.Session()
	client = session.client(service_name = "secretmanager", region_name = region_name)
	
	response = client.get.secret_value(SecretId = secret_name)
	secrets = json.loads(response["SecretString"])
	
	uname = secrets["username"]
	pwd = secrets["password"]
	host = secrets["host"]

	print(host)
	
	
	glueContext.write_dynamic_frame.from_options(frame = fooddf, connection_type = "redshift",
							connection_options = {"user": uname,
							"password": pwd, 
							"url": "jdbc:redshift://" + host + ":5439/dev", 
							"dbtable": "public.fooddemand",
							"redshiftTmpDir": "s3_uri",
							"bulkSize" : "2"})

	


configure aws cli with IAM role and access aws resources
configure aws cli with config file

Role to be created or already created for glue to access the s3 bucket
Check the policies with in this role

check the limitations of interactive sessions

create connections for input datasource and target datasource by providing the credentials from secret manager
create database or
create/update table by adding/running a crawler
create glue jobs and do tranformations
wrtite to Reshift tables


AWS Glue Optimization Technique:
	*Exclusions for s3 path
	
	df = glueContext.create_dynamic_frame.from_options('s3',
						{
    							"paths": ['s3://shop_branch_bucket/state_branches_table/'],
    							"exclusions":  "[\"s3://shop_branch_bucket/state_branches_table/Karnataka/**\"]"
						},
						format="json",transformation_ctx = "AWSGlueDataCatalog")


	*Exclusions for S3 storage class

	df = glueContext.create_dynamic_frame.from_catalog(database = "branches_database",
    								tableName = "state_branches_table",
    								redshift_tmp_dir = "",
    								transformation_ctx = "AWSGlueDataCatalog",
    						additional_options = {
        								"excludeStorageClasses": ["GLACIER", "DEEP_ARCHIVE"]
    								})



AWS Glue Optimization Technique:
	Optimize Parallel processing
	Glue job capacity configuration
	Number of workers and worker type
	G.1X

AWS Glue Optimization Technique: Batch processing using workload partitioning
Helps in scalable processing of historical data
2 use cases
	1. trying to ingest first time large scale data
	2. Scheduled large scale data processing

Challenges with large scale data processing
	Processing all data in one go, one job
	
	Problems: Resource crunch such as out of memory
		  Not able to progress incremental
       		  Long time to take for processing: if failed at the last moment: start again for long time
	
	Solution: workload partitioning or batch data processing
		this works on only s3
		1. Batch dby file count or data size
			glueContext.create_dynamic_frame.from_catalog(
					database = "database",
					tableName = "table_name",
					additional_options = {"boundedFiles": "500"})


		OR
			glueContext.create_dynamic_frame.from_catalog(
					database = "database",
					tableName = "table_name",
					additional_options = {"boundedSize": 1000000"})

		2. Enable Job book mark
		3. Run Job Multiple Times (Can be used Step functions)

		Catalog parameters:
			Set boundedSize = xyz bytes
			Set boundedFiles = xyz

AWS Glue Optimization Technique:
	Flexible Execution class for Glue job
	
	Ex of non-time critical ETL jobs
	Test job runs in pre production
	One-time bulk data load jobs
	Job with longer time-frame to run such as nighty jobs week-end jobs etc
	Any other job where time is not a consideration
	
	Two ways to configure the job
	1. Standard job $0.44 per DPU-Hour 
		Immediate Fulfillment
	2. Job with Flexible execution $0.29 per DPU-Hour
		AWS Glue version 3.0 or later
		G.1X or G.2X worker types
		
		Fulfillment based on spare capacity
	How to:	
		1. Flex execution check box
		2. aws glue start-job-run
			--job-name jaob_name
			--execution-class FLEX
			--timeout 120
	


Tips for Glue jobs
	1. use of development end points
	2. Enable continuous logging and monitoring
	3. Understanding glue dynamic frame abstraction
	4. AWS Crawlers can be used but not only a way
	5. no need to think of having many layers of partition
	6. Using glue workflows
	7. using python shell jobs
	8. make use of bookmarks 

Job parameters
--additional-python-modules
--auto-scale-within-microbatch
--class
--continuous-log-conversionPattern
--continuous-log-logGroup
--continuous-log-logStreamPrefix
--datalake-formats
--disable-proxy-v2
--enable-auto-scaling
--enable-continuous-cloudwatch-log
--enable-continuous-log-filter
--enable-glue-datacatalog
--enable-job-insights
--enable-metrics
--enable-rename-algorithm-v2
--enable-s3-parquet-optimized-committer
--enable-spark-ui
--extra-files
--extra-jars
--extra-py-files
--job-bookmark-option

Job status
FAIL
TIMEOT
ERROR
WAITING


Job Properties
Name
IAM Role
Type of job
Glue Version
Temporary directory
Advanced properties
	job bookmark
Monitoring options
	Job Metrics
	Continous Logging
	Spark UI
Tags
Security Configurations 
Python library path, Referenced files path
Worker Type
Number of Workers
Execution class (pre-prod jobs)
Max Concurrency
job timeout
Delay notification threshold
Number of retries
Non overridable job parameters
Catalog options
Data source -- choose data catalog table
Transformations
Target


aws ecr get-login-password \
    --region us-east-1 | docker login \
    --username AWS \
    --password-stdin 709825985650.dkr.ecr.us-east-1.amazonaws.com
    
CONTAINER_IMAGES="709825985650.dkr.ecr.us-east-1.amazonaws.com/amazon-web-services/glue/sftpstorage:1.0.0-glue3.0"    

for i in $(echo $CONTAINER_IMAGES | sed "s/,/ /g"); do docker pull $i; done



Create a new secret for SFTP Storage in AWS Secrets Manager

host

On the Secrets Manager console, choose Store a new secret.
For Secret type, select Other type of secret.
Enter key as host for SFTP storage host.
Enter keys as username and password(Optional) for SFTP credential.
Enter key as keyS3Uri for SFTP secret key file. Value is s3 full path where key file uploaded, like s3://myBucket/myKeyFile.
Leave the rest of the options at their default.
Choose Next.
Give a name to the secret sftp_credentials.


Create a job of data source or target from this connector, select custom connection. Then input options and values.
File format connection options, we support 5 different formats, csv/parquet/json/orc/text.
The basic options are path, the SFTP storage cloud storage URI, e.g. /input/covid-csv-data/. fileFormat, input or output file format, e.g. csv/parquet/json/orc/text
For each format, there are different connection options supported.
CSV: Option name, header, delimiter, compression, Option Value corresponding,true/false, any delimiter char, none/uncompressed/snappy/gzip/lzo/lz4/brotli/zstd, default value is false, , none.
PARQUET, ORC, TEXT and JSON: Option name, compression, Option Value, none/uncompressed/snappy/gzip/lzo/lz4/brotli/zstd, default value is none.
Remember to set the Glue version to be Glue 3.0 on job detail tab.


import boto3
import paramiko

s3 = boto3.resource("s3")
bucket = s3.Bucket(name="destination-bucket")
bucket.load()
 
ssh = paramiko.SSHClient()
# In prod, add explicitly the rsa key of the host instead of using the AutoAddPolicy:
# ssh.get_host_keys().add('example.com', 'ssh-rsa', paramiko.RSAKey(data=decodebytes(b"""AAAAB3NzaC1yc2EAAAABIwAAAQEA0hV...""")))
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
ssh.connect(
    hostname="sftp.example.com",
    username="thisdataguy",
    password="very secret",
)
 
sftp = ssh.open_sftp()
 
for filename in sftp.listdir():
    print(f"Downloading {filename} from sftp...")
    # mode: ssh treats all files as binary anyway, to 'b' is ignored.
    with sftp.file(filename, mode="r") as file_obj:
        print(f"uploading  {filename} to s3...")
        bucket.put_object(Body=file_obj, Key=f"destdir/{filename}")
        print(f"All done for {filename}")



# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "sftpcreds"
    region_name = "ap-south-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    # Your code goes here.





