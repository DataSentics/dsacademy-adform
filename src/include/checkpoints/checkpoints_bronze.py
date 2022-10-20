# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS radomirfabian_adform

# COMMAND ----------

# MAGIC %sql
# MAGIC USE radomirfabian_adform

# COMMAND ----------

# Static Path Variables
user_dbfs_path = '/dbfs/user/fabian-augustin-ilie.radomir@datasentics.com/dbacademy/Adform' # Databricks File System Path
path_01rawdata = 'abfss://{}@adapeuacadlakeg2dev.dfs.core.windows.net/Adform'.format("01rawdata") # abfss://.../01rawdata
path_02parseddata = 'abfss://{}@adapeuacadlakeg2dev.dfs.core.windows.net/RF-Adform'.format("02parseddata") # abfss://.../02parseddata/RF-Adform



# COMMAND ----------

# Static Data Paths
click_data_location = f'{path_01rawdata}/Click/Increment/' # 01rawdata/Click/Increment
impression_data_location = f'{path_01rawdata}/Impression/Increment/' # 01rawdata/Click/Increment

# COMMAND ----------

# Bronze Checkpoint Locations
bronze_click_checkpoint = f"{user_dbfs_path}/bronze/bronze_click_checkpoint"
bronze_click_checkpoint_write = f"{user_dbfs_path}/bronze/bronze_click_checkpoint_write"
bronze_impression_checkpoint = f"{user_dbfs_path}/bronze/bronze_impression_checkpoint"
bronze_impression_checkpoint_write = f"{user_dbfs_path}/bronze/bronze_impression_checkpoint_write"

# COMMAND ----------

# Bronze Export Locations
bronze_click_data = f'{path_02parseddata}/bronze/Click'
bronze_impression_data = f'{path_02parseddata}/bronze/Impression'
