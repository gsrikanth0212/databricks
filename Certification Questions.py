# Databricks notebook source
# MAGIC %md
# MAGIC **1. A data engineer is configuring an AWS Glue job to read data from an Amazon S3 bucket. The data engineer has set up the necessary AWS Glue connection details and an associated IAM role. However, when the data engineer attempts to run the AWS Glue job, the data engineer receives an error message that indicates that there are problems with the Amazon S3 VPC gateway endpoint.
# MAGIC The data engineer must resolve the error and connect the AWS Glue job to the S3 bucket.
# MAGIC Which solution will meet this requirement?**
# MAGIC
# MAGIC - A. Update the AWS Glue security group to allow inbound traffic from the Amazon S3 VPC gateway endpoint.
# MAGIC - B. Configure an S3 bucket policy to explicitly grant the AWS Glue job permissions to access the S3 bucket.
# MAGIC - C. Review the AWS Glue job code to ensure that the AWS Glue connection details include a fully qualified domain name.
# MAGIC - D. Verify that the VPC's route table includes inbound and outbound routes for the Amazon S3 VPC gateway endpoint.
# MAGIC
# MAGIC D

# COMMAND ----------

# MAGIC %md
# MAGIC **2. A retail company has a customer data hub in an Amazon S3 bucket. Employees from many countries use the data hub to support company-wide analytics. A governance team must ensure that the company's data analysts can access data only for customers who are within the same country as the analysts.
# MAGIC Which solution will meet these requirements with the LEAST operational effort?**
# MAGIC
# MAGIC - A. Create a separate table for each country's customer data. Provide access to each analyst based on the country that the analyst serves.
# MAGIC - B. Register the S3 bucket as a data lake location in AWS Lake Formation. Use the Lake Formation row-level security features to enforce the company's access policies.
# MAGIC - C. Move the data to AWS Regions that are close to the countries where the customers are. Provide access to each analyst based on the country that the analyst serves.
# MAGIC - D. Load the data into Amazon Redshift. Create a view for each country. Create separate IAM roles for each country to provide access to data from each country. Assign the appropriate roles to the analysts.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **3. A media company wants to improve a system that recommends media content to customer based on user behavior and preferences. To improve the recommendation system, the company needs to incorporate insights from third-party datasets into the company's existing analytics platform.
# MAGIC The company wants to minimize the effort and time required to incorporate third-party datasets.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Use API calls to access and integrate third-party datasets from AWS Data Exchange.
# MAGIC - B. Use API calls to access and integrate third-party datasets from AWS DataSync.
# MAGIC - C. Use Amazon Kinesis Data Streams to access and integrate third-party datasets from AWS CodeCommit repositories.
# MAGIC - D. Use Amazon Kinesis Data Streams to access and integrate third-party datasets from Amazon Elastic Container Registry (Amazon ECR).
# MAGIC
# MAGIC A

# COMMAND ----------

# MAGIC %md
# MAGIC **4. A financial company wants to implement a data mesh. The data mesh must support centralized data governance, data analysis, and data access control. The company has decided to use AWS Glue for data catalogs and extract, transform, and load (ETL) operations.
# MAGIC Which combination of AWS services will implement a data mesh? (Choose two.)**
# MAGIC
# MAGIC - A. Use Amazon Aurora for data storage. Use an Amazon Redshift provisioned cluster for data analysis.
# MAGIC - B. Use Amazon S3 for data storage. Use Amazon Athena for data analysis.
# MAGIC - C. Use AWS Glue DataBrew for centralized data governance and access control.
# MAGIC - D. Use Amazon RDS for data storage. Use Amazon EMR for data analysis.
# MAGIC - E. Use AWS Lake Formation for centralized data governance and access control.
# MAGIC
# MAGIC
# MAGIC B&E

# COMMAND ----------

# MAGIC %md
# MAGIC **5. A data engineer maintains custom Python scripts that perform a data formatting process that many AWS Lambda functions use. When the data engineer needs to modify the Python scripts, the data engineer must manually update all the Lambda functions.
# MAGIC The data engineer requires a less manual way to update the Lambda functions.
# MAGIC Which solution will meet this requirement?**
# MAGIC
# MAGIC - A. Store a pointer to the custom Python scripts in the execution context object in a shared Amazon S3 bucket.
# MAGIC - B. Package the custom Python scripts into Lambda layers. Apply the Lambda layers to the Lambda functions.
# MAGIC - C. Store a pointer to the custom Python scripts in environment variables in a shared Amazon S3 bucket.
# MAGIC - D. Assign the same alias to each Lambda function. Call reach Lambda function by specifying the function's alias
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **6. A company created an extract, transform, and load (ETL) data pipeline in AWS Glue. A data engineer must crawl a table that is in Microsoft SQL Server. The data engineer needs to extract, transform, and load the output of the crawl to an Amazon S3 bucket. The data engineer also must orchestrate the data pipeline.
# MAGIC Which AWS service or feature will meet these requirements MOST cost-effectively?**
# MAGIC
# MAGIC - A. AWS Step Functions
# MAGIC - B. AWS Glue workflows
# MAGIC - C. AWS Glue Studio
# MAGIC - D. Amazon Managed Workflows for Apache Airflow (Amazon MWAA)
# MAGIC
# MAGIC D

# COMMAND ----------

# MAGIC %md
# MAGIC **7. A financial services company stores financial data in Amazon Redshift. A data engineer wants to run real-time queries on the financial data to support a web-based trading application. The data engineer wants to run the queries from within the trading application.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Establish WebSocket connections to Amazon Redshift.
# MAGIC - B. Use the Amazon Redshift Data API.
# MAGIC - C. Set up Java Database Connectivity (JDBC) connections to Amazon Redshift.
# MAGIC - D. Store frequently accessed data in Amazon S3. Use Amazon S3 Select to run the queries.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **8. A company uses Amazon Athena for one-time queries against data that is in Amazon S3. The company has several use cases. The company must implement permission controls to separate query processes and access to query history among users, teams, and applications that are in the same AWS account.
# MAGIC Which solution will meet these requirements?**
# MAGIC
# MAGIC - A. Create an S3 bucket for each use case. Create an S3 bucket policy that grants permissions to appropriate individual IAM users. Apply the S3 bucket policy to the S3 bucket.
# MAGIC - B. Create an Athena workgroup for each use case. Apply tags to the workgroup. Create an IAM policy that uses the tags to apply appropriate permissions to the workgroup.
# MAGIC - C. Create an IAM role for each use case. Assign appropriate permissions to the role for each use case. Associate the role with Athena.
# MAGIC - D. Create an AWS Glue Data Catalog resource policy that grants permissions to appropriate individual IAM users for each use case. Apply the resource policy to the specific tables that Athena uses.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **9. A data engineer needs to schedule a workflow that runs a set of AWS Glue jobs every day. The data engineer does not require the Glue jobs to run or finish at a specific time.
# MAGIC Which solution will run the Glue jobs in the MOST cost-effective way?**
# MAGIC
# MAGIC - A. Choose the FLEX execution class in the Glue job properties.
# MAGIC - B. Use the Spot Instance type in Glue job properties.
# MAGIC - C. Choose the STANDARD execution class in the Glue job properties.
# MAGIC - D. Choose the latest version in the GlueVersion field in the Glue job properties.
# MAGIC
# MAGIC A
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **10. A data engineer needs to create an AWS Lambda function that converts the format of data from .csv to Apache Parquet. The Lambda function must run only if a user uploads a .csv file to an Amazon S3 bucket.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Create an S3 event notification that has an event type of s3:ObjectCreated:*. Use a filter rule to generate notifications only when the suffix includes .csv. Set the Amazon Resource Name (ARN) of the Lambda function as the destination for the event notification.
# MAGIC - B. Create an S3 event notification that has an event type of s3:ObjectTagging:* for objects that have a tag set to .csv. Set the Amazon Resource Name (ARN) of the Lambda function as the destination for the event notification.
# MAGIC - C. Create an S3 event notification that has an event type of s3:*. Use a filter rule to generate notifications only when the suffix includes .csv. Set the Amazon Resource Name (ARN) of the Lambda function as the destination for the event notification.
# MAGIC - D. Create an S3 event notification that has an event type of s3:ObjectCreated:*. Use a filter rule to generate notifications only when the suffix includes .csv. Set an Amazon Simple Notification Service (Amazon SNS) topic as the destination for the event notification. Subscribe the Lambda function to the SNS topic.
# MAGIC
# MAGIC A
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **11. A data engineer needs Amazon Athena queries to finish faster. The data engineer notices that all
# MAGIC the files the Athena queries use are currently stored in uncompressed .csv format. The data engineer
# MAGIC also notices that users perform most queries by selecting a specific column. Which solution will
# MAGIC MOST speed up the Athena query performance?**
# MAGIC
# MAGIC - A. Change the data format from .csv to JSON format. Apply Snappy compression.
# MAGIC - B. Compress the .csv files by using Snappy compression.
# MAGIC - C. Change the data format from .csv to Apache Parquet. Apply Snappy compression.
# MAGIC - D. Compress the .csv files by using gzip compression
# MAGIC
# MAGIC D

# COMMAND ----------

