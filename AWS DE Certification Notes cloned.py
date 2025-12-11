# Databricks notebook source
Types of Data
Properties of Data data

Data Warehouse - Centralized repository which is optimized for analytics
Data Lakes - Storage repository holds large datasets in it's own format
Data Lakehouse - Architecture of combination of both data warehouse and datalake
Data Mesh - Individual group data management and governance
ETL Pipeline
    Data Cleansing
    Data enrichment
    Format Changes
    Aggregations and Computations
    Encoding and decoding data
    Handling missing values

Managing ETL Pipelines



# COMMAND ----------

Data Sources
    JDBC
    ODBC
    Raw Logs
    API's
    Streams

    CSV
    JSON
    AVRO
    PARQUET

# COMMAND ----------

Data Lineage
Schema Evolution
Database performance optimization
Data Sampling Techniques
Data Skew mechanism
Addressing Data Skew


# COMMAND ----------

Data Validation and Profiling
    Completeness
    Consistency
    Accuracy
    Integrity
    

# COMMAND ----------

S3- Buckets
S3- Objects
S3- Security
    User-based
    Resourse-based
    Encryption
S3 Bukcet Policies
    JSON based
    S3 Bucket policies
S3 Versioning
S3 Replication CRR & SRR
S3 Storage Classes
S3 Durability & Availability

# COMMAND ----------

Storage Serivices
    S3 
    EFS
    EBS
    AWS Backup



# COMMAND ----------

Amazon EMR
    Key Features:
        Managed Bigdata frameworks - Apache Hadoop,Apache Spark, Hive, Hbase and others
        Scalable Infrastructure - resize clusters
        Cost Efficiency - pay only for use, graviton based instances
        Integrated with AWS Ecosystem
    
    Cluster Architecture:
        Master Node - distribution of tasks and data, task assignment, failure recovery, cluster health management
        Core Nodes - storage and computation processing the data
        Task Nodes - scaling compution when workloads demand additional resources, do not store data
    
    Storage Options:
        HDFS
        EMRFS
        Local File Systems - local disk attached to EC2 instances (ephemeral storage)
    External Metastores:
        By default, Hive stores its metastore information in a MySQL database located on the primary node’s file system.
        AWS Glue Data Catalog
        Amazon RDS or Amazon Aurora

        Run MSCK REPAIR TABLE to synchronize the metadata with actual data layout in the file system if using HDFS or s3

    Cluster Types: Transient vs Long-Running:
        Transient - temporory clusters. Terminates once the job execution is completed, cost efficient
        Long-Running Clusters: Stays active all the times
    
    Amazon EC2 Graviton
    Spark Memory Overhead
    Amazon EMR Serverless




# COMMAND ----------

AWS Glue
    Key Features:
        Connectivity
        Automated ETL Script Generation
        Customizable ETL code
        Scalability
        Scheduling
        DynamicFrames
        Job Bookmarks
        Data Quality

    Resources:
        DPU - combination of CPU, memory and network capacity (1 DPU = 4 CPUs & 16 GB)
        Determine appropriate DPU capacity by using Job run monitoring

    Streaming Data
        AWS Glue supports streaming ETL jobs - integrating with streaming data sources such as Kinesis, Kafka, MSK
    
    Security and Data Protection:
        Encryption at rest and in-transit
        Uses KMS 
        Can be deployed in VPC
        Secure management of credentials in SecretManager and Access them from Glue

    AWS Glue Crawlers
    AWS Glue Workflows
    Schema management with AWS Glue schema registry
    AWS Glue for Ray and Interactive Sessions - 
    ResolveChoice - Manage ambiguous or incosistent datatypes
    AWS Glue FindMatches ML Transform
    Glue Python shell jobs - light to medium data transformations
    Sensitive Data Detection
    GIT Integration

    Best Practices & Optimization
        Optimize data partitioning - Supports partition projection
        Effiecient data transformation & Filtering - Server-side filtering with partition predicates 
        Monitoring & performance Optimization
        Broadcast Joins
        Partition Indexes
    
    AWS Glue DataBrew
        Data Preparation tool
        Key Features:
            Code-Free Data Preparation
            Data Profiling
            Custom Data Quality Rules
            Masking and Anonymizing PII
             








# COMMAND ----------

Amazon Redshift
    Fully Managed Petabyte scale cloud data warehouse
    Redshift is optimized for OLAP
    Consists of cluster of computing resources called Nodes

    Node and Cluster Architecture:
        Leader Node
        Compute Nodes
        Slices
    
    Data Distribution and Storage
        Distribution Keys
        Storage Decoupling

    Data Loading and Performance
        Parallel Processing
        Compression

    Federated Queries
    Redshift Spectrum
    Data Sharing
    Redshift Serverless

    Performance Insights
        Query performance insights
        Amazon Redshift Advisor

    System Tables and View
        SVV - 
        SYS
        STL
        STV
        SVCS
        SVL



