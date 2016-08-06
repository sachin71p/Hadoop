spark-submit \
--class user.sachin.sparkapp \
--deploy-mode cluster \
--master yarn-cluster \
hdfs://nameservice:8020/user/sachin/spark-jobs/spark_scala.jar
