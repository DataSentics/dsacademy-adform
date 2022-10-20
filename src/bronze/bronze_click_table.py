# Databricks notebook source
# DELETE THE CELLS BELOW WHEN WORKFLOW IS SET UP

# COMMAND ----------

# MAGIC %run ../includer

# COMMAND ----------

# Notebook driver to automatically all current files, format and export as usable tables

# COMMAND ----------

# Autoload data from 01rawdata/Click
bronze_click_ingested_data = autoloader(click_data_location,bronze_click_checkpoint,"csv")

# COMMAND ----------

# Write Bronze Click Table to ABFSS in 02parsedata/RF_Adform/bronze/click
(
    bronze_click_ingested_data
    .writeStream
    .format("delta")
    .option("checkpointLocation", bronze_click_checkpoint_write)
    .option("path", bronze_click_data)
    .option("mergeSchema", "true")
    .trigger(availableNow=True)
    .outputMode("append")
    .table("bronze_click_table")
)
