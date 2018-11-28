from flask import Flask, render_template, request
import boto3
import random
import uuid

application = Flask(__name__)
ec2_client = boto3.client('ec2')
response = ec2_client.describe_availability_zones()


@application.route('/')
def index():
	zone = response['AvailabilityZones'][0]['ZoneName']
	return render_template('index.html', availability_zone = zone)

if __name__ == "__main__":
    application.run(host='0.0.0.0', threaded=True)