# MAGIC %md
# MAGIC **12. A manufacturing company collects sensor data from its factory floor to monitor and enhance
# MAGIC operational efficiency. The company uses Amazon Kinesis Data Streams to publish the data that the
# MAGIC sensors collect to a data stream. Then Amazon Kinesis Data Firehose writes the data to an Amazon
# MAGIC S3 bucket. The company needs to display a real-time view of operational efficiency on a large
# MAGIC screen in the manufacturing facility. Which solution will meet these requirements with the
# MAGIC LOWEST latency?**
# MAGIC
# MAGIC - A. Use Amazon Managed Service for Apache Flink (previously known as Amazon Kinesis Data Analytics) to process the sensor data. Use a connector for Apache Flink to write data to an Amazon Timestream database. Use the Timestream database as a source to create a Grafana dashboard.
# MAGIC - B. Configure the S3 bucket to send a notification to an AWS Lambda function when any new object is created. Use the Lambda function to publish the data to Amazon Aurora. Use Aurora as a source to create an Amazon QuickSight dashboard.
# MAGIC - C. Use Amazon Managed Service for Apache Flink (previously known as Amazon Kinesis Data Analytics) to process the sensor data. Create a new Data Firehose delivery stream to publish data directly to an Amazon Timestream database. Use the Timestream database as a source to create an Amazon QuickSight dashboard.
# MAGIC - D. Use AWS Glue bookmarks to read sensor data from the S3 bucket in real time. Publish the data to an Amazon Timestream database. Use the Timestream database as a source to create a Grafana dashboard.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **13. A company stores daily records of the financial performance of investment portfolios in .csv
# MAGIC format in an Amazon S3 bucket. A data engineer uses AWS Glue crawlers to crawl the S3 data. The
# MAGIC data engineer must make the S3 data accessible daily in the AWS Glue Data Catalog. Which
# MAGIC solution will meet these requirements?**
# MAGIC
# MAGIC - A. Create an IAM role that includes the AmazonS3FullAccess policy. Associate the role with the
# MAGIC    crawler. Specify the S3 bucket path of the source data as the crawler's data store. Create a daily
# MAGIC    schedule to run the crawler. Configure the output destination to a new path in the existing S3
# MAGIC    bucket.
# MAGIC - B. Create an IAM role that includes the AWSGlueServiceRole policy. Associate the role with the
# MAGIC    crawler. Specify the S3 bucket path of the source data as the crawler's data store. Create a daily
# MAGIC    schedule to run the crawler. Specify a database name for the output.
# MAGIC - C. Create an IAM role that includes the AmazonS3FullAccess policy. Associate the role with the
# MAGIC    crawler. Specify the S3 bucket path of the source data as the crawler's data store. Allocate data
# MAGIC    processing units (DPUs) to run the crawler every day. Specify a database name for the output.
# MAGIC - D. Create an IAM role that includes the AWSGlueServiceRole policy. Associate the role with the
# MAGIC    crawler. Specify the S3 bucket path of the source data as the crawler's data store. Allocate data
# MAGIC    processing units (DPUs) to run the crawler every day. Configure the output destination to a new
# MAGIC    path in the existing S3 bucket.
# MAGIC
# MAGIC    D

# COMMAND ----------

# MAGIC %md
# MAGIC **14. A company loads transaction data for each day into Amazon Redshift tables at the end of each
# MAGIC day. The company wants to have the ability to track which tables have been loaded and which tables
# MAGIC still need to be loaded. A data engineer wants to store the load statuses of Redshift tables in an
# MAGIC Amazon DynamoDB table. The data engineer creates an AWS Lambda function to publish the
# MAGIC details of the load statuses to DynamoDB. How should the data engineer invoke the Lambda
# MAGIC function to write load statuses to the DynamoDB table?**
# MAGIC
# MAGIC - A. Use a second Lambda function to invoke the first Lambda function based on Amazon CloudWatch events.
# MAGIC - B. Use the Amazon Redshift Data API to publish an event to Amazon EventBridge. Configure an EventBridge rule to invoke the Lambda function.
# MAGIC - C. Use the Amazon Redshift Data API to publish a message to an Amazon Simple Queue Service (Amazon SQS) queue. Configure the SQS queue to invoke the Lambda function.
# MAGIC - D. Use a second Lambda function to invoke the first Lambda function based on AWS CloudTrail events.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **15. A data engineer needs to securely transfer 5 TB of data from an on-premises data center to an
# MAGIC Amazon S3 bucket. Approximately 5% of the data changes every day. Updates to the data need to
# MAGIC be regularly proliferated to the S3 bucket. The data includes files that are in multiple formats. The
# MAGIC data engineer needs to automate the transfer process and must schedule the process to run
# MAGIC periodically. Which AWS service should the data engineer use to transfer the data in the MOST
# MAGIC operationally efficient way?**
# MAGIC
# MAGIC - A. AWS DataSync
# MAGIC - B. AWS Glue
# MAGIC - C. AWS Direct Connect
# MAGIC - D. Amazon S3 Transfer Acceleration
# MAGIC
# MAGIC A

# COMMAND ----------

# MAGIC %md
# MAGIC **16. A company uses an on-premises Microsoft SQL Server database to store financial transaction
# MAGIC data. The company migrates the transaction data from the on-premises database to AWS at the end
# MAGIC of each month. The company has noticed that the cost to migrate data from the on-premises
# MAGIC database to an Amazon RDS for SQL Server database has increased recently. The company requires
# MAGIC a cost-effective solution to migrate the data to AWS. The solution must cause minimal downtime for
# MAGIC the applications that access the database. Which AWS service should the company use to meet these
# MAGIC requirements?**
# MAGIC
# MAGIC - A. AWS Lambda
# MAGIC - B. AWS Database Migration Service (AWS DMS)
# MAGIC - C. AWS Direct Connect
# MAGIC - D. AWS DataSync
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **17. A data engineer is building a data pipeline on AWS by using AWS Glue extract, transform, and
# MAGIC load (ETL) jobs. The data engineer needs to process data from Amazon RDS and MongoDB,
# MAGIC perform transformations, and load the transformed data into Amazon Redshift for analytics. The
# MAGIC data updates must occur every hour. Which combination of tasks will meet these requirements with
# MAGIC the LEAST operational overhead? (Choose two.)**
# MAGIC
# MAGIC - A. Configure AWS Glue triggers to run the ETL jobs every hour.
# MAGIC - B. Use AWS Glue DataBrew to clean and prepare the data for analytics.
# MAGIC - C. Use AWS Lambda functions to schedule and run the ETL jobs every hour.
# MAGIC - D. Use AWS Glue connections to establish connectivity between the data sources and Amazon Redshift.
# MAGIC - E. Use the Redshift Data API to load transformed data into Amazon Redshift.
# MAGIC
# MAGIC A and D

# COMMAND ----------

# MAGIC %md
# MAGIC **18. A company uses an Amazon Redshift cluster that runs on RA3 nodes. The company wants to
# MAGIC scale read and write capacity to meet demand. A data engineer needs to identify a solution that will
# MAGIC turn on concurrency scaling. Which solution will meet this requirement?**
# MAGIC
# MAGIC - A. Turn on concurrency scaling in workload management (WLM) for Redshift Serverless workgroups.
# MAGIC - B. Turn on concurrency scaling at the workload management (WLM) queue level in the Redshift cluster.
# MAGIC - C. Turn on concurrency scaling in the settings during the creation of any new Redshift cluster.
# MAGIC - D. Turn on concurrency scaling for the daily usage quota for the Redshift cluster
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **19. A data engineer must orchestrate a series of Amazon Athena queries that will run every day.
# MAGIC Each query can run for more than 15 minutes. Which combination of steps will meet these
# MAGIC requirements MOST cost-effectively? (Choose two.)**
# MAGIC
# MAGIC - A. Use an AWS Lambda function and the Athena Boto3 client start_query_execution API call to invoke the Athena queries programmatically.
# MAGIC - B. Create an AWS Step Functions workflow and add two states. Add the first state before the Lambda function. Configure the second state as a Wait state to periodically check whether the Athena query has finished using the Athena Boto3 get_query_execution API call. Configure the workflow to invoke the next query when the current query has finished running.
# MAGIC - C. Use an AWS Glue Python shell job and the Athena Boto3 client start_query_execution API call to invoke the Athena queries programmatically.
# MAGIC - D. Use an AWS Glue Python shell script to run a sleep timer that checks every 5 minutes to determine whether the current Athena query has finished running successfully. Configure the Python shell script to invoke the next query when the current query has finished running.
# MAGIC - E. Use Amazon Managed Workflows for Apache Airflow (Amazon MWAA) to orchestrate the Athena queries in AWS Batch.
# MAGIC
# MAGIC A and B

# COMMAND ----------

# MAGIC %md
# MAGIC **20. A company is migrating on-premises workloads to AWS. The company wants to reduce overall
# MAGIC operational overhead. The company also wants to explore serverless options. The company's current
# MAGIC workloads use Apache Pig, Apache Oozie, Apache Spark, Apache Hbase, and Apache Flink. The
# MAGIC on-premises workloads process petabytes of data in seconds. The company must maintain similar or
# MAGIC better performance after the migration to AWS. Which extract, transform, and load (ETL) service
# MAGIC will meet these requirements?**
# MAGIC
# MAGIC - A. AWS Glue
# MAGIC - B. Amazon EMR
# MAGIC - C. AWS Lambda
# MAGIC - D. Amazon Redshift
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **21. A data engineer must use AWS services to ingest a dataset into an Amazon S3 data lake. The
# MAGIC data engineer profiles the dataset and discovers that the dataset contains personally identifiable
# MAGIC information (PII). The data engineer must implement a solution to profile the dataset and obfuscate
# MAGIC the PII. Which solution will meet this requirement with the LEAST operational effort?**
# MAGIC
# MAGIC - A. Use an Amazon Kinesis Data Firehose delivery stream to process the dataset. Create an AWS Lambda transform function to identify the PII. Use an AWS SDK to obfuscate the PII. Set the S3 data lake as the target for the delivery stream.
# MAGIC - B. Use the Detect PII transform in AWS Glue Studio to identify the PII. Obfuscate the PII. Use an AWS Step Functions state machine to orchestrate a data pipeline to ingest the data into the S3 data lake.
# MAGIC - C. Use the Detect PII transform in AWS Glue Studio to identify the PII. Create a rule in AWS Glue Data Quality to obfuscate the PII. Use an AWS Step Functions state machine to orchestrate a data pipeline to ingest the data into the S3 data lake.
# MAGIC - D. Ingest the dataset into Amazon DynamoDB. Create an AWS Lambda function to identify and obfuscate the PII in the DynamoDB table and to transform the data. Use the same Lambda function to ingest the data into the S3 data lake.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **22. A company maintains multiple extract, transform, and load (ETL) workflows that ingest data
# MAGIC from the company's operational databases into an Amazon S3-based data lake. The ETL workflows
# MAGIC use AWS Glue and Amazon EMR to process data. The company wants to improve the existing
# MAGIC architecture to provide automated orchestration and to require minimal manual effort. Which
# MAGIC solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. AWS Glue workflows
# MAGIC - B. AWS Step Functions tasks
# MAGIC - C. AWS Lambda functions
# MAGIC - D. Amazon Managed Workflows for Apache Airflow (Amazon MWAA) workflows
# MAGIC
# MAGIC A

