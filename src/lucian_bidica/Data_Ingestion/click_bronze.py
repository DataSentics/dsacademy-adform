# Databricks notebook source
# MAGIC %run ./initial_notebook

# COMMAND ----------

click_raw = auto_loader(click_source_path, click_checkpoint_path)

# COMMAND ----------

display(click_raw)

# COMMAND ----------

(click_raw.writeStream
.format("delta")
.option("checkpointLocation", click_checkpoint_path)
.option("path", click_parsed_path)
.outputMode("append")
.table("click_bronze"))

# COMMAND ----------

display(spark.sql("show tables"))
