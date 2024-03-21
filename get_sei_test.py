import http.client
import json
import time
import sys

conn = http.client.HTTPSConnection("api.faucet.nima.enterprises")

coin_address = ["0x7bA0f41AFb392f647e7E64dDad8912fa6F7a76bd"]

json_body1 = {
    "address": "0x7bA0f41AFb392f647e7E64dDad8912fa6F7a76bd",
    "chain_id": 713715
}


jsons = [json_body1]

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNzQwN2MxMDkyOTVjNjFkNjJmZjRiODk4NDRjMTMzZmQyYmU5M2Y3ZjJlMzU4MDhjZDZiZGZiZGU0MjNiZTEzN2ZiMGEwMjQ1YTMzNTRlOGEiLCJpYXQiOjE3MTA5MzIxODQuMjQyNjkzLCJuYmYiOjE3MTA5MzIxODQuMjQyNjk1LCJleHAiOjE3MTExMDQ5ODQuMjM3MjA2LCJzdWIiOiI4NDQxIiwic2NvcGVzIjpbXX0.p4_nfEfCR07LyvacjNrGRHsF2Lbzf-XXqP5S5wZjJUPejDgyfYgq3edOslu9Himp0vG4YNlwyJ1zw_3j8m2BeUd7IpFqeCRIbL7dfmGwC4bEctiOv2U6kuX1k2DSiSDGdKY1S5tsDIJFndBsZKg3X1Wpt2uaMQSOkUgzEDBgOUv5iZCCyCa90A_dfKeRZMu_2YmT7nGesgjtM7j9JxNRn-Mm5YRK0ntkRwS7abgbay3txKuvTZnbp_tTsPl9EgFHDFZrpS0VESvdqfb8LWqaxRdMtCIMdAex_g40KHhmWpw5qvkn1puNwCRWyC3ZjEpoG090mUJHZfcRUghSIu4cLm79RXGCfb63a9upfyTu42cTHcoa_Qqn3Ckd7gF6WmQNH0JOnDL7msttRHFBDdnXGqe07OUbFPmHO31S9KUxYrAqUQdKNEn0E0f106RH4JSLbj9m7pRd6T6lH55vfg7PU63uSfs1HeB-PB7lXBg_caNv82rHP5bEo_9dngnqa49IlBy7xy2IMt4hIibq9Aa80V1uiTJoKZDGIvEIGgOov35hRQVSRTrnYPI7lb_a9EbOhXypZLZx1kZi1vMXfxpGx4e4nXQicLWmIhwSxVBshw87MM7wvDIjBl56NLNs0lGQ24lv5qKS4EfjL3XwP1JkJ67IsGoWROhH8F4u8y1itI4'
}

for body in jsons:
    payload = json.dumps(body)
    conn.request("POST", "/api/faucet/claim", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("-------------------------------------\n")
    print(data.decode("utf-8"))
    time.sleep(2)
