from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext

sc = SparkContext('yarn-cluster')
hc = HiveContext(sc)
parquetFile = hc.parquetFile("/czdataset/weather/weather_data/000000_0")
parquetFile.registerTempTable("weatherStation")
stations = hc.sql("SELECT wban_number, yearmonthday, cz_year, cz_month, dayofmonth FROM weatherStation")
stations.write.parquet("/user/sachin/output/hive-spark")
