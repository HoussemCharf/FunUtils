#!/usr/bin/python2

'''
This script is used to count number of lines that are present with an 'e' or 'g'
in a file using Apache Spark.

'''
  



from pyspark import SparkContext

sc=SparkContext("local","App_first")
filename=""# Enter path of the file

load_file=sc.textFile(filename).cache()

numacount=load_file.filter(lambda s:'g' in s).count()
numbcount=load_file.filter(lambda s:'e' in s).count()


print "line with g:%i, line with e:%i"%(numacount,numbcount)
