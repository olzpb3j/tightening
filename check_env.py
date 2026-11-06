# spark is pre-configured when this runs on a Databricks cluster — no setup needed.
 
df = spark.sql("select * from SNOWFLAKE_DB_TL_MFG_S.TL_MFG.ENT_IIOT_ATLASCO_PCO")
 
print(f"Row count: {df.count()}")
df.show(5)