# COMMAND ----------

# MAGIC %md
# MAGIC **23. A company currently stores all of its data in Amazon S3 by using the S3 Standard storage class.
# MAGIC A data engineer examined data access patterns to identify trends. During the first 6 months, most
# MAGIC data files are accessed several times each day. Between 6 months and 2 years, most data files are
# MAGIC accessed once or twice each month. After 2 years, data files are accessed only once or twice each
# MAGIC year.
# MAGIC The data engineer needs to use an S3 Lifecycle policy to develop new data storage rules. The new
# MAGIC storage solution must continue to provide high availability. Which solution will meet these
# MAGIC requirements in the MOST cost-effective way?**
# MAGIC
# MAGIC - A. Transition objects to S3 One Zone-Infrequent Access (S3 One Zone-IA) after 6 months. Transfer objects to S3 Glacier Flexible Retrieval after 2 years.
# MAGIC - B. Transition objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 6 months. Transfer objects to S3 Glacier Flexible Retrieval after 2 years.
# MAGIC - C. Transition objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 6 months. Transfer objects to S3 Glacier Deep Archive after 2 years.
# MAGIC - D. Transition objects to S3 One Zone-Infrequent Access (S3 One Zone-IA) after 6 months. Transfer objects to S3 Glacier Deep Archive after 2 years.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **24. A company maintains an Amazon Redshift provisioned cluster that the company uses for
# MAGIC extract, transform, and load (ETL) operations to support critical analysis tasks. A sales team within
# MAGIC the company maintains a Redshift cluster that the sales team uses for business intelligence (BI)
# MAGIC tasks. The sales team recently requested access to the data that is in the ETL Redshift cluster so the
# MAGIC team can perform weekly summary analysis tasks. The sales team needs to join data from the ETL
# MAGIC cluster with data that is in the sales team's BI cluster.
# MAGIC The company needs a solution that will share the ETL cluster data with the sales team without
# MAGIC interrupting the critical analysis tasks. The solution must minimise usage of the computing
# MAGIC resources of the ETL cluster.
# MAGIC Which solution will meet these requirements?**
# MAGIC
# MAGIC
# MAGIC - A. Set up the sales team BI cluster as a consumer of the ETL cluster by using Redshift data sharing.
# MAGIC - B. Create materialised views based on the sales team's requirements. Grant the sales team direct access to the ETL cluster.
# MAGIC - C. Create database views based on the sales team's requirements. Grant the sales team direct access to the ETL cluster.
# MAGIC - D. Unload a copy of the data from the ETL cluster to an Amazon S3 bucket every week. Create an Amazon Redshift Spectrum table based on the content of the ETL cluster.
# MAGIC
# MAGIC A

# COMMAND ----------

# MAGIC %md
# MAGIC **25. A data engineer needs to join data from multiple sources to perform a one-time analysis job. The
# MAGIC data is stored in Amazon DynamoDB, Amazon RDS, Amazon Redshift, and Amazon S3. Which
# MAGIC solution will meet this requirement MOST cost-effectively?**
# MAGIC
# MAGIC - A. Use an Amazon EMR provisioned cluster to read from all sources. Use Apache Spark to join the data and perform the analysis.
# MAGIC - B. Copy the data from DynamoDB, Amazon RDS, and Amazon Redshift into Amazon S3. Run Amazon Athena queries directly on the S3 files.
# MAGIC - C. Use Amazon Athena Federated Query to join the data from all data sources.
# MAGIC - D. Use Redshift Spectrum to query data from DynamoDB, Amazon RDS, and Amazon S3 directly from Redshift.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **26. A company is planning to use a provisioned Amazon EMR cluster that runs Apache Spark jobs
# MAGIC to perform big data analysis. The company requires high reliability. A big data team must follow
# MAGIC best practices for running cost-optimised and long-running workloads on Amazon EMR. The team
# MAGIC must find a solution that will maintain the company's current level of performance. Which
# MAGIC combination of resources will meet these requirements MOST cost-effectively? (Choose two.)**
# MAGIC
# MAGIC - A. Use Hadoop Distributed File System (HDFS) as a persistent data store.
# MAGIC - B. Use Amazon S3 as a persistent data store.
# MAGIC - C. Use x86-based instances for core nodes and task nodes.
# MAGIC - D. Use Graviton instances for core nodes and task nodes.
# MAGIC - E. Use Spot Instances for all primary nodes.
# MAGIC
# MAGIC B and D

# COMMAND ----------

# MAGIC %md
# MAGIC **27. A company wants to implement real-time analytics capabilities. The company wants to use
# MAGIC Amazon Kinesis Data Streams and Amazon Redshift to ingest and process streaming data at the rate
# MAGIC of several gigabytes per second. The company wants to derive near real-time insights by using
# MAGIC existing business intelligence (BI) and analytics tools. Which solution will meet these requirements
# MAGIC with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Use Kinesis Data Streams to stage data in Amazon S3. Use the COPY command to load data from Amazon S3 directly into Amazon Redshift to make the data immediately available for realtime analysis.
# MAGIC - B. Access the data from Kinesis Data Streams by using SQL queries. Create materialised views directly on top of the stream. Refresh the materialised views regularly to query the most recent stream data.
# MAGIC - C. Create an external schema in Amazon Redshift to map the data from Kinesis Data Streams to an Amazon Redshift object. Create a materialised view to read data from the stream. Set the materialised view to auto refresh.
# MAGIC - D. Connect Kinesis Data Streams to Amazon Kinesis Data Firehose. Use Kinesis Data Firehose to stage the data in Amazon S3. Use the COPY command to load the data from Amazon S3 to a table in Amazon Redshift.
# MAGIC
# MAGIC D

# COMMAND ----------

# MAGIC %md
# MAGIC **28. A company uses an Amazon QuickSight dashboard to monitor usage of one of the company's
# MAGIC applications. The company uses AWS Glue jobs to process data for the dashboard. The company
# MAGIC stores the data in a single Amazon S3 bucket. The company adds new data every day. A data
# MAGIC engineer discovers that dashboard queries are becoming slower over time. The data engineer
# MAGIC determines that the root cause of the slowing queries is long-running AWS Glue jobs. Which actions
# MAGIC should the data engineer take to improve the performance of the AWS Glue jobs? (Choose two.)**
# MAGIC
# MAGIC - A. Partition the data that is in the S3 bucket. Organise the data by year, month, and day.
# MAGIC - B. Increase the AWS Glue instance size by scaling up the worker type.
# MAGIC - C. Convert the AWS Glue schema to the DynamicFrame schema class.
# MAGIC - D. Adjust AWS Glue job scheduling frequency so the jobs run half as many times each day.
# MAGIC - E. Modify the IAM role that grants access to AWS Glue to grant access to all S3 features.
# MAGIC
# MAGIC A and B

# COMMAND ----------

# MAGIC %md
# MAGIC **29. A data engineer needs to use AWS Step Functions to design an orchestration workflow. The
# MAGIC workflow must parallel process a large collection of data files and apply a specific transformation to
# MAGIC each file. Which Step Functions state should the data engineer use to meet these requirements?**
# MAGIC
# MAGIC - A. Parallel state
# MAGIC - B. Choice state
# MAGIC - C. Map state
# MAGIC - D. Wait state
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **30. A company is migrating a legacy application to an Amazon S3-based data lake. A data engineer
# MAGIC reviewed data that is associated with the legacy application. The data engineer found that the legacy
# MAGIC data contained some duplicate information.
# MAGIC The data engineer must identify and remove duplicate information from the legacy application data.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Write a custom extract, transform, and load (ETL) job in Python. Use the DataFrame.drop_duplicates() function by importing the Pandas library to perform data deduplication.
# MAGIC - B. Write an AWS Glue extract, transform, and load (ETL) job. Use the FindMatches machine learning (ML) transform to transform the data to perform data deduplication.
# MAGIC - C. Write a custom extract, transform, and load (ETL) job in Python. Import the Python dedupe library. Use the dedupe library to perform data deduplication.
# MAGIC - D. Write an AWS Glue extract, transform, and load (ETL) job. Import the Python dedupe library to perform data deduplication.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **31. A company is building an analytics solution. The solution uses Amazon S3 for data lake storage
# MAGIC and Amazon Redshift for a data warehouse. The company wants to use Amazon Redshift Spectrum
# MAGIC to query the data that is in Amazon S3. Which actions will provide the FASTEST queries? (Choose
# MAGIC two.)**
# MAGIC
# MAGIC - A. Use gzip compression to compress individual files to sizes that are between 1 GB and 5 GB.
# MAGIC - B. Use a columnar storage file format.
# MAGIC - C. Partition the data based on the most common query predicates.
# MAGIC - D. Split the data into files that are less than 10 KB.
# MAGIC - E. Use file formats that are not splittable.
# MAGIC
# MAGIC B and C

# COMMAND ----------

# MAGIC %md
# MAGIC **32. A company uses Amazon RDS to store transactional data. The company runs an RDS DB
# MAGIC instance in a private subnet. A developer wrote an AWS Lambda function with default settings to
# MAGIC insert, update, or delete data in the DB instance.
# MAGIC The developer needs to give the Lambda function the ability to connect to the DB instance privately
# MAGIC without using the public internet.
# MAGIC Which combination of steps will meet this requirement with the LEAST operational overhead?
# MAGIC (Choose two.)**
# MAGIC
# MAGIC - A. Turn on the public access setting for the DB instance.
# MAGIC - B. Update the security group of the DB instance to allow only Lambda function invocations on the database port.
# MAGIC - C. Configure the Lambda function to run in the same subnet that the DB instance uses.
# MAGIC - D. Attach the same security group to the Lambda function and the DB instance. Include a selfreferencing rule that allows access through the database port.
# MAGIC - E. Update the network ACL of the private subnet to include a self-referencing rule that allows access through the database port.
# MAGIC
# MAGIC B and C

# COMMAND ----------

