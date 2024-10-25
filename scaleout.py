import requests
import json


image_id = Enter Image Id here
count = Enter the Number of replicas here
ssh_key_id = Enter the SSH ID

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer XXXXXX'
}

get_droplet_id = f"https://api.digitalocean.com/v2/snapshots/{image_id}"
response = requests.request("GET", get_droplet_id, headers=headers)

data = json.loads(response.text)


get_droplet_details = f"https://api.digitalocean.com/v2/droplets/{data['snapshot']['resource_id']}"

response = requests.request("GET", get_droplet_details, headers=headers)

data = json.loads(response.text)

url = "https://api.digitalocean.com/v2/droplets"
for i in range(count):
  payload = json.dumps({
  "name": data['droplet']['name']+"-" + str(i + 1),
  "region": data['droplet']['region']['slug'],
  "size": data['droplet']['size_slug'],
  "image": image_id,
  "ssh_keys": [
    ssh_key_id
  ],
  "monitoring": "true",
  "tags": [
   "test-scale",
   "scaleout"
  ],
  "vpc_uuid": data['droplet']['vpc_uuid']
  })


  response = requests.request("POST", url, headers=headers, data=payload)
  if response.status_code == 202:
    print(f"Droplet {data['droplet']['name']}-{i + 1} is creating")
  else:
    print(f"Failed to create droplet: {response.text}")



