# Databricks notebook source
# MAGIC %run ../Data_Ingestion/initial_notebook

# COMMAND ----------

df_click = spark.table("click_bronze")
df_event = spark.table("event_bronze")
df_impression = spark.table("impression_bronze")
df_trackingpoint = spark.table("trackingpoint_bronze")

# COMMAND ----------

df_merged = df_click.join(df_event, "ClientId").join(df_impression, "ClientId").join(df_trackingpoint, "ClientId")
display(df_merged)
