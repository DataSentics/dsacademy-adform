# Databricks notebook source
# MAGIC %run ../includer

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

# Load Bronze Click Table

bronze_click_df = (
    spark.readStream.table("bronze_click_table")
)

# COMMAND ----------

silver_click_df = (
    bronze_click_df.select(
        "yyyymmdd",
        "BatchId",
        "TransactionId",
        "Timestamp",
        "CookieID",
        "TagId",
        "PublisherDomain",
        "CampaignId",
        "PlacementId-ActivityId",
        "CookiesEnabled",
        "IsRobot",
        "IP",
        "DeviceTypeId",
        "ClientId",
        "CityId",
        "BrowserId",
        "Timestamp-Server"
    )
    .fillna("NULL")
)

# COMMAND ----------

display(silver_click_df)

# COMMAND ----------


