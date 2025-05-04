from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("FraudDetectionETL").getOrCreate()

# Load all raw JSON files
df = spark.read.json("s3://fraud-detection-buckets/raw-transactions/")

# Clean and transform
df = df.select(
    col("transaction_id").cast("string"),
    col("user_id").cast("int"),
    col("amount").cast("double"),
    col("location").cast("string"),
    col("transaction_type").cast("string"),
    col("fraud_probability").cast("double")
).dropna().dropDuplicates()

# Write as CSV with header
df.coalesce(1).write.mode("overwrite").option("header", True).csv("s3://fraud-detection-buckets/transformed/")