# MAGIC %md
# MAGIC **33. A company has a frontend ReactJS website that uses Amazon API Gateway to invoke REST
# MAGIC APIs. The APIs perform the functionality of the website. A data engineer needs to write a Python
# MAGIC script that can be occasionally invoked through API Gateway. The code must return results to API
# MAGIC Gateway.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Deploy a custom Python script on an Amazon Elastic Container Service (Amazon ECS) cluster.
# MAGIC - B. Create an AWS Lambda Python function with provisioned concurrency.
# MAGIC - C. Deploy a custom Python script that can integrate with API Gateway on Amazon Elastic Kubernetes Service (Amazon EKS).
# MAGIC - D. Create an AWS Lambda function. Ensure that the function is warm by scheduling an Amazon EventBridge rule to invoke the Lambda function every 5 minutes by using mock events.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **A company has a production AWS account that runs company workloads. The company's
# MAGIC security team created a security AWS account to store and analyse security logs from the production
# MAGIC AWS account. The security logs in the production AWS account are stored in Amazon CloudWatch
# MAGIC Logs. The company needs to use Amazon Kinesis Data Streams to deliver the security logs to the
# MAGIC security AWS account.
# MAGIC Which solution will meet these requirements?**
# MAGIC
# MAGIC - A. Create a destination data stream in the production AWS account. In the security AWS account,create an IAM role that has cross-account permissions to Kinesis Data Streams in the production
# MAGIC AWS account.
# MAGIC - B. Create a destination data stream in the security AWS account. Create an IAM role and a trust
# MAGIC policy to grant CloudWatch Logs the permission to put data into the stream. Create a subscription filter in the security AWS account.
# MAGIC - C. Create a destination data stream in the production AWS account. In the production AWS account,
# MAGIC create an IAM role that has cross-account permissions to Kinesis Data Streams in the security AWS
# MAGIC account.
# MAGIC - D. Create a destination data stream in the security AWS account. Create an IAM role and a trust
# MAGIC policy to grant CloudWatch Logs the permission to put data into the stream. Create a subscription
# MAGIC filter in the production AWS account.
# MAGIC
# MAGIC D

# COMMAND ----------

# MAGIC %md
# MAGIC **35. A company uses Amazon S3 to store semi-structured data in a transactional data lake. Some of
# MAGIC the data files are small, but other data files are tens of terabytes. A data engineer must perform a
# MAGIC change data capture (CDC) operation to identify changed data from the data source. The data source
# MAGIC sends a full snapshot as a JSON file every day and ingests the changed data into the data lake.
# MAGIC Which solution will capture the changed data MOST cost-effectively?**
# MAGIC
# MAGIC - A. Create an AWS Lambda function to identify the changes between the previous data and the current data. Configure the Lambda function to ingest the changes into the data lake.
# MAGIC - B. Ingest the data into Amazon RDS for MySQL. Use AWS Database Migration Service (AWS
# MAGIC DMS) to write the changed data to the data lake.
# MAGIC - C. Use an open source data lake format to merge the data source with the S3 data lake to insert the
# MAGIC new data and update the existing data.
# MAGIC - D. Ingest the data into an Amazon Aurora MySQL DB instance that runs Aurora Serverless. Use
# MAGIC AWS Database Migration Service (AWS DMS) to write the changed data to the data lake.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **36. A data engineer runs Amazon Athena queries on data that is in an Amazon S3 bucket. The
# MAGIC Athena queries use AWS Glue Data Catalog as a metadata table. The data engineer notices that the Athena query plans are experiencing a performance bottleneck. The data engineer determines that the cause of the performance bottleneck is the large number of partitions that are in the S3 bucket. The data engineer must resolve the performance bottleneck and reduce Athena query planning time. Which solutions will meet these requirements? (Choose two.)**
# MAGIC
# MAGIC - A. Create an AWS Glue partition index. Enable partition filtering.
# MAGIC - B. Bucket the data based on a column that the data have in common in a WHERE clause of the user query.
# MAGIC - C. Use Athena partition projection based on the S3 bucket prefix.
# MAGIC - D. Transform the data that is in the S3 bucket to Apache Parquet format.
# MAGIC - E. Use the Amazon EMR S3DistCP utility to combine smaller objects in the S3 bucket into larger objects.
# MAGIC
# MAGIC A and C

# COMMAND ----------

# MAGIC %md
# MAGIC **37. A data engineer must manage the ingestion of real-time streaming data into AWS. The data
# MAGIC engineer wants to perform real-time analytics on the incoming streaming data by using time-based
# MAGIC aggregations over a window of up to 30 minutes. The data engineer needs a solution that is highly
# MAGIC fault tolerant.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC - A. Use an AWS Lambda function that includes both the business and the analytics logic to perform time-based aggregations over a window of up to 30 minutes for the data in Amazon Kinesis Data Streams.
# MAGIC - B. Use Amazon Managed Service for Apache Flink (previously known as Amazon Kinesis Data Analytics) to analyse the data that might occasionally contain duplicates by using multiple types of aggregations.
# MAGIC - C. Use an AWS Lambda function that includes both the business and the analytics logic to perform aggregations for a tumbling window of up to 30 minutes, based on the event timestamp.
# MAGIC - D. Use Amazon Managed Service for Apache Flink (previously known as Amazon Kinesis Data Analytics) to analyse the data by using multiple types of aggregations to perform time-based analytics over a window of up to 30 minutes.
# MAGIC
# MAGIC D

# COMMAND ----------

# MAGIC %md
# MAGIC **38. A company is planning to upgrade its Amazon Elastic Block Store (Amazon EBS) General
# MAGIC Purpose SSD storage from gp2 to gp3. The company wants to prevent any interruptions in its
# MAGIC Amazon EC2 instances that will cause data loss during the migration to the upgraded storage.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC - A. Create snapshots of the gp2 volumes. Create new gp3 volumes from the snapshots. Attach the new gp3 volumes to the EC2 instances.
# MAGIC - B. Create new gp3 volumes. Gradually transfer the data to the new gp3 volumes. When the transfer is complete, mount the new gp3 volumes to the EC2 instances to replace the gp2 volumes.
# MAGIC - C. Change the volume type of the existing gp2 volumes to gp3. Enter new values for volume size, IOPS, and throughput.
# MAGIC - D. Use AWS DataSync to create new gp3 volumes. Transfer the data from the original gp2 volumes to the new gp3 volumes.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **39. A company is migrating its database servers from Amazon EC2 instances that run Microsoft
# MAGIC SQL Server to Amazon RDS for Microsoft SQL Server DB instances. The company's analytics
# MAGIC team must export large data elements every day until the migration is complete. The data elements
# MAGIC are the result of SQL joins across multiple tables. The data must be in Apache Parquet format. The
# MAGIC analytics team must store the data in Amazon S3.
# MAGIC Which solution will meet these requirements in the MOST operationally efficient way?**
# MAGIC
# MAGIC - A. Create a view in the EC2 instance-based SQL Server databases that contains the required data
# MAGIC elements. Create an AWS Glue job that selects the data directly from the view and transfers the data
# MAGIC in Parquet format to an S3 bucket. Schedule the AWS Glue job to run every day.
# MAGIC - B. Schedule SQL Server Agent to run a daily SQL query that selects the desired data elements from
# MAGIC the EC2 instance-based SQL Server databases. Configure the query to direct the output .csv objects
# MAGIC to an S3 bucket. Create an S3 event that invokes an AWS Lambda function to transform the output
# MAGIC format from .csv to Parquet.
# MAGIC - C. Use a SQL query to create a view in the EC2 instance-based SQL Server databases that contains
# MAGIC the required data elements. Create and run an AWS Glue crawler to read the view. Create an AWS
# MAGIC Glue job that retrieves the data and transfers the data in Parquet format to an S3 bucket. Schedule
# MAGIC the AWS Glue job to run every day.
# MAGIC - D. Create an AWS Lambda function that queries the EC2 instance-based databases by using Java
# MAGIC Database Connectivity (JDBC). Configure the Lambda function to retrieve the required data,
# MAGIC transform the data into Parquet format, and transfer the data into an S3 bucket. Use Amazon
# MAGIC EventBridge to schedule the Lambda function to run every day.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **40. A data engineering team is using an Amazon Redshift data warehouse for operational reporting.
# MAGIC The team wants to prevent performance issues that might result from long-running queries. A data
# MAGIC engineer must choose a system table in Amazon Redshift to record anomalies when a query
# MAGIC optimizer identifies conditions that might indicate performance issues. Which table views should
# MAGIC the data engineer use to meet this requirement?**
# MAGIC - A. STL_USAGE_CONTROL
# MAGIC - B. STL_ALERT_EVENT_LOG
# MAGIC - C. STL_QUERY_METRICS
# MAGIC - D. STL_PLAN_INFO
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **41. A data engineer must ingest a source of structured data that is in .csv format into an Amazon S3
# MAGIC data lake. The .csv files contain 15 columns. Data analysts need to run Amazon Athena queries on
# MAGIC one or two columns of the dataset. The data analysts rarely query the entire file. Which solution will
# MAGIC meet these requirements MOST cost-effectively?**
# MAGIC
# MAGIC - A. Use an AWS Glue PySpark job to ingest the source data into the data lake in .csv format.
# MAGIC - B. Create an AWS Glue extract, transform, and load (ETL) job to read from the .csv structured data source. Configure the job to ingest the data into the data lake in JSON format.
# MAGIC - C. Use an AWS Glue PySpark job to ingest the source data into the data lake in Apache Avro format.
# MAGIC - D. Create an AWS Glue extract, transform, and load (ETL) job to read from the .csv structured data source. Configure the job to write the data into the data lake in Apache Parquet format.
# MAGIC
# MAGIC D

# COMMAND ----------

# MAGIC %md
# MAGIC **42. A company has five offices in different AWS Regions. Each office has its own human resources
# MAGIC (HR) department that uses a unique IAM role. The company stores employee records in a data lake
# MAGIC that is based on Amazon S3 storage.
# MAGIC A data engineering team needs to limit access to the records. Each HR department should be able to
# MAGIC access records for only employees who are within the HR department's Region.
# MAGIC Which combination of steps should the data engineering team take to meet this requirement with the
# MAGIC LEAST operational overhead? (Choose two.)**
# MAGIC
# MAGIC - A. Use data filters for each Region to register the S3 paths as data locations.
# MAGIC - B. Register the S3 path as an AWS Lake Formation location.
# MAGIC - C. Modify the IAM roles of the HR departments to add a data filter for each department's Region.
# MAGIC - D. Enable fine-grained access control in AWS Lake Formation. Add a data filter for each Region.
# MAGIC - E. Create a separate S3 bucket for each Region. Configure an IAM policy to allow S3 access. Restrict access based on Region.
# MAGIC
# MAGIC B and D

