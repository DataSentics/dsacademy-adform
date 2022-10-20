# Databricks notebook source
# USER VARIABLES
user = "radomirfabian"
print(user)

# COMMAND ----------

# STORAGE VARIABLES
user_storage_root = 'abfss://{}@adapeuacadlakeg2dev.dfs.core.windows.net'.format(f"{user}")
user_working_dir = f'{user_storage_root}/Adform'

data_storage_root = 'abfss://{}@adapeuacadlakeg2dev.dfs.core.windows.net'.format("01rawdata")
rawdata_location = f'{data_storage_root}/Adform'

click_data_location = f'{rawdata_location}/Click/Increment/'
impression_data_location = f'{rawdata_location}/Impression/Increment/'

# COMMAND ----------

# VERIFY PATH CORRECTNESS
# dbutils.fs.ls(rawdata_location)
# dbutils.fs.ls(click_data_location)
# dbutils.fs.ls(impression_data_location)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS radomirfabian_adform

# COMMAND ----------

# MAGIC %sql
# MAGIC USE radomirfabian_adform
