#version 1.0
#!/usr/bin/env python
# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://aws.amazon.com/asl/
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express
# or implied. See the License for the specific language governing permissions
# and limitations under the License.
"""Simple command-line realtime prediction utility

Usage:
    python realtime.py ml_model_id attribute1=value1 attribute2=value2 
...
or:
    python realtime.py ml_model_id --deleteEndpoint

Multi-word text attributes can be specified like:
    python realtime.py ml-12345678901 "textVar=Multiple words grouped 
together" numericVar=123
"""

import boto
import boto3
import json
import sys
import time
import aws


danceclient = aws.getClient('machinelearning','us-east-1')
instrumentclient = aws.getClient('machinelearning','us-east-1')
acousticclient = aws.getClient('machinelearning','us-east-1')
energyclient = aws.getClient('machinelearning','us-east-1')
genreclient = aws.getClient('machinelearning','us-east-1')
#ml_model_id = "MLModelId='finalmodel2'"


"""
def parse_args_to_dict(argv):
    ##Returns a record as a python dict by parsing key=value pairs
    ##from the command line
    record = {}
    for kv in argv:
        try:
            (k, v) = kv.split('=')
            record[k] = v
   	    print record
        except:
            print('Unable to parse "%s" as attribute=value' % kv)
            raise RuntimeError()
    if not record:
        print("No attributes specified")
        raise RuntimeError()
    return record
"""

def realtime_predict(record):
    """Takes a string ml_model_id, and a dict record, and makes a realtime
    prediction call, if the ML Model has a realtime endpoint.
    If the ML Model doesn't have a realtime endpoint, it creates one instead
    of calling predict()
    """
    #ml = client.connect_machinelearning()
    dancemodel = danceclient.get_ml_model(MLModelId='danceability0')
    danceendpoint = dancemodel.get('EndpointInfo', {}).get('EndpointUrl', '')
    acousticmodel = acousticclient.get_ml_model(MLModelId='Acoustic0')
    acousticendpoint = acousticmodel.get('EndpointInfo', {}).get('EndpointUrl', '')
    instrumentmodel = instrumentclient.get_ml_model(MLModelId='Instrumentalness0')
    instrumentendpoint = instrumentmodel.get('EndpointInfo', {}).get('EndpointUrl', '')
    energymodel = energyclient.get_ml_model(MLModelId='Energy0')
    energyendpoint = energymodel.get('EndpointInfo', {}).get('EndpointUrl', '')
    genremodel = genreclient.get_ml_model(MLModelId='Genre0')
    genreendpoint = genremodel.get('EndpointInfo', {}).get('EndpointUrl', '')
    if (danceendpoint and acousticendpoint and instrumentendpoint and energyendpoint and genreendpoint):
        #print('ml.predict("%s", %s, "%s") # returns...' % (ml_model_id, json.dumps(record, indent=2), endpoint))
        start = time.time()
	print "this is the record"
	print record
        
	danceprediction = danceclient.predict(MLModelId='danceability0', Record=record, PredictEndpoint=danceendpoint)
        acousticprediction = acousticclient.predict(MLModelId='Acoustic0', Record=record, PredictEndpoint=acousticendpoint)
	instrumentprediction = instrumentclient.predict(MLModelId='Instrumentalness0', Record=record, PredictEndpoint=instrumentendpoint)
	energyprediction = energyclient.predict(MLModelId='Energy0', Record=record, PredictEndpoint=energyendpoint)
	genreprediction = genreclient.predict(MLModelId='Genre0', Record=record, PredictEndpoint=genreendpoint)
	latency_ms = (time.time() - start)*1000
        print(json.dumps(danceprediction, indent=4))
	print(json.dumps(acousticprediction, indent=4))
	print(json.dumps(instrumentprediction, indent=4))
	print(json.dumps(energyprediction, indent=4))
	print(json.dumps(genreprediction, indent=4))
	
        print("Latency: %.2fms" % latency_ms)
        return danceprediction,acousticprediction,instrumentprediction,energyprediction,genreprediction    

    #else:
       # print('# Missing realtime endpoint\nml.create_realtime_endpoint("%s")' % ml_model_id)
       # result = client.create_realtime_endpoint(MLModelId='danceability0')
	#print(json.dumps(result, indent=2))
  #      print("""# Predictions will fail until the endpoint has been fully created.# Note that you will be charged a reservation fee until this endpoint is deleted.# Delete with:
 #python realtime.py %s --deleteEndpoint""" % ml_model_id)


#def delete_realtime_endpoint():
    #ml = client.connect_machinelearning()
    #print('# Deleting realtime endpoint\nml.delete_realtime_endpoint("%s")' %ml_model_id)
    #result = client.delete_realtime_endpoint(MLModelId='danceability0')
    #print(json.dumps(result, indent=2))


"""
if __name__ == "__main__":
    try:
        ml_model_id = sys.argv[1]
        delete_endpoint = (sys.argv[2] == "--deleteEndpoint")
        if not delete_endpoint:
            record = parse_args_to_dict(sys.argv[1:])
	    print record
    except:
        print(__doc__)
        sys.exit(-1)
  #  if delete_endpoint:
   #     delete_realtime_endpoint()
   # else:
    #    realtime_predict(record)
"""


