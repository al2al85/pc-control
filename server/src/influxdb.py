import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import json

# Open and read the config.json file
with open('src/config.json') as f:
    config = json.load(f)

# Get the InfluxDB information from the config
influxdb_info = config['influxdb']

# Extract the required values
url = influxdb_info['url']
token = influxdb_info['token']
org = influxdb_info['org']

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="elatek_control"

write_api = write_client.write_api(write_options=SYNCHRONOUS)

def write_battery_data(data):
    point = (
        Point("battery")
        .tag("device_id", data['device_id'])
        .field("percent", data['percent'])
        .field("plugged", data['plugged'])
        .field("battery_time", data['time'])
    )
    write_api.write(bucket=bucket, org=org, record=point)
    print('Battery data written to InfluxDB')

# for value in range(5):
#   point = (
#     Point("measurement1")
#     .tag("tagname1", "tagvalue1")
#     .field("field1", value)
#   )
#   write_api.write(bucket=bucket, org="elatek", record=point)
#   time.sleep(1) # separate points by 1 second