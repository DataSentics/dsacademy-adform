# Databricks notebook source
# MAGIC %run ./variables

# COMMAND ----------

list_checkpoints = [
    "daniela_click_raw_checkpoint/",
    "daniela_impression_raw_checkpoint/"
]

# COMMAND ----------

for checkpoint in list_checkpoints:
    dbutils.fs.rm(
        f"{working_dir}{checkpoint}",
        True
    )
