# Databricks notebook source
Features
    Columnar storage
    Massively Parallel Processing (MPP)

Architecture
    Leader Node ---> Compute nodes ----> node slices
    One Leader node --- manages the client connections and SQL query planning
    Multiple Compute nodes --- Stores data and execute queries
    Node slices --- Each computer node has node slices, each node slice process portion of workload

Distribution styles of Redshift:
    Key Distribution --- distribute the data based on values of the column
    Even Distribution --- distribute the data evenly across node slices
    All Distribution  --- copies entire table to every node (usefull for small lookup tables)

SortKeys in Redshift
    Compound sortkeys  --- Order data by first key and then by second key
    Interleaved sortkeys --- Spread the sorting evenly across all keys

Columnar storage
    significantly reduces the amount of I/O reuired for queries that accesses subset of columns
    better compression and performance
    reduces the storage costs
    
Compression and encoding types:
    redshift uses the compression to reduce storage costs and improve I/O performance
    Different ecncoding types:
        LZO -- General purpose compression
        RUNLENGTH - Best for columns with repeated values
        BYTEDICT -- Best for columns with small number of unique columns
        DELTA -- Best for columns with increasing or decreasing values

VACUUM Command:
    reclaims storage space and re-sorts the rows in a table to maintain query performance
    useful after large DELETE or UPDATE operations

ANALYZE command:
    ANALYZE command updates the table statistics used by query optimizer to generate efficient query plans
    Regularly running ANALYZE ensures the optimizer has accurate information

Optimize the Redshift cluster:
    Use appropriate distrbution and sort keys
    Regularly running VACCUM and ANALYZE commands
    Monitoring and tuning the WLM settings
    Scaling the cluster by adding nodes or using concurrency scaling

Process of loading data into redshift. Common methods and best practices
    Data can be loaded using COPY command, which supports various file formats (CSV, AVRO, JSON ect)
    Best practices:
        using compression for input files
        splitting large files into smaller chunks
        Loading from S3 and DynamoDB for better performance
    
Considerations for data unloading in Redshift
    data can unloaded uisng UNLOAD command
    exports data to s3 in text or parquet format
    Considerations:
        chossing the right format for downstream processing
        using parallelism to speed up the process
        ensuring data security during transfer

Concurrency and Workload management
    They handled using WLM queues. 
    Each queue can have different memory and concurrency settings
    Users can be assigned to specific queues based on their workload needs

Security features availble in redshift
    Encryption at rest and in transit
    IAM roles
    VPC
    Auditing: Logging user activity and API calls with CloudTrail

Amazon Redshift Spectrum
    Spectrum allows to query the data which is in s3 without having to load into the redshift tables
    Enables seamless querying across data stored in redshift tables and S3

Common Challenges:
    Query performance issues: Optimize with proper keys, use VACUUM, ANALYZE and WLM Settings
    Data loading bottlenecks: Parallel loading, Compression, Even distribution
    Storage Management: Regularely monitor and reclaim storage with VACUUM

Monitor and Troubleshoot Redshift cluster
    Cloudwatch: For monitoring metrics and setting alarms
    System tables and Views: To analyze query performance and disk usage 
    AWS Management Console: For cluster management and insights

Difference between Redshift and RDS
    Redshift: Data warehouse -- Optimized for OLAP (Large-scale data analytics)
    RDS: Data storage and designed for OLTP

Backup and restore operations:
    Redshift automatically takes snapshot of the cluster at regular intervals and allow manual snapshots
    We can restore the cluster with the snapshots incase of data loss or corruption

Schema Migration in Redshift:
    can be done using tools like AWS Schema Conversion Tool (SCT)
    Best practices:
            Testing the migration in staging environment
            minimize the downtime using the incremental data transfer methods
            validating the data integrity post-migration
        
Managing Redshift cost
    Using reserved instances to save long term costs
    right sized clusters based on workload requirements
    unlading infrequently accessed data to s3 and using redshift spectrum for queries
    regularely monitoring the usage and setting the budget alerts






# COMMAND ----------

Design dataware house using Amazon Redshift
    Identifying the datasources - Data load to Redshift using COPY command or third-party ETL tools
    Data Warehouse architecture - Determine the number of nodes and storage configuration
    Data Warehouse design - Designing data mode, schema and queries 

Strategies to optimize the query performance in redshift
    Ensure the data is properly distributed across the cluster nodes, done by COPY command and setting the distribution key when creating tables
    Using right sort keys when creating the tables
    Using the right datatypes when creating the tables
    Using the right compression techniques
    EXPAIN command to analyze query plans, VACUUM for reclaim disk space, ANALYZE for update statistics

Data loading and unloading
Amazon Redshift security and encryption
Monitor and troubleshoot Amazon redshift performance issues:
        Understand the query workload and data distribution:
            This can be done by running the system tables STV_BLOCKLIST and STV_PARTITIONS to identify any skews in the data distribution
            Monitor system performance metrics in cloudwatch which provide CPU utilization, Disk I/O and Network I/O
            SVV_SYSSTAT and SVV_QUERY_REPORT system tables provides info on long running queries
            EXPLAIN command to identify potential issues with query plan, Query can be optimized by using the appropriate sort and distribution keys
            SVV_DISKUSAGE - to monitor disk usage
            SVV_REFRESH_SUMMARY can be used to identify any tables not being refreshed regularly

Optimize data storage in Redshift
    using appropriate datatypes
    use right sort and distribution keys
    compression
    right table structure such as star schema or snowflake schema and right partition strategy

Data replication and Backup
    data replication and backup in redshift handled through combination of automated and manual processes
    Automated process:
        Automated snapshots
        Automated backups
    Manual process:
        Manual snapshots
        Manual Backups

Amazon redshift scalability and Elasticity
    





# COMMAND ----------

1. How does Amazon Redshift differ from traditional relational databases?
2. What are the main components of Amazon Redshift?
3. What types of data sources can you load into Amazon Redshift?
4. How does Amazon Redshift handle data compression and distribution?
4. What are some best practices for optimizing query performance in Amazon Redshift?
5. How does Amazon Redshift handle concurrency and scalability?
6. What is the difference between dense compute and dense storage node types in Amazon Redshift?
7. How does Amazon Redshift handle backups and data durability?
8. How does Amazon Redshift integrate with other AWS services?
9. What is the purpose of the VACUUM command in Amazon Redshift?
10. What are the different types of sort keys in Amazon Redshift, and when should you use them?

