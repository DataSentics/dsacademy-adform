# Databricks notebook source
# Autoload data from 01rawdata/Impression
bronze_impression_ingested_data = autoloader(impression_data_location, bronze_impression_checkpoint, "csv")

# COMMAND ----------

# Write Bronze Impression Table to ABFSS in 02parsedata/RF_Adfrom/bronze/impression

(
    bronze_impression_ingested_data
    .writeStream
    .format("delta")
    .option("checkpointLocation", bronze_impression_checkpoint_write)
    .option("path", bronze_impression_data)
    .option("mergeSchema", "true")
    .trigger(availableNow=True)
    .outputMode("append")
    .table("bronze_impression_table")
)