# COMMAND ----------

# MAGIC %md
# MAGIC **43. A company uses AWS Step Functions to orchestrate a data pipeline. The pipeline consists of
# MAGIC Amazon EMR jobs that ingest data from data sources and store the data in an Amazon S3 bucket.
# MAGIC The pipeline also includes EMR jobs that load the data to Amazon Redshift.
# MAGIC The company's cloud infrastructure team manually built a Step Functions state machine. The cloud
# MAGIC infrastructure team launched an EMR cluster into a VPC to support the EMR jobs. However, the
# MAGIC deployed Step Functions state machine is not able to run the EMR jobs.
# MAGIC Which combination of steps should the company take to identify the reason the Step Functions state
# MAGIC machine is not able to run the EMR jobs? (Choose two.)**
# MAGIC
# MAGIC - A. Use AWS CloudFormation to automate the Step Functions state machine deployment. Create a
# MAGIC step to pause the state machine during the EMR jobs that fail. Configure the step to wait for a
# MAGIC human user to send approval through an email message. Include details of the EMR task in the
# MAGIC email message for further analysis.
# MAGIC - B. Verify that the Step Functions state machine code has all IAM permissions that are necessary to
# MAGIC create and run the EMR jobs. Verify that the Step Functions state machine code also includes IAM
# MAGIC permissions to access the Amazon S3 buckets that the EMR jobs use. Use Access Analyzer for S3 to
# MAGIC check the S3 access properties.
# MAGIC - C. Check for entries in Amazon CloudWatch for the newly created EMR cluster. Change the AWS
# MAGIC Step Functions state machine code to use Amazon EMR on EKS. Change the IAM access policies
# MAGIC and the security group configuration for the Step Functions state machine code to reflect inclusion
# MAGIC of Amazon Elastic Kubernetes Service (Amazon EKS).
# MAGIC - D. Query the flow logs for the VPC. Determine whether the traffic that originates from the EMR
# MAGIC cluster can successfully reach the data providers. Determine whether any security group that might
# MAGIC be attached to the Amazon EMR cluster allows connections to the data source servers on the
# MAGIC informed ports.
# MAGIC - E. Check the retry scenarios that the company configured for the EMR jobs. Increase the number of
# MAGIC seconds in the interval between each EMR task. Validate that each fallback state has the appropriate
# MAGIC catch for each decision state. Configure an Amazon Simple Notification Service (Amazon SNS)
# MAGIC topic to store the error messages.
# MAGIC
# MAGIC B and D

# COMMAND ----------

# MAGIC %md
# MAGIC **44. A company is developing an application that runs on Amazon EC2 instances. Currently, the data
# MAGIC that the application generates is temporary. However, the company needs to persist the data, even if
# MAGIC the EC2 instances are terminated.
# MAGIC A data engineer must launch new EC2 instances from an Amazon Machine Image (AMI) and
# MAGIC configure the instances to preserve the data.
# MAGIC Which solution will meet this requirement?**
# MAGIC - A. Launch new EC2 instances by using an AMI that is backed by an EC2 instance store volume that contains the application data. Apply the default settings to the EC2 instances.
# MAGIC - B. Launch new EC2 instances by using an AMI that is backed by a root Amazon Elastic Block Store (Amazon EBS) volume that contains the application data. Apply the default settings to the EC2 instances.
# MAGIC - C. Launch new EC2 instances by using an AMI that is backed by an EC2 instance store volume. Attach an Amazon Elastic Block Store (Amazon EBS) volume to contain the application data. Apply the default settings to the EC2 instances.
# MAGIC - D. Launch new EC2 instances by using an AMI that is backed by an Amazon Elastic Block Store (Amazon EBS) volume. Attach an additional EC2 instance store volume to contain the application data. Apply the default settings to the EC2 instances
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **45. A company uses Amazon Athena to run SQL queries for extract, transform, and load (ETL)
# MAGIC tasks by using Create Table As Select (CTAS). The company must use Apache Spark instead of
# MAGIC SQL to generate analytics.
# MAGIC Which solution will give the company the ability to use Spark to access Athena?**
# MAGIC
# MAGIC - A. Athena query settings
# MAGIC - B. Athena workgroup
# MAGIC - C. Athena data source
# MAGIC - D. Athena query editor
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **46. A company needs to partition the Amazon S3 storage that the company uses for a data lake. The
# MAGIC partitioning will use a path of the S3 object keys in the following format: s3://bucket/prefix/
# MAGIC year=2023/month=01/day=01.
# MAGIC A data engineer must ensure that the AWS Glue Data Catalog synchronises with the S3 storage
# MAGIC when the company adds new partitions to the bucket.
# MAGIC Which solution will meet these requirements with the LEAST latency?**
# MAGIC
# MAGIC - A. Schedule an AWS Glue crawler to run every morning.
# MAGIC - B. Manually run the AWS Glue CreatePartition API twice each day.
# MAGIC - C. Use code that writes data to Amazon S3 to invoke the Boto3 AWS Glue create_partition API call.
# MAGIC - D. Run the MSCK REPAIR TABLE command from the AWS Glue console.
# MAGIC
# MAGIC C
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **47. A media company uses software as a service (SaaS) applications to gather data by using thirdparty tools. The company needs to store the data in an Amazon S3 bucket. The company will use
# MAGIC Amazon Redshift to perform analytics based on the data. Which AWS service or feature will meet
# MAGIC these requirements with the LEAST operational overhead?**
# MAGIC - A. Amazon Managed Streaming for Apache Kafka (Amazon MSK)
# MAGIC - B. Amazon AppFlow
# MAGIC - C. AWS Glue Data Catalog
# MAGIC - D. Amazon Kinesis
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **48. A data engineer is using Amazon Athena to analyze sales data that is in Amazon S3. The data
# MAGIC engineer writes a query to retrieve sales amounts for 2023 for several products from a table named
# MAGIC sales_data. However, the query does not return results for all of the products that are in the
# MAGIC sales_data table. The data engineer needs to troubleshoot the query to resolve the issue.
# MAGIC The data engineer's original query is as follows:
# MAGIC SELECT product_name, sum(sales_amount)
# MAGIC FROM sales_data
# MAGIC WHERE year = 2023
# MAGIC GROUP BY product_name
# MAGIC How should the data engineer modify the Athena query to meet these requirements?**
# MAGIC
# MAGIC - A. Replace sum(sales_amount) with count(*) for the aggregation.
# MAGIC - B. Change WHERE year = 2023 to WHERE extract(year FROM sales_data) = 2023.
# MAGIC - C. Add HAVING sum(sales_amount) > 0 after the GROUP BY clause.
# MAGIC - D. Remove the GROUP BY clause.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **49. A data engineer has a one-time task to read data from objects that are in Apache Parquet format
# MAGIC in an Amazon S3 bucket. The data engineer needs to query only one column of the data. Which
# MAGIC solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Configure an AWS Lambda function to load data from the S3 bucket into a pandas dataframe. Write a SQL SELECT statement on the dataframe to query the required column.
# MAGIC - B. Use S3 Select to write a SQL SELECT statement to retrieve the required column from the S3 objects.
# MAGIC - C. Prepare an AWS Glue DataBrew project to consume the S3 objects and to query the required column.
# MAGIC - D. Run an AWS Glue crawler on the S3 objects. Use a SQL SELECT statement in Amazon Athena to query the required column.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **50. A company uses Amazon Redshift for its data warehouse. The company must automate refresh
# MAGIC schedules for Amazon Redshift materialised views. Which solution will meet this requirement with
# MAGIC the LEAST effort?**
# MAGIC - A. Use Apache Airflow to refresh the materialised views.
# MAGIC - B. Use an AWS Lambda user-defined function (UDF) within Amazon Redshift to refresh the materialised views.
# MAGIC - C. Use the query editor v2 in Amazon Redshift to refresh the materialised views.
# MAGIC - D. Use an AWS Glue workflow to refresh the materialised views.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **51. A data engineer must orchestrate a data pipeline that consists of one AWS Lambda function and
# MAGIC one AWS Glue job. The solution must integrate with AWS services. Which solution will meet these
# MAGIC requirements with the LEAST management overhead?**
# MAGIC
# MAGIC - A. Use an AWS Step Functions workflow that includes a state machine. Configure the state machine to run the Lambda function and then the AWS Glue job.
# MAGIC - B. Use an Apache Airflow workflow that is deployed on an Amazon EC2 instance. Define a directed acyclic graph (DAG) in which the first task is to call the Lambda function and the second task is to call the AWS Glue job.
# MAGIC - C. Use an AWS Glue workflow to run the Lambda function and then the AWS Glue job.
# MAGIC - D. Use an Apache Airflow workflow that is deployed on Amazon Elastic Kubernetes Service (Amazon EKS). Define a directed acyclic graph (DAG) in which the first task is to call the Lambda function and the second task is to call the AWS Glue job.

# COMMAND ----------

