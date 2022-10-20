# Databricks notebook source
# SET USER
user = "radomirfabian"

# COMMAND ----------

# STORAGE LOCATION VARIABLES
user_storage_root = 'abfss://{}@adapeuacadlakeg2dev.dfs.core.windows.net'.format(f"{user}")
user_working_dir = f'{user_storage_root}/Adform'
user_dbfs_path = '/dbfs/user/fabian-augustin-ilie.radomir@datasentics.com/dbacademy/Adform'

data_storage_root = 'abfss://{}@adapeuacadlakeg2dev.dfs.core.windows.net'.format("01rawdata")
rawdata_location = f'{data_storage_root}/Adform'

click_data_location = f'{rawdata_location}/Click/Increment/'
impression_data_location = f'{rawdata_location}/Impression/Increment/'

parsedata_storage_root = f'{data_storage_root}/02parsedata/RF_Adform'

# COMMAND ----------

# SILVER TABLE LOCATION VARIABLES
silver_click_data = f'{parsedata_storage_root}/silver/Click'
silver_impression_data = f'{parsedata_storage_root}/silver/Impression'

# COMMAND ----------

# VERIFY PATH CORRECTNESS
# dbutils.fs.ls(rawdata_location)
# dbutils.fs.ls(click_data_location)
# dbutils.fs.ls(impression_data_location)

# COMMAND ----------

# CREATE AND SET WORKING DATABASE

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS radomirfabian_adform

# COMMAND ----------

# MAGIC %sql
# MAGIC USE radomirfabian_adform
