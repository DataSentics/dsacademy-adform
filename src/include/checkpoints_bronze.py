# Databricks notebook source
# Bronze Table Checkpoint Paths

# COMMAND ----------

# User DBFS path
user_dbfs_path = '/dbfs/user/fabian-augustin-ilie.radomir@datasentics.com/dbacademy/Adform'

# COMMAND ----------

bronze_click_checkpoint = f"{user_dbfs_path}/bronze/bronze_click_checkpoint"
bronze_click_checkpoint_write = f"{user_dbfs_path}/bronze/bronze_click_checkpoint_write"
bronze_impression_checkpoint = f"{user_dbfs_path}/bronze/bronze_impression_checkpoint"
bronze_impression_checkpoint_write = f"{user_dbfs_path}/bronze/bronze_impression_checkpoint_write"
