# Databricks notebook source
# Silver Checkpoint Locations
silver_click_checkpoint = f"{user_dbfs_path}/silver/silver_click_checkpoint"
silver_click_checkpoint_write = f"{user_dbfs_path}/silver/silver_click_checkpoint_write"
silver_impression_checkpoint = f"{user_dbfs_path}/silver/silver_impression_checkpoint"
silver_impression_checkpoint_write = f"{user_dbfs_path}/silver/silver_impression_checkpoint_write"

# COMMAND ----------

# Silver Export Locations
silver_click_data = f'{path_02parseddata}/silver/Click'
silver_impression_data = f'{path_02parseddata}/silver/Impression'
