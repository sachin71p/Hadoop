DROP TABLE default.weather_jan2000;
CREATE EXTERNAL TABLE default.weather_jan2000  ( 
    `wban_number`                    int, 
    `yearmonthday`                    string, 
    `cz_year`                              int, 
    `cz_month`                           int
)
row format delimited fields terminated by ','
STORED AS textfile;
load data inpath "/user/sachin/output/weather_jan2000.csv" into TABLE default.weather_jan2000;
