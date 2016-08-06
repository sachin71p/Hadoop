DROP TABLE weather_modified;
CREATE EXTERNAL TABLE weather_modified  ( 
    `wban_number`                    int, 
    `yearmonthday`                    string, 
    `cz_year`                              int, 
    `cz_month`                           int
)
    
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 'hdfs://nameservice/user/sachin/output/hive-spark'
TBLPROPERTIES ('COLUMN_STATS_ACCURATE'='false', 'numFiles'='0', 'numRows'='-1', 'rawDataSize'='-1', 'totalSize'='0');