# MAGIC %md
# MAGIC **52. A company needs to set up a data catalog and metadata management for data sources that run in
# MAGIC the AWS Cloud. The company will use the data catalog to maintain the metadata of all the objects
# MAGIC that are in a set of data stores. The data stores include structured sources such as Amazon RDS and
# MAGIC Amazon Redshift. The data stores also include semistructured sources such as JSON files and .xml
# MAGIC files that are stored in Amazon S3.
# MAGIC The company needs a solution that will update the data catalog on a regular basis. The solution also
# MAGIC must detect changes to the source metadata.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Use Amazon Aurora as the data catalog. Create AWS Lambda functions that will connect to the data catalog. Configure the Lambda functions to gather the metadata information from multiple sources and to update the Aurora data catalog. Schedule the Lambda functions to run periodically.
# MAGIC - B. Use the AWS Glue Data Catalog as the central metadata repository. Use AWS Glue crawlers to connect to multiple data stores and to update the Data Catalog with metadata changes. Schedule the crawlers to run periodically to update the metadata catalog.
# MAGIC - C. Use Amazon DynamoDB as the data catalog. Create AWS Lambda functions that will connect to the data catalog. Configure the Lambda functions to gather the metadata information from multiple sources and to update the DynamoDB data catalog. Schedule the Lambda functions to run periodically.
# MAGIC - D. Use the AWS Glue Data Catalog as the central metadata repository. Extract the schema for Amazon RDS and Amazon Redshift sources, and build the Data Catalog. Use AWS Glue crawlers for data that is in Amazon S3 to infer the schema and to automatically update the Data Catalog.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **53. A company stores data from an application in an Amazon DynamoDB table that operates in
# MAGIC provisioned capacity mode. The workloads of the application have predictable throughput load on a
# MAGIC regular schedule. Every Monday, there is an immediate increase in activity early in the morning.
# MAGIC The application has very low usage during weekends.
# MAGIC The company must ensure that the application performs consistently during peak usage times.
# MAGIC Which solution will meet these requirements in the MOST cost-effective way?**
# MAGIC
# MAGIC - A. Increase the provisioned capacity to the maximum capacity that is currently present during peak load times.
# MAGIC - B. Divide the table into two tables. Provision each table with half of the provisioned capacity of the original table. Spread queries evenly across both tables.
# MAGIC - C. Use AWS Application Auto Scaling to schedule higher provisioned capacity for peak usage times. Schedule lower capacity during off-peak times.
# MAGIC - D. Change the capacity mode from provisioned to on-demand. Configure the table to scale up and scale down based on the load on the table.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **54. A company is planning to migrate on-premises Apache Hadoop clusters to Amazon EMR. The
# MAGIC company also needs to migrate a data catalog into a persistent storage solution. The company
# MAGIC currently stores the data catalog in an on-premises Apache Hive metastore on the Hadoop clusters.
# MAGIC The company requires a serverless solution to migrate the data catalog.
# MAGIC Which solution will meet these requirements MOST cost-effectively?**
# MAGIC
# MAGIC - A. Use AWS Database Migration Service (AWS DMS) to migrate the Hive metastore into Amazon S3. Configure AWS Glue Data Catalog to scan Amazon S3 to produce the data catalog.
# MAGIC - B. Configure a Hive metastore in Amazon EMR. Migrate the existing on-premises Hive metastore into Amazon EMR. Use AWS Glue Data Catalog to store the company's data catalog as an external data catalog.
# MAGIC - C. Configure an external Hive metastore in Amazon EMR. Migrate the existing on-premises Hive metastore into Amazon EMR. Use Amazon Aurora MySQL to store the company's data catalog.
# MAGIC - D. Configure a new Hive metastore in Amazon EMR. Migrate the existing on-premises Hive metastore into Amazon EMR. Use the new metastore as the company's data catalog.
# MAGIC
# MAGIC A

# COMMAND ----------

# MAGIC %md
# MAGIC **55. A company uses an Amazon Redshift provisioned cluster as its database. The Redshift cluster
# MAGIC has five reserved ra3.4xlarge nodes and uses key distribution. A data engineer notices that one of the
# MAGIC nodes frequently has a CPU load over 90%. SQL queries that run on the node are queued. The other
# MAGIC four nodes usually have a CPU load under 15% during daily operations.
# MAGIC The data engineer wants to maintain the current number of compute nodes. The data engineer also
# MAGIC wants to balance the load more evenly across all five compute nodes.
# MAGIC Which solution will meet these requirements?**
# MAGIC
# MAGIC - A. Change the sort key to be the data column that is most often used in a WHERE clause of the SQL SELECT statement.
# MAGIC - B. Change the distribution key to the table column that has the largest dimension.
# MAGIC - C. Upgrade the reserved node from ra3.4xlarge to ra3.16xlarge.
# MAGIC - D. Change the primary key to be the data column that is most often used in a WHERE clause of the SQL SELECT statement.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **56. A security company stores IoT data that is in JSON format in an Amazon S3 bucket. The data
# MAGIC structure can change when the company upgrades the IoT devices. The company wants to create a
# MAGIC data catalog that includes the IoT data. The company's analytics department will use the data
# MAGIC catalog to index the data.
# MAGIC Which solution will meet these requirements MOST cost-effectively?**
# MAGIC
# MAGIC - A. Create an AWS Glue Data Catalog. Configure an AWS Glue Schema Registry. Create a new AWS Glue workload to orchestrate the ingestion of the data that the analytics department will use into Amazon Redshift Serverless.
# MAGIC - B. Create an Amazon Redshift provisioned cluster. Create an Amazon Redshift Spectrum database for the analytics department to explore the data that is in Amazon S3. Create Redshift stored procedures to load the data into Amazon Redshift.
# MAGIC - C. Create an Amazon Athena workgroup. Explore the data that is in Amazon S3 by using Apache Spark through Athena. Provide the Athena workgroup schema and tables to the analytics department.
# MAGIC - D. Create an AWS Glue Data Catalog. Configure an AWS Glue Schema Registry. Create AWS Lambda user-defined functions (UDFs) by using the Amazon Redshift Data API. Create an AWS Step Functions job to orchestrate the ingestion of the data that the analytics department will use into Amazon Redshift Serverless.
# MAGIC
# MAGIC A

# COMMAND ----------

# MAGIC %md
# MAGIC **57. A company stores details about transactions in an Amazon S3 bucket. The company wants to log
# MAGIC all writes to the S3 bucket into another S3 bucket that is in the same AWS Region.
# MAGIC Which solution will meet this requirement with the LEAST operational effort?**
# MAGIC
# MAGIC - A. Configure an S3 Event Notifications rule for all activities on the transactions S3 bucket to invoke an AWS Lambda function. Program the Lambda function to write the event to Amazon Kinesis Data Firehose. Configure Kinesis Data Firehose to write the event to the logs S3 bucket.
# MAGIC - B. Create a trail of management events in AWS CloudTrail. Configure the trail to receive data from the transactions S3 bucket. Specify an empty prefix and write-only events. Specify the logs S3 bucket as the destination bucket.
# MAGIC - C. Configure an S3 Event Notifications rule for all activities on the transactions S3 bucket to invoke an AWS Lambda function. Program the Lambda function to write the events to the logs S3 bucket.
# MAGIC - D. Create a trail of data events in AWS CloudTrail. Configure the trail to receive data from the transactions S3 bucket. Specify an empty prefix and write-only events. Specify the logs S3 bucket as the destination bucket.
# MAGIC
# MAGIC D

# COMMAND ----------

# MAGIC %md
# MAGIC **58. A data engineer needs to maintain a central metadata repository that users access through
# MAGIC Amazon EMR and Amazon Athena queries. The repository needs to provide the schema and
# MAGIC properties of many tables. Some of the metadata is stored in Apache Hive. The data engineer needs
# MAGIC to import the metadata from Hive into the central metadata repository.
# MAGIC Which solution will meet these requirements with the LEAST development effort?**
# MAGIC
# MAGIC - A. Use Amazon EMR and Apache Ranger.
# MAGIC - B. Use a Hive metastore on an EMR cluster.
# MAGIC - C. Use the AWS Glue Data Catalog.
# MAGIC - D. Use a metastore on an Amazon RDS for MySQL DB instance.

# COMMAND ----------

# MAGIC %md
# MAGIC **59. A company needs to build a data lake in AWS. The company must provide row-level data access
# MAGIC and column-level data access to specific teams. The teams will access the data by using Amazon
# MAGIC Athena, Amazon Redshift Spectrum, and Apache Hive from Amazon EMR.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Use Amazon S3 for data lake storage. Use S3 access policies to restrict data access by rows and columns. Provide data access through Amazon S3.
# MAGIC - B. Use Amazon S3 for data lake storage. Use Apache Ranger through Amazon EMR to restrict data access by rows and columns. Provide data access by using Apache Pig.
# MAGIC - C. Use Amazon Redshift for data lake storage. Use Redshift security policies to restrict data access by rows and columns. Provide data access by using Apache Spark and Amazon Athena federated queries.
# MAGIC - D. Use Amazon S3 for data lake storage. Use AWS Lake Formation to restrict data access by rows and columns. Provide data access through AWS Lake Formation.

# COMMAND ----------

# MAGIC %md
# MAGIC **60. An airline company is collecting metrics about flight activities for analytics. The company is
# MAGIC conducting a proof of concept (POC) test to show how analytics can provide insights that the
# MAGIC company can use to increase on-time departures.
# MAGIC The POC test uses objects in Amazon S3 that contain the metrics in .csv format. The POC test uses
# MAGIC Amazon Athena to query the data. The data is partitioned in the S3 bucket by date. As the amount of
# MAGIC data increases, the company wants to optimise the storage solution to improve query performance.
# MAGIC Which combination of solutions will meet these requirements? (Choose two.)**
# MAGIC
# MAGIC - A. Add a randomised string to the beginning of the keys in Amazon S3 to get more throughput across partitions.
# MAGIC - B. Use an S3 bucket that is in the same account that uses Athena to query the data.
# MAGIC - C. Use an S3 bucket that is in the same AWS Region where the company runs Athena queries.
# MAGIC - D. Preprocess the .csv data to JSON format by fetching only the document keys that the query requires.
# MAGIC - E. Preprocess the .csv data to Apache Parquet format by fetching only the data blocks that are needed for predicates.
# MAGIC
# MAGIC C and E

# COMMAND ----------

# MAGIC %md
# MAGIC **61. A company uses Amazon RDS for MySQL as the database for a critical application. The
# MAGIC database workload is mostly writes, with a small number of reads.
# MAGIC A data engineer notices that the CPU utilisation of the DB instance is very high. The high CPU
# MAGIC utilisation is slowing down the application. The data engineer must reduce the CPU utilisation of
# MAGIC the DB instance.
# MAGIC Which actions should the data engineer take to meet this requirement? (Choose two.)**
# MAGIC
# MAGIC - A. Use the Performance Insights feature of Amazon RDS to identify queries that have high CPU utilisation. Optimise the problematic queries.
# MAGIC - B. Modify the database schema to include additional tables and indexes.
# MAGIC - C. Reboot the RDS DB instance once each week.
# MAGIC - D. Upgrade to a larger instance size.
# MAGIC - E. Implement caching to reduce the database query load
# MAGIC
# MAGIC A and D

# COMMAND ----------

