#!/usr/bin/env Rscript
# Load the dplyr library and a helper library.
library(dplyr)
library(dplyrimpaladb) 

# Identify the source of the data as the Impala 'weather_modified' table
default_db <- src_impaladb('default', host='10.128.73.107')
# INVALIDATE METADATA default.weather_modified
weather_data <- tbl(default_db, sql('SELECT * FROM weather_modified'))

print('*** Print typeof weather_data: ***')
typeof(weather_data)

print('*** Head weather_data: ***')
head(weather_data)

print('*** Print the dimensions of the table: ***')
dim(weather_data)

print('*** Print the first 10 rows of the data: ***')
weather_data

print('*** weather_sample: Run a simple table query and view the results: ***')
weather_sample <- weather_data %>% group_by(cz_year, cz_month) %>% summarise(num_months = count(cz_month)) %>% arrange(cz_year, cz_month)
weather_sample

print('*** weather_Jan2000: Run a simple table query and view the results: ***')
weather_jan2000 <- tbl(default_db, sql('SELECT * FROM weather_modified WHERE cz_year = 2000 AND cz_month = 1'))
weather_jan2000

print('*** write to local /tmp/weather_jan2000.csv ***')
file.create("weather_jan2000.csv")
locfile <- "weather_jan2000.csv"
write.table(weather_data, locfile, row.names=FALSE, na="", col.names=FALSE, sep=",")

print('*** init rhdfs: ***')
library(rhdfs)
Sys.setenv(HADOOP_CMD="/bin/hadoop")
Sys.setenv(HADOOP_USER_NAME="sachin")
hdfs.init()

print('*** copy to hdfs weather_jan2000.csv ***')
hfile <- "output/weather_jan2000.csv"
hdfs.put(locfile, hfile)  # copy local file to hdfs
hdfs.file.info(hfile)
