# ThymeDrift

Solution to assess, continuously monitor and manage data quality and data dependencies.

## Problem Statement

### Data Quality

The automated data ingestion pipelines (ETL / ELT) either batch or event-based does not produce trusted outputs due to lack of quality or insight into quality. Data consumers do not trust the data publishers or have no way of validating the source data. Investigating generated data errors is time consuming. Errors in data format or data types can result in application failure or errors in application behavior.

Poor data quality can come from multiple different places. Humans are likely to make mistakes when entering data into an application or a system, typos, missed entries or data entered into the wrong colum. Automated processes can input bad quality data or the lack of alignment across systems can result in inconsistency. When analyzing a dataset you often face the problem of missing information or data far outside of the expected range. Ingesting data from multiple different source systems may result in duplicate records. When a system is transforming data it may lead to errors.

We have classified data quality in the 6 listed categories:

* Accuracy
* Completeness
* Consistency
* Timeliness
* Uniqueness
* Validity

Each category consists of a set of features affecting data quality.

### Data dependencies

When the number of available data sets or data products in an organization grows there becomes a need to monitor and manage dependencies. When ingesting data from a source system you want to reduce the additional load on the system and avoid performance implications on the primary workload. You also want to reduce duplicates of the ingested data. These requirements lead you to reusing ingested datasets. When multiple data products consume the same data or parts of the same dataset they need to be able to map and monitor dependencies to avoid errors in downstream applications. Data products can consume data from other data products and becoming both a consumer and a producer of data, the dependencies between the data products needs to be mapped and monitored.

## Solution

A set of rules to assess data quality and monitor dependencies.
Lightweight component integrated in data pipelines and data set scanning.

### Architecture

 [Architecture doc](/docs/README.md)

## Market Gap analysis

### Microsoft

Today there are no product feature available to address the challenges outlined in the problem statement. Current tools for data monitoring and cataloging is Purview, this service does not have any of the capabilities described and there are no known plans to develop this. The current tools for data ingest and data pipelines are Azure Data Factory and Logic Aps, neither have features for tracking dependencies or data quality.

Customers are asking for this. As their data estates grows and they are adopting patterns for distributed data environments, enabling teams to be self serviced and increase automation, it increases the need for continuous monitoring and maintenance of data quality and data dependencies.

### 3rd party tools

| DQ Tool | Key Features | Value to the users
|:---------------------------|:------------|:----------------|
| Informatica Quality Data MDM solutions|Data Standardization, deduplication, validation, consolidation, and robust MDM solution.|MDM supports structured and unstructured data. AI features enabled.
|SAS Data Management | Data Integration and Cleansing. Uses Data governance and metadata management disciplines of DQ management | Unstructured data. AI features Graphical interfaces and powerful wizard for effective data management
Experian Aperture Data Studio|Data discovery and profiling, Data monitoring, Data cleansing. Works with any type of data. |Easy to use DQ management tool. Workflow designer enables easy data quality monitoring.
IBM InfoSphere Quality Stage |Data cleansing and Data management. Data profiling helps deep analysis of data. |Machine learning-enabled delivers high data accuracy.
Cloudingo |Data integrity and cleansing. Removes duplicates and human errors. |Used extensively in Salesforce. It has a drag and drop interface.
Talend Data Quality |Data Standardization, Deduplication, Validation. |Uses ML features to maintain clean data.
Data ladder | Data Cleansing. Uses data matching, deduplication techniques for cleansing. Very high data accuracy. Manages multiple databases, big data.
SAP Data Services |Data integration, transformation and Master data Management. Uses text analysis, auditing, and data profiling techniques. |Handles data from multiple sources and provide a reliable data for analytics.
OpenRefine |Data Cleansing including big data. |Open-source tool. Supports multiple languages.|
