d = {}

d ["sensorData"] = {
"temp":"67",
"humi" : "56"
}
print(d)

import json
data = json.dumps(d)

with open("temp.json","w") as f:
  f.write(data)

