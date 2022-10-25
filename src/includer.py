# Databricks notebook source
# This will be the driver notebook to load all the required include files

# COMMAND ----------

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

# CORE INCLUDE

# COMMAND ----------

# MAGIC %run ./include/autoloader

# COMMAND ----------

# MAGIC %run ./include/save_as_table

# COMMAND ----------

# BRONZE CHECKPOINT INCLUDES

# COMMAND ----------

# MAGIC %run ./include/checkpoints/checkpoints_bronze

# COMMAND ----------

# SILVER CHECKPOINT INCLUDES

# COMMAND ----------

# MAGIC %run ./include/checkpoints/checkpoints_silver