# MAGIC %md
# MAGIC **62. A company has used an Amazon Redshift table that is named Orders for 6 months. The
# MAGIC company performs weekly updates and deletes on the table. The table has an interleaved sort key on
# MAGIC a column that contains AWS Regions.
# MAGIC The company wants to reclaim disk space so that the company will not run out of storage space.
# MAGIC The company also wants to analyse the sort key column.
# MAGIC Which Amazon Redshift command will meet these requirements?**
# MAGIC
# MAGIC - A. VACUUM FULL Orders
# MAGIC - B. VACUUM DELETE ONLY Orders
# MAGIC - C. VACUUM REINDEX Orders
# MAGIC - D. VACUUM SORT ONLY Orders

# COMMAND ----------

# MAGIC %md
# MAGIC **63. A manufacturing company wants to collect data from sensors. A data engineer needs to
# MAGIC implement a solution that ingests sensor data in near real-time.
# MAGIC The solution must store the data to a persistent data store. The solution must store the data in nested
# MAGIC JSON format. The company must have the ability to query from the data store with a latency of less
# MAGIC than 10 milliseconds.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Use a self-hosted Apache Kafka cluster to capture the sensor data. Store the data in Amazon S3 or querying.
# MAGIC - B. Use AWS Lambda to process the sensor data. Store the data in Amazon S3 for querying.
# MAGIC - C. Use Amazon Kinesis Data Streams to capture the sensor data. Store the data in Amazon DynamoDB for querying.
# MAGIC - D. Use Amazon Simple Queue Service (Amazon SQS) to buffer incoming sensor data. Use AWS Glue to store the data in Amazon RDS for querying.

# COMMAND ----------

# MAGIC %md
# MAGIC **64. A company stores data in a data lake that is in Amazon S3. Some data that the company stores
# MAGIC in the data lake contains personally identifiable information (PII). Multiple user groups need to
# MAGIC access the raw data. The company must ensure that user groups can access only the PII that they
# MAGIC require.
# MAGIC Which solution will meet these requirements with the LEAST effort?**
# MAGIC
# MAGIC - A. Use Amazon Athena to query the data. Set up AWS Lake Formation and create data filters to establish levels of access for the company’s IAM roles. Assign each user to the IAM role that matches the user’s PII access requirements.
# MAGIC - B. Use Amazon QuickSight to access the data. Use column-level security features in QuickSight to limit the PII that users can retrieve from Amazon S3 by using Amazon Athena. Define QuickSight access levels based on the PII access requirements of the users.
# MAGIC - C. Build a custom query builder UI that will run Athena queries in the background to access the data. Create user groups in Amazon Cognito. Assign access levels to the user groups based on the PII access requirements of the users.
# MAGIC - D. Create IAM roles that have different levels of granular access. Assign the IAM roles to IAM user groups. Use an identity-based policy to assign access levels to user groups at the column level.

# COMMAND ----------

# MAGIC %md
# MAGIC **65. A data engineer must build an extract, transform, and load (ETL) pipeline to process and load
# MAGIC data from 10 source systems into 10 tables that are in an Amazon Redshift database. All the source
# MAGIC systems generate .csv, JSON, or Apache Parquet files every 15 minutes. The source systems all
# MAGIC deliver files into one Amazon S3 bucket. The file sizes range from 10 MB to 20 GB. The ETL
# MAGIC pipeline must function correctly despite changes to the data schema.
# MAGIC Which data pipeline solutions will meet these requirements? (Choose two.)**
# MAGIC
# MAGIC - A. Use an Amazon EventBridge rule to run an AWS Glue job every 15 minutes. Configure the AWS Glue job to process and load the data into the Amazon Redshift tables.
# MAGIC - B. Use an Amazon EventBridge rule to invoke an AWS Glue workflow job every 15 minutes. Configure the AWS Glue workflow to have an on-demand trigger that runs an AWS Glue crawler and then runs an AWS Glue job when the crawler finishes running successfully. Configure the AWS Glue job to process and load the data into the Amazon Redshift tables.
# MAGIC - C. Configure an AWS Lambda function to invoke an AWS Glue crawler when a file is loaded into the S3 bucket. Configure an AWS Glue job to process and load the data into the Amazon Redshift tables. Create a second Lambda function to run the AWS Glue job. Create an Amazon EventBridge rule to invoke the second Lambda function when the AWS Glue crawler finishes running successfully.
# MAGIC - D. Configure an AWS Lambda function to invoke an AWS Glue workflow when a file is loaded into the S3 bucket. Configure the AWS Glue workflow to have an on-demand trigger that runs an AWS Glue crawler and then runs an AWS Glue job when the crawler finishes running successfully. Configure the AWS Glue job to process and load the data into the Amazon Redshift tables.
# MAGIC - E. Configure an AWS Lambda function to invoke an AWS Glue job when a file is loaded into the S3 bucket. Configure the AWS Glue job to read the files from the S3 bucket into an Apache Spark DataFrame. Configure the AWS Glue job to also put smaller partitions of the DataFrame into an Amazon Kinesis Data Firehose delivery stream. Configure the delivery stream to load data into the Amazon Redshift tables.
# MAGIC
# MAGIC B and D

# COMMAND ----------

# MAGIC %md
# MAGIC **66. A financial company wants to use Amazon Athena to run on-demand SQL queries on a petabytescale dataset to support a business intelligence (BI) application. An AWS Glue job that runs during
# MAGIC non-business hours updates the dataset once every day. The BI application has a standard data
# MAGIC refresh frequency of 1 hour to comply with company policies.
# MAGIC A data engineer wants to cost optimise the company's use of Amazon Athena without adding any
# MAGIC additional infrastructure costs.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Configure an Amazon S3 Lifecycle policy to move data to the S3 Glacier Deep Archive storage class after 1 day.
# MAGIC - B. Use the query result reuse feature of Amazon Athena for the SQL queries.
# MAGIC - C. Add an Amazon ElastiCache cluster between the BI application and Athena.
# MAGIC - D. Change the format of the files that are in the dataset to Apache Parquet.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **67. A company's data engineer needs to optimise the performance of table SQL queries. The
# MAGIC company stores data in an Amazon Redshift cluster. The data engineer cannot increase the size of
# MAGIC the cluster because of budget constraints.
# MAGIC The company stores the data in multiple tables and loads the data by using the EVEN distribution
# MAGIC style. Some tables are hundreds of gigabytes in size. Other tables are less than 10 MB in size.
# MAGIC Which solution will meet these requirements?**
# MAGIC
# MAGIC - A. Keep using the EVEN distribution style for all tables. Specify primary and foreign keys for all tables.
# MAGIC - B. Use the ALL distribution style for large tables. Specify primary and foreign keys for all tables.
# MAGIC - C. Use the ALL distribution style for rarely updated small tables. Specify primary and foreign keys for all tables.
# MAGIC - D. Specify a combination of distribution, sort, and partition keys for all tables.

# COMMAND ----------

# MAGIC %md
# MAGIC **68. A company receives .csv files that contain physical address data. The data is in columns that
# MAGIC have the following names: Door_No, Street_Name, City, and Zip_Code. The company wants to
# MAGIC create a single column to store these values in the following format:
# MAGIC `{
# MAGIC  "Door_No": "24",
# MAGIC  "Street_Name": "AAA street",
# MAGIC  "City": "BBB",
# MAGIC  "Zip_Code": "111111"
# MAGIC }`
# MAGIC Which solution will meet this requirement with the LEAST coding effort?**
# MAGIC
# MAGIC - A. Use AWS Glue DataBrew to read the files. Use the NEST_TO_ARRAY transformation to create the new column.
# MAGIC - B. Use AWS Glue DataBrew to read the files. Use the NEST_TO_MAP transformation to create the new column.
# MAGIC - C. Use AWS Glue DataBrew to read the files. Use the PIVOT transformation to create the new column.
# MAGIC - D. Write a Lambda function in Python to read the files. Use the Python data dictionary type to create the new column.

# COMMAND ----------

# MAGIC %md
# MAGIC **69. A company receives call logs as Amazon S3 objects that contain sensitive customer information.
# MAGIC The company must protect the S3 objects by using encryption. The company must also use
# MAGIC encryption keys that only specific employees can access. Which solution will meet these
# MAGIC requirements with the LEAST effort?**
# MAGIC
# MAGIC - A. Use an AWS CloudHSM cluster to store the encryption keys. Configure the process that writes to Amazon S3 to make calls to CloudHSM to encrypt and decrypt the objects. Deploy an IAM policy that restricts access to the CloudHSM cluster.
# MAGIC - B. Use server-side encryption with customer-provided keys (SSE-C) to encrypt the objects that contain customer information. Restrict access to the keys that encrypt the objects.
# MAGIC - C. Use server-side encryption with AWS KMS keys (SSE-KMS) to encrypt the objects that contain customer information. Configure an IAM policy that restricts access to the KMS keys that encrypt the objects.
# MAGIC - D. Use server-side encryption with Amazon S3 managed keys (SSE-S3) to encrypt the objects that contain customer information. Configure an IAM policy that restricts access to the Amazon S3 managed keys that encrypt the objects.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC **70. A company stores petabytes of data in thousands of Amazon S3 buckets in the S3 Standard
# MAGIC storage class. The data supports analytics workloads that have unpredictable and variable data
# MAGIC access patterns.
# MAGIC The company does not access some data for months. However, the company must be able to
# MAGIC retrieve all data within milliseconds. The company needs to optimise S3 storage costs.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Use S3 Storage Lens standard metrics to determine when to move objects to more cost-optimised storage classes. Create S3 Lifecycle policies for the S3 buckets to move objects to cost-optimised storage classes. Continue to refine the S3 Lifecycle policies in the future to optimise storage costs.
# MAGIC - B. Use S3 Storage Lens activity metrics to identify S3 buckets that the company accesses infrequently. Configure S3 Lifecycle rules to move objects from S3 Standard to the S3 StandardInfrequent Access (S3 Standard-IA) and S3 Glacier storage classes based on the age of the data.
# MAGIC - C. Use S3 Intelligent-Tiering. Activate the Deep Archive Access tier.
# MAGIC - D. Use S3 Intelligent-Tiering. Use the default access tier.
# MAGIC
# MAGIC D

# COMMAND ----------

