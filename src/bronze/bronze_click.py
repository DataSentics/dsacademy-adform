# Databricks notebook source
# DELETE THE CELLS BELOW WHEN WORKFLOW IS SET UP

# COMMAND ----------

# MAGIC %run ../include/initialize

# COMMAND ----------

# MAGIC %run ../include/checkpoints_bronze

# COMMAND ----------

# Notebook driver to automatically all current files, format and export as usable tables

# COMMAND ----------

# MAGIC %run ../include/autoloader

# COMMAND ----------

ingested_data = autoloader(click_data_location,bronze_click_checkpoint,"csv")

# COMMAND ----------

display(ingested_data)

# COMMAND ----------


