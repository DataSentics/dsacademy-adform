# Databricks notebook source
# MAGIC %run ../Includes/variables

# COMMAND ----------

click_download_path = f"{azure_storage}Adform/Click/Increment/".format("01rawdata")

# COMMAND ----------

(
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option(
        "cloudFiles.schemaLocation",
        f"{working_dir}daniela_click_raw_checkpoint/",
    )
    .option("encoding", "ISO-8859-1")
    .load(click_download_path)
    .createOrReplaceTempView("click_raw_temp")
)

# COMMAND ----------

click_path_upload = (
    f"{azure_storage}".format("02parseddata")
    + "daniela-vlasceanu-click/bronze/click"
)

# COMMAND ----------

spark.sql(
    "create or replace Temporary view bronze_click_tmp as select * from click_raw_temp"
)

# COMMAND ----------

(
    spark.table("bronze_click_tmp")
    .writeStream
    .trigger(availableNow=True)
    .format("delta")
    .option(
        "checkpointLocation",
        f"{working_dir}daniela_click_raw_checkpoint/",
    )
    .option("path", click_path_upload)
    .outputMode("append")
    .partitionBy("yyyymmdd")
    .table("bronze_click")
)
