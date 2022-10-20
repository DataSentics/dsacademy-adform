# Databricks notebook source
# This Notebook is specifically Autoloader function and nothing else

# COMMAND ----------

def autoloader(data_source, checkpoint_directory, source_format):
    query = (
        spark
        .readStream.format("cloudFiles")
        .option("cloudFiles.format", source_format)
        .option("cloudFiles.schemaLocation", checkpoint_directory)
        .option("header", True)
        .option(availableNow=True)
        .load(data_source)
    )
    return query
