import http.client
import json
import time

conn = http.client.HTTPSConnection("faucet.testnet.inco.org")
payload1 = json.dumps({
    "address": "0x1d2d4062F3bF9789bE550F08B7b9Add010EEb5D8"
})

arrays = [payload1, payload1]

headers = {
  'Content-Type': 'application/json'
}

for payload in arrays:
  conn.request("POST", "/api/get-faucet", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))
  print("-------------------------------------\n")
  time.sleep(2)
