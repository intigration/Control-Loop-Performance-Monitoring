
import json, urllib.request
def post_to_slack(webhook_url: str, text: str):
    data = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(webhook_url, data=data, headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req) as resp: return resp.read()
