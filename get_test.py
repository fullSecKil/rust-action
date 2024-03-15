import http.client
import json
import time
import sys

conn = http.client.HTTPSConnection("api.testnet.solana.com")

# payload1 = json.dumps({
#   "method": "requestAirdrop",
#   "jsonrpc": "2.0",
#   "params": [
#     "5Q4hmzMSKjLdjpKsqn8KLxiHxUmrNUGmSYbbWNJH2PYj",
#     1000000000
#   ],
#   "id": "314811ae-f599-4e0f-8752-08df10dc6ccd"
# })

# payload2 = json.dumps({
#   "jsonrpc": "2.0",
#   "id": "96dec5c4-4e6e-447e-bcf3-2bdebf9d282d",
#   "method": "requestAirdrop",
#   "params": [
#     "5Q4hmzMSKjLdjpKsqn8KLxiHxUmrNUGmSYbbWNJH2PYj",
#     1000000000
#   ]
# })

# payload3 = json.dumps({
#   "jsonrpc": "2.0",
#   "id": "c5935154-73a1-4712-9c08-c392d216dd22",
#   "method": "requestAirdrop",
#   "params": [
#     "5Q4hmzMSKjLdjpKsqn8KLxiHxUmrNUGmSYbbWNJH2PYj",
#     1000000000
#   ]
# })


# arrays = [payload1, payload1, payload2, payload2, payload3]

# coin_address = ["5Q4hmzMSKjLdjpKsqn8KLxiHxUmrNUGmSYbbWNJH2PYj", "ASQ3GaBQwSeDuTFrADvBGVbqLqNtahkZnBprHT4uEso7"
#            , "2KGd36cUGrkkZJCUJ9vr3mmPxH5VXMvQdxAywepRfokJ", "AksDqZzMudL53f2ioWq7QNhpeFiuNjLREUjc37jCajat",
#            "F5Ypik73KXF52dYFEs8qctZkvNs2bkrWkwoVWfk1rZ4d", "69xgmEVpRTS2ykxLidegUP7baNB8wor7xx3BKgqKB7yb"]

coin_address = [sys.argv[1]]

json_body1 = {
  "method": "requestAirdrop",
  "jsonrpc": "2.0",
  "params": [
    "5Q4hmzMSKjLdjpKsqn8KLxiHxUmrNUGmSYbbWNJH2PYj",
    1000000000
  ],
  "id": "314811ae-f599-4e0f-8752-08df10dc6ccd"
}

json_body2 = {
  "jsonrpc": "2.0",
  "id": "96dec5c4-4e6e-447e-bcf3-2bdebf9d282d",
  "method": "requestAirdrop",
  "params": [
    "5Q4hmzMSKjLdjpKsqn8KLxiHxUmrNUGmSYbbWNJH2PYj",
    1000000000
  ]
}

json_body3 = {
  "jsonrpc": "2.0",
  "id": "c5935154-73a1-4712-9c08-c392d216dd22",
  "method": "requestAirdrop",
  "params": [
    "5Q4hmzMSKjLdjpKsqn8KLxiHxUmrNUGmSYbbWNJH2PYj",
    1000000000
  ]
}

jsons = [json_body1, json_body1, json_body2, json_body2, json_body3]

headers = {
  'Content-Type': 'application/json'
}

for address in coin_address:
  for body in jsons:
    body['params'] = [address, 1000000000]
    payload = json.dumps(body)
    conn.request("POST", "/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("address "+ address +"-------------------------------------\n")
    print(data.decode("utf-8"))
    time.sleep(2)
