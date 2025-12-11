# Databricks notebook source
S3 Object lambda
     Redacting and enriching the objects for different applications through AWS lambda through access points
     s3 ------> --> original object --------> E-Commerce
        ------> Analytics ----> -------> supporting access point ---> lambda ----> Redacting the object -------> Analytics Platform
        ------> Marketing ----> -------> supporting access point ---> lambda ----> Enriching the object -------> Marketing Platform

Amazon EBS (Elastic Block Store)
    EBS is a networks drive you can attach to your instances while they run
    persist data even after terminated
    
Amazon S3 - Storage lens 
    

# COMMAND ----------

EC2 instance Storage
Amazon EBS (Elastic Block Storage)
    network drive
    can be attached and dettached from EC2 instance
    intances to persist the data event after the termination of the instance
    Bound to specific AZ -Zone

    EBS - Volumes --  Network drive (Not physical)
    They can be detach and attach to another intance with in specific AZ 
    Provisioned capacity

    An EBS can not be attched to two ec2 instances
    But, 2 EBS can be attached to single ec2 instance

    If we want in another AZ, need to create seperately
    Toggle between delete on termination of ec2 instances

Amazon EBS Elastic Volumes
    Dont have to detach volume to change it
    Increase Volume
    Change Volume Type
    Adjust Performance
    

# COMMAND ----------

Amazon  EFS - Elastic File System
    Managed NFS (Network File System) that can be mounted on many ec2 instances
    EFS can work with multiple instances 
    Copatible with Linux based AMI
    Encryption at rest using KMS

Performance & Storage Classes


# COMMAND ----------

AWS Backup
    Centrally manage and automate backups across AWS services
    AWS Backup Vault Lock
    

# COMMAND ----------

DynamoDB
Amazon RDS
    Amazon Aurora -- MySQL, PostgreSQL compatible -- 5x than MySQL, 3x than PostgreSQL
    MySQL
    PostgreSQL
    MariaDB
    Oracle
    SQL Server

    ACID - Atomicity, Consistancy, Isolation, Durability
    LOCK Commands
        Shared lock
        Exclusive lock
    
    Amazon RDS Best Practices
        



    

# COMMAND ----------

Document DB --- Same as MongoDB
Similar deployments as Aurora

# COMMAND ----------

Amazon MwemoryDB for Redis
Redis -- durable and in-memory database
More suitable for microservices applications

# COMMAND ----------

Amazon Keyspaces for Cassandra
Apache Cassandra --- open source NoSQL database
Uses CQL(Cassandra Query Language)

# COMMAND ----------

Amazon Neptune  
    Fully Managed Graph database
Query Languages
    Gremlin, openCypher, SPARQL

# COMMAND ----------

Amazon Timestream
1000 times faster & 1/10th cost of RDMS for time series data
Amazon Timestream Architecture

# COMMAND ----------

Amazon Redshift
    Fully managed, petabyte-scale dataware house
    Designed for OLAP not OLTP
Redshift use-cases
Redshift Architecture
    One Cluster --> One Leader node---> Many compute nodes --> Many node slices
Redshift Spectrum
Redshift performance
    MPP
    Columnar Data Storage
    Column Compression
Redshift Durabilty
Scaling Redshift
Redshift Distribution Styles
    AUTO
    EVEN
    KEY
    ALL
Redshift DataFlows and COPY command
    COPY command
    UNLOAD command
    Enhanced VPC routing
    Auto-copy from s3
    Aurora Zero ETL 
Redshift copy grants for cross-region snapshot copies
DBLINK
Redshift integration with other services
    S3, DynamoDB, EMR/EC2, Data Pipeline, DMS
Redshift WLM
    Automatic WLM

Resizing Redshift Cluster
    Elastic Resize
    Classic Resize
    Snapshot, restore, resize

Newer Redshift Features
    RA3 modes with managed storage
    Redshift datalake export
    Spatial data types
    Cross- region data sharing

Amazon Redshift ML
Reshift Security
Redshift Serverless
    Scaling 
    Only with in VPC
    Monitoring
        Views
        Cloudwatch logs
        Cloudwatch metrics
Redshift Materialized views --- precomputed results
Redshift Datasharing --
    Standard
    Data Exchange
    Data Lake Formation
