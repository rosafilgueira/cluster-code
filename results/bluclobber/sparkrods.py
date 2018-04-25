import pyspark
import requests
from requests import get

def get_streams(downsample=1, source="oids.txt", app="iRodsSpark"):


    sc = pyspark.SparkContext(appName=app)

    oids = map(lambda x: x.strip(), list(open('oids.txt')))
    print(">>> oids is %s" % oids)
    rddoids = sc.parallelize(oids)
    streams = rddoids.map(lambda url: get(url, stream=True).raw)
    print (">>>>>>> Streams %s" % streams)
    return streams
