# Databricks notebook source
# This will be the driver notebook to load all the required include files

# COMMAND ----------

# CORE INCLUDES

# COMMAND ----------

# MAGIC %run ./include/initialize

# COMMAND ----------

# MAGIC %run ./include/autoloader

# COMMAND ----------

# BRONZE CHECKPOINT INCLUDES

# COMMAND ----------

# MAGIC %run ./include/checkpoints/checkpoints_bronze

# COMMAND ----------

# SILVER CHECKPOINT INCLUDES

# COMMAND ----------

# MAGIC %run ./include/checkpoints/checkpoints_silver
