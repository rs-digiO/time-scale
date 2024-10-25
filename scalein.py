import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer XXXX'
}

url = "https://api.digitalocean.com/v2/droplets?tag_name=scaleout"

response = requests.request("DELETE", url, headers=headers)