# MAGIC %md
# MAGIC **71. During a security review, a company identified a vulnerability in an AWS Glue job. The
# MAGIC company discovered that credentials to access an Amazon Redshift cluster were hard coded in the
# MAGIC job script. A data engineer must remediate the security vulnerability in the AWS Glue job. The
# MAGIC solution must securely store the credentials.
# MAGIC Which combination of steps should the data engineer take to meet these requirements? (Choose
# MAGIC two.)**
# MAGIC
# MAGIC - A. Store the credentials in the AWS Glue job parameters.
# MAGIC - B. Store the credentials in a configuration file that is in an Amazon S3 bucket.
# MAGIC - C. Access the credentials from a configuration file that is in an Amazon S3 bucket by using the AWS Glue job.
# MAGIC - D. Store the credentials in AWS Secrets Manager.
# MAGIC - E. Grant the AWS Glue job IAM role access to the stored credentials.
# MAGIC
# MAGIC D and E

# COMMAND ----------

# MAGIC %md
# MAGIC **72. A data engineer uses Amazon Redshift to run resource-intensive analytics processes once every
# MAGIC month. Every month, the data engineer creates a new Redshift provisioned cluster. The data
# MAGIC engineer deletes the Redshift provisioned cluster after the analytics processes are complete every
# MAGIC month. Before the data engineer deletes the cluster each month, the data engineer unloads backup
# MAGIC data from the cluster to an Amazon S3 bucket.
# MAGIC The data engineer needs a solution to run the monthly analytics processes that does not require the
# MAGIC data engineer to manage the infrastructure manually.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Use Amazon Step Functions to pause the Redshift cluster when the analytics processes are complete and to resume the cluster to run new processes every month.
# MAGIC - B. Use Amazon Redshift Serverless to automatically process the analytics workload.
# MAGIC - C. Use the AWS CLI to automatically process the analytics workload.
# MAGIC - D. Use AWS CloudFormation templates to automatically process the analytics workload
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **73. A company receives a daily file that contains customer data in .xls format. The company stores
# MAGIC the file in Amazon S3. The daily file is approximately 2 GB in size.
# MAGIC A data engineer concatenates the column in the file that contains customer first names and the
# MAGIC column that contains customer last names. The data engineer needs to determine the number of
# MAGIC distinct customers in the file.
# MAGIC Which solution will meet this requirement with the LEAST operational effort?**
# MAGIC
# MAGIC - A. Create and run an Apache Spark job in an AWS Glue notebook. Configure the job to read the S3 file and calculate the number of distinct customers.
# MAGIC - B. Create an AWS Glue crawler to create an AWS Glue Data Catalog of the S3 file. Run SQL queries from Amazon Athena to calculate the number of distinct customers.
# MAGIC - C. Create and run an Apache Spark job in Amazon EMR Serverless to calculate the number of distinct customers.
# MAGIC - D. Use AWS Glue DataBrew to create a recipe that uses the COUNT_DISTINCT aggregate function to calculate the number of distinct customers.
# MAGIC
# MAGIC D

# COMMAND ----------

# MAGIC %md
# MAGIC **74. A healthcare company uses Amazon Kinesis Data Streams to stream real-time health data from
# MAGIC wearable devices, hospital equipment, and patient records.
# MAGIC A data engineer needs to find a solution to process the streaming data and store the data in an
# MAGIC Amazon Redshift Serverless warehouse. The solution must support near real-time analytics of the
# MAGIC streaming data and the previous day's data.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Load data into Amazon Kinesis Data Firehose. Load the data into Amazon Redshift.
# MAGIC - B. Use the streaming ingestion feature of Amazon Redshift.
# MAGIC - C. Load the data into Amazon S3. Use the COPY command to load the data into Amazon Redshift.
# MAGIC - D. Use the Amazon Aurora zero-ETL integration with Amazon Redshift.
# MAGIC
# MAGIC B
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **75. A data engineer needs to use an Amazon QuickSight dashboard that is based on Amazon Athena
# MAGIC queries on data that is stored in an Amazon S3 bucket. When the data engineer connects to the
# MAGIC QuickSight dashboard, the data engineer receives an error message that indicates insufficient
# MAGIC permissions.
# MAGIC Which factors could cause the permissions-related errors? (Choose two.)**
# MAGIC
# MAGIC - A. There is no connection between QuickSight and Athena.
# MAGIC - B. The Athena tables are not cataloged.
# MAGIC - C. QuickSight does not have access to the S3 bucket.
# MAGIC - D. QuickSight does not have access to decrypt S3 data.
# MAGIC - E. There is no IAM role assigned to QuickSight.
# MAGIC
# MAGIC C and D

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **76. A company stores datasets in JSON format and .csv format in an Amazon S3 bucket. The
# MAGIC company has Amazon RDS for Microsoft SQL Server databases, Amazon DynamoDB tables that
# MAGIC are in provisioned capacity mode, and an Amazon Redshift cluster. A data engineering team must
# MAGIC develop a solution that will give data scientists the ability to query all data sources by using syntax
# MAGIC similar to SQL.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**  
# MAGIC
# MAGIC - A. Use AWS Glue to crawl the data sources. Store metadata in the AWS Glue Data Catalog. Use Amazon Athena to query the data. Use SQL for structured data sources. Use PartiQL for data that is stored in JSON format.
# MAGIC - B. Use AWS Glue to crawl the data sources. Store metadata in the AWS Glue Data Catalog. Use Redshift Spectrum to query the data. Use SQL for structured data sources. Use PartiQL for data that is stored in JSON format.
# MAGIC - C. Use AWS Glue to crawl the data sources. Store metadata in the AWS Glue Data Catalog. Use AWS Glue jobs to transform data that is in JSON format to Apache Parquet or .csv format. Store the transformed data in an S3 bucket. Use Amazon Athena to query the original and transformed data from the S3 bucket.
# MAGIC - D. Use AWS Lake Formation to create a data lake. Use Lake Formation jobs to transform the data from all data sources to Apache Parquet format. Store the transformed data in an S3 bucket. Use Amazon Athena or Redshift Spectrum to query the data.
# MAGIC
# MAGIC C

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **77. A data engineer is configuring Amazon SageMaker Studio to use AWS Glue interactive
# MAGIC sessions to prepare data for machine learning (ML) models. The data engineer receives an access
# MAGIC denied error when the data engineer tries to prepare the data by using SageMaker Studio.
# MAGIC Which change should the engineer make to gain access to SageMaker Studio?**
# MAGIC
# MAGIC - A. Add the AWSGlueServiceRole managed policy to the data engineer's IAM user.
# MAGIC - B. Add a policy to the data engineer's IAM user that includes the sts:AssumeRole for the AWS Glue and SageMaker service principals in the trust policy.
# MAGIC - C. Add the AmazonSageMakerFullAccess managed policy to the data engineer's IAM user.
# MAGIC - D. Add a policy to the data engineer's IAM user that allows the sts:AddAssociation for the AWS Glue and SageMaker service principals in the trust policy.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **78. A company extracts approximately 1 TB of data every day from data sources such as SAP
# MAGIC HANA, Microsoft SQL Server, MongoDB, Apache Kafka, and Amazon DynamoDB. Some of the
# MAGIC data sources have undefined data schemas or data schemas that change.
# MAGIC A data engineer must implement a solution that can detect the schema for these data sources. The
# MAGIC solution must extract, transform, and load the data to an Amazon S3 bucket. The company has a
# MAGIC service level agreement (SLA) to load the data into the S3 bucket within 15 minutes of data
# MAGIC creation.
# MAGIC Which solution will meet these requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Use Amazon EMR to detect the schema and to extract, transform, and load the data into the S3 bucket. Create a pipeline in Apache Spark.
# MAGIC - B. Use AWS Glue to detect the schema and to extract, transform, and load the data into the S3 bucket. Create a pipeline in Apache Spark.
# MAGIC - C. Create a PySpark program in AWS Lambda to extract, transform, and load the data into the S3 bucket.
# MAGIC - D. Create a stored procedure in Amazon Redshift to detect the schema and to extract, transform, and load the data into a Redshift Spectrum table. Access the table from Amazon S3.    
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **79. A company has multiple applications that use datasets that are stored in an Amazon S3 bucket.
# MAGIC The company has an ecommerce application that generates a dataset that contains personally
# MAGIC identifiable information (PII). The company has an internal analytics application that does not
# MAGIC require access to the PII.
# MAGIC To comply with regulations, the company must not share PII unnecessarily. A data engineer needs to
# MAGIC implement a solution that will redact PII dynamically, based on the needs of each application that
# MAGIC accesses the dataset.
# MAGIC Which solution will meet the requirements with the LEAST operational overhead?**
# MAGIC
# MAGIC - A. Create an S3 bucket policy to limit the access each application has. Create multiple copies of the dataset. Give each dataset copy the appropriate level of redaction for the needs of the application that accesses the copy.
# MAGIC - B. Create an S3 Object Lambda endpoint. Use the S3 Object Lambda endpoint to read data from the S3 bucket. Implement redaction logic within an S3 Object Lambda function to dynamically redact PII based on the needs of each application that accesses the data.
# MAGIC - C. Use AWS Glue to transform the data for each application. Create multiple copies of the dataset. Give each dataset copy the appropriate level of redaction for the needs of the application that accesses the copy.
# MAGIC - D. Create an API Gateway endpoint that has custom authorisers. Use the API Gateway endpoint to read data from the S3 bucket. Initiate a REST API call to dynamically redact PII based on the needs of each application that accesses the data.
# MAGIC
# MAGIC B

# COMMAND ----------

# MAGIC %md
# MAGIC **80. A data engineer needs to build an extract, transform, and load (ETL) job. The ETL job will
# MAGIC process daily incoming .csv files that users upload to an Amazon S3 bucket. The size of each S3
# MAGIC object is less than 100 MB.
# MAGIC Which solution will meet these requirements MOST cost-effectively?**
# MAGIC
# MAGIC - A. Write a custom Python application. Host the application on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster.
# MAGIC - B. Write a PySpark ETL script. Host the script on an Amazon EMR cluster.
# MAGIC - C. Write an AWS Glue PySpark job. Use Apache Spark to transform the data.
# MAGIC - D. Write an AWS Glue Python shell job. Use pandas to transform the data.
# MAGIC
# MAGIC D

# COMMAND ----------


