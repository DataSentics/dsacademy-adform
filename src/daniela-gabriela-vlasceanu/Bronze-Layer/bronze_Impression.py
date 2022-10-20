# Databricks notebook source
# MAGIC %run ../Includes/variables

# COMMAND ----------

impresion_download_path = f"{azure_storage}Adform/Impression/Increment/".format("01rawdata")

# COMMAND ----------

(
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option(
        "cloudFiles.schemaLocation",
        f"{working_dir}daniela_impression_raw_checkpoint/",
    )
    .option("encoding", "ISO-8859-1")
    .load(impresion_download_path)
    .createOrReplaceTempView("raw_impreSsion_temp")
)

# COMMAND ----------

impression_path_upload = (
    f"{azure_storage}".format("02parseddata")
    + "daniela-vlasceanu-click/bronze/impression"
)

# COMMAND ----------

spark.sql(
    "create or replace Temporary view bronze_impression_tmp as select * from raw_impression_temp"
)

# COMMAND ----------

(
    spark.table("bronze_impression_tmp")
    .writeStream
    .trigger(availableNow=True)
    .format("delta")
    .option(
        "checkpointLocation",
        f"{working_dir}daniela_impression_raw_checkpoint/",
    )
    .option("path", impression_path_upload)
    .outputMode("append")
    .partitionBy("yyyymmdd")
    .table("bronze_impression")
)
