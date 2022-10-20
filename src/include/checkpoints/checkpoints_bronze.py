# Databricks notebook source
# Bronze Checkpoint Locations
bronze_click_checkpoint = f"{user_dbfs_path}/bronze/bronze_click_checkpoint"
bronze_click_checkpoint_write = f"{user_dbfs_path}/bronze/bronze_click_checkpoint_write"
bronze_impression_checkpoint = f"{user_dbfs_path}/bronze/bronze_impression_checkpoint"
bronze_impression_checkpoint_write = f"{user_dbfs_path}/bronze/bronze_impression_checkpoint_write"

# COMMAND ----------

# Bronze Export Locations
bronze_click_data = f'{parsedata_storage_root}/bronze/Click'
bronze_impression_data = f'{parsedata_storage_root}/bronze/Impression'
