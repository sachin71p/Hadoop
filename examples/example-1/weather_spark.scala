package user.sachin

import org.apache.spark._
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.sql.Row
object sparkapp {
    def main(args: Array[String]) {
        val conf = new SparkConf().setAppName("Spark-app")
        val sc = new SparkContext(conf)
        val sqlContext = new org.apache.spark.sql.SQLContext(sc)
        import sqlContext.implicits._
        import sqlContext.sql
        val df = sqlContext.read.parquet("/czdataset/weather/weather_data/000000_0")
        df.select("wban_number", "yearmonthday", "cz_year", "cz_month").write.format("parquet").save("/user/sachin/output/hive-spark")
    }
}
