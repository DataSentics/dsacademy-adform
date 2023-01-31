# Databricks notebook source
# creating a database and using it for the exercise:

spark.sql("create database if not exists lucian_bidica_adform")
spark.sql("use lucian_bidica_adform")

# COMMAND ----------

# the core source paths for the ingestion, parsed data, and checkpoints:

source_path = "abfss://01rawdata@adapeuacadlakeg2dev.dfs.core.windows.net/Adform"

parsed_path = "abfss://02parseddata@adapeuacadlakeg2dev.dfs.core.windows.net/lucian_bidica_adform"

checkpoint_path = "abfss://01rawdata@adapeuacadlakeg2dev.dfs.core.windows.net/lucian-bidica/adform_checkpoints"

# COMMAND ----------

# the source paths for the data in each table:

click_source_path = f"{source_path}/Click/Increment"
event_source_path = f"{source_path}/Event/Increment"
impression_source_path = f"{source_path}/Impression/Increment"
trackingpoint_source_path = f"{source_path}/Trackingpoint/Increment"

# COMMAND ----------

# the paths for pased data:

click_parsed_path = f"{parsed_path}/click_bronze"
event_parsed_path = f"{parsed_path}/event_bronze"
impression_parsed_path = f"{parsed_path}/impression_bronze"
trackingpoint_parsed_path = f"{parsed_path}/trackingpoint_bronze"

# COMMAND ----------

# the paths for checkpoints used for data ingestion:

click_checkpoint_path = f"{checkpoint_path}/click_checkpoint"
event_checkpoint_path = f"{checkpoint_path}/event_checkpoint"
impression_checkpoint_path = f"{checkpoint_path}/impression_checkpoint"
trackingpoint_checkpoint_path = f"{checkpoint_path}/trackingpoint_checkpoint"

# COMMAND ----------

# ingestion function (auto_loader)

def auto_loader(data_source, checkpoint_path):
    query = (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("cloudFiles.schemaLocation", checkpoint_path)
        .option("header", True)
        .load(data_source)
    )
    return query
