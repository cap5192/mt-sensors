import meraki
from prettytable import PrettyTable

API_KEY = "f59c3b2d2521afb6904361242c3ddd5bc4ad29f7"
org_id = "877061"
net_id = "L_634444597505856873"
sr = ["Q3CA-2DS4-798S"]
dashboard = meraki.DashboardAPI(API_KEY)

response = dashboard.sensor.getOrganizationSensorReadingsLatest(org_id, total_pages='all', serials = sr)
for i in response:
    print(i["readings"])