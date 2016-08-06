export PYTHON_EGG_CACHE=./myeggs
impala-shell -q "invalidate metadata"
echo "*** entering r.sh"
hostname
pwd
echo "*** running Rscript weather3.R"
Rscript weather3.R
echo "***exiting r.sh"
