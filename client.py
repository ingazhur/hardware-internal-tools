import banana_dev as banana
import numpy as np
import json

model_inputs = {
  "image": "images/simple.jpg"
}

# import api key and model key from config file
api_key = None
model_key = None
with open("config.json", "r") as f:
    config = json.load(f)
    api_key = config["API_KEY"]
    model_key = config["MODEL_KEY"]

# Run the model
out = banana.run(api_key, model_key, model_inputs)

masks = out["modelOutputs"][0]["masks"]

#Convert segmentation list to numpy array
for mask in masks:
    mask["segmentation"] = np.array(mask["segmentation"])
