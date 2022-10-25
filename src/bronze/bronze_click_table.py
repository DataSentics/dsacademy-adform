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

save_as_table(bronze_click_ingested_data, "bronze_click_table", bronze_click_data, bronze_click_checkpoint_write)

# COMMAND ----------


