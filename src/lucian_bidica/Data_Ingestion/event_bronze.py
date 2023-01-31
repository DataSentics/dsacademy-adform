# Databricks notebook source
# MAGIC %run ./initial_notebook

# COMMAND ----------

event_raw = auto_loader(event_source_path, event_checkpoint_path)

# COMMAND ----------

display(event_raw)

# COMMAND ----------

(event_raw.writeStream
.format("delta")
.option("checkpointLocation", event_checkpoint_path)
.option("path", event_parsed_path)
.outputMode("append")
.table("event_bronze"))

# COMMAND ----------

display(spark.sql("show tables"))