Redshift Lambda UDF
Redshift Federated Queries
Redshift System tables and Views
Redshift Data API



    


# COMMAND ----------

AWS Glue
    Glue, Hive, ETL
    ETL Transformations
    Modifying the Data Catalog


# COMMAND ----------

Migration & transfer
AWS Application Discovery Service
    Agentless Discovery
    Agent-based Discovery

AWS Application Migration Service  MGN
AWS Data Migration Service DMS
    Required EC2
    Supports - Homogenious, Heterogenious, CDC

    AWS Schema Conversion Tool (SCT) (Ex: Oracle --> MySQL)
        source ----> DMS+SCT ----> Target DB
Hands on --- Create RDS MySQL ---> Create Oracle --> Migrate (use SCT)




# COMMAND ----------

AWS DataSync
Move large amount of data to and from
    AWS Snowcone
    Preserve metadata and file permissions

AWS Snowball ---> (Data Migrations and Edge computing)
    Helps migrate petabytes of Data




# COMMAND ----------

AWS Transfer Family
    FTP
    FTPS
    SFTP

EC2 in Bigdata
AWS Graviton


# COMMAND ----------

AWS SAM - Serverless Application Model
SAM Accelerate (SAM Sync)


# COMMAND ----------

AWS Glue
    Fully Managed ETL
    Glue Crawler/ Data Catalog
        Glue crawlers extracts partitions of the data how you organized
        It's good to think upfront how you will be querying the data before you oraganize the data

Hive
    you can write SQL like queries to access EMR Cluster

Glue ETL
    Automatic code generation
    Scala or Python
    Can be event driven
    DynamicFrame --- Collection of Dynamic records
    Glue ETL Transformations
        Bundled Transformations
            DropFileds, DropNullFields
            Filter
            Join
            Map
        ML Transformations
            FindMatches ML
        Glue ETL ResolveChoice
            make_cols
            cast
            make_struct
            project

Running Glue Jobs    
    Time based
    Job bookmarks
    Cloudwatch events
Glue Supports Serverless ETL Streaming

AWS GLue Data Quality
AWS Glue Data Brew
Handling personally identifiable information with Databrew
AWS Glue Workflows
    Glue Workflow triggers
    

# COMMAND ----------

AWS Lake Formation -- Anything Glue can do AWS Lakeformation can do
AWS Lake Formation Data Filters
    Row, Column, cell level filter
    

# COMMAND ----------

Amazon Athena
    Interactive query service for s3
    Presto under the hood
    Serverless
    Supports many file formats

    Athena Workgroups
        Specific access control for individual workgroups
    Athena Security
    Athens anti-patterns
        Doesn't work for highly formatted reports
        Doesn't work for Complex ETL
    
    Athena Optimizing Performance
        Columnar format storage
        small number of large files performs better
        Use partitions

    Athena ACID Transactions
        Powered by Apache Iceberg


# COMMAND ----------

Iceberg
Apache Spark
Spark Components
    Spark Core
    Spark Streaming
    Spark SQL
    Spark ML
    GraphX
    

# COMMAND ----------

Spark Integration with Athena
Athena Federated Queries


# COMMAND ----------

EMR - Elastic MapReduce
EMR Cluster
    Master Node
    Core Node
    Task Node
EMR Usage
    Transient Cluster
    Long Running Clusters

EMR, AWS Integration and Storage
    Storage
        HDFS
        EMRFS

EMR Charges by hour
EMR Managed Scaling
EMR Serverless
EMR Serverless Application Life cycle
EMR Serverless Security
EMR on EKS -- on Elastic Kubernetes service, Fully Managed, share resources between spark and other apps on kubernetes
    

# COMMAND ----------

Amazon Kinesis Data Streams
Kinesis Data Steams - Capcity Modes
    Provisioned Mode
    On-demanad Mode
Security
Kinesis producers
    Kinesis SDK - PutRecord, PutRecords
    Kinesis Producer Library
    Kinesis Agent
    3rd Party libraries
Kenisis API Exceptions
    ProvisionedThroughputExceeded Exceptions
    Solution- Retries backoff
    Increase shards

