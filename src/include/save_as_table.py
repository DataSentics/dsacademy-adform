# Databricks notebook source
# MAGIC %md
# MAGIC This notebook helps to quickly save tables in any location.

# COMMAND ----------

# If save_path is None, it means the user wants to save the table in hive metastore and not a physical copy
def save_as_table(df,table_name, save_path=None, checkpoint_location=None, save_format="delta"):
    # Save to ABFSS IF path & checkpoint is specified
    if(save_path != None and checkpoint_location != None):
        (
            df
            .writeStream
            .format(save_format)
            .option("checkpointLocation", checkpoint_location)
            .option("path", save_path)
            .option("mergeSchema", "true")
            .trigger(availableNow=True)
            .outputMode("append")
            .table(table_name)
        )
        print(f"Table '{table_name}' successfully saved at '{save_path}'")
    # Error Handle if user wants to save to ABFSS and does not specify a checkpoint_location
    elif(save_path != None and checkpoint_location == None):
        raise Exception("Checkpoint Location not provided!")
    # Save to hive metastore if above choices do not apply
    else:
        (
        df.write.option("mergeSchema", "True").mode("overwrite").saveAsTable(table_name)
        )
        print(f"Table {table_name} saved in Hive Metastore")
