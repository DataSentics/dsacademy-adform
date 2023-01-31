# Databricks notebook source
# MAGIC %run ./initial_notebook

# COMMAND ----------

impression_raw = auto_loader(impression_source_path, impression_checkpoint_path)

# COMMAND ----------

display(impression_raw)

# COMMAND ----------

(impression_raw.writeStream
.format("delta")
.option("checkpointLocation", impression_checkpoint_path)
.option("path", impression_parsed_path)
.outputMode("append")
.table("impression_bronze"))

# COMMAND ----------

display(spark.sql("show tables"))