Kinesis Producer Library
Kinesis Consumers
    SDK
    Kinesis Client Library
    Kinesis Connector Library
    


# COMMAND ----------

Kinesis Operations
    Shard splitting
    
Managed Service for Apache Flink
Apache Flink Capabilities
Kinesis Analytics
    Schema Discovery
    RANDOM_CUT_FOREST
    

# COMMAND ----------

Amazon Managed Streaming for Apache Kafka (MSK):
    Architecture
    MSK Security
        Encryption
        Network Security
        Authentication & Autherization
    MSK Monitoring
    MSK Connect
    MSK Serverless

Amazon Kenisis Vs Amazon MSK


# COMMAND ----------

Amazon OpenSerach Service (Formarely Elastic Search)
    Kibana - Visualization tool
    Search Engine
    Opensearch Applications
        Full-text search
        Log Analytics
        application monitoring
        security analytics
        clickstream analytics
        opensearch concepts
            documents
            types
            indices

Amazon OpenSearch Serive (Managed)
    Fully-Managed (But not serverless)
        There is seperate serverless option

    Amazon Opensearch options
    Amazon Opensearch Security
        decide for VPC or public upfront

Opensearch index management and designing for stability
    Cold/Warm/hot
    Index state management
    Cross cluster replication
Openseacrch stability
Amazon Opensearch Serverless


# COMMAND ----------

Amazon QuickSight
    SPICE
    Quicksight ML Insights
        ML-Powered anaomoly detection
        ML-Powered Forecasting
        Autonarratives
        Suggestive Isights
    Qucksight Calculated Fields
        newfields based on other fields
        mathematical and logical operators
        conditional functions
        date functions
        Numeric and math functions
        table calculation functions
        Aggregation functions
            Level-Aware calculations
                LAC-A
                LAC-W
            Float vs Fixed datatypes
            
            

# COMMAND ----------

Application Integration
    Amazon SQS
        AWS SQS -  Standard Queue
        SQS - Producing Messages
        SQS - Consuming Messages
        SQS Extended Client
        SQS Usecases
            Decouple applications
            Buffer writes to a database
        SQS Limits
        SQS Security


        SQS Vs Kinesis Data stream
        SQS Dead Letter Queue


# COMMAND ----------

Amazon SNS
    Security

    SNS+SQS Fan Out
    S3 Events to multiple Queues
    SNS to Amazon S3 through Kinesis Data Firehose
    SNS FIFO
    SNS FIFO + SQS FIFO: Fan Out
    SNS - Messaging Filtering


# COMMAND ----------

AWS Step Functions
    State Machines and States
    

# COMMAND ----------

Amazon AppFlow
 SaaS

# COMMAND ----------

Amazon EventBridge
    Rules


# COMMAND ----------

MWAA (Managed workflows for Apache Airflow)
    DAGs are uploaded to s3
    Pick it up from S3, Orchastrates and schedule the pipeline defined by each DAG
    Runs with in VPC (at least 2 Az's)
    Private or public endpoints
    Automatic scaling
Amazon MWAA Integration
    


# COMMAND ----------

Full Data Engineering Pipelines
    Real Time Layer
    Video layer
    Batch Layer
    Analytics Layer
    

# COMMAND ----------

Security, Identity and Compliances
    Principle of Least Privilege
    Data Masking and Anonymization
    Key Salting

    IAM Section
        IAM Permissions
        

# COMMAND ----------

Amazon Macie

# COMMAND ----------

AWS Shield
    Service that protects from DDoS attacks -- Many requests at same time
    AWS Shield Standard
    AWS Shield Advanced
        


# COMMAND ----------

Security - Kinesis
    Data streams
    SSL endpoints -- HTTPS
    server side
    no client side -- use encryption lib

Security -SQS
    HTTPS
    Ser ver side KMS
    IAM
    SQS queue access

    Client side -manually
    VPC

Security - IOT
    IOT policies
    IAM policies

Security - Amazon S3
    IAM
    S3 bucket policies
    ACL
    Encryption in flight, rest
    Versioning
    CORS
    VPC
    Glacier

Secuirity -Dynamo DB
    HTTPS

RDS
    VPC
    security groups
    KMS
    SSL
    IAM





# COMMAND ----------


