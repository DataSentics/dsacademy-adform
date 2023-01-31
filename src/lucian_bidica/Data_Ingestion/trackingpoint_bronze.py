# Databricks notebook source
# MAGIC %run ./initial_notebook

# COMMAND ----------

trackingpoint_raw = auto_loader(trackingpoint_source_path, trackingpoint_checkpoint_path)

# COMMAND ----------

display(trackingpoint_raw)

# COMMAND ----------

(trackingpoint_raw.writeStream
.format("delta")
.option("checkpointLocation", trackingpoint_checkpoint_path)
.option("path", trackingpoint_parsed_path)
.outputMode("append")
.table("trackingpoint_bronze"))

# COMMAND ----------

display(spark.sql("show tables"))
