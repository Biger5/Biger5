import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="gcs.json"
from typing import Annotated
from fastapi import FastAPI, Form
import uvicorn

import tensorflow as tf
import pandas as pd
import numpy

import google.auth

from gmapsapis.geocoding import get_location

app = FastAPI()
credentials, project = google.auth.default()
print(f"this from google.auth {project}")

@app.get('/')
def main():
  return {
    "serverStatus": "server is running...",
    "team": "CH2-PS514",
    "TFversion": tf.__version__
  }
  
@app.get('/geocode')
def location(formattedAddress: str):
  response = get_location(formattedAddress)
  print(response)
  return response

@app.post('/v1/business')
async def get_recommendation(formattedAddress: Annotated[str, Form()], price: Annotated[str, Form()], rating: Annotated[float, Form()]):
  # print(Request['formattedAddress'])
  print('getting user location coordinate...')
  user_location = get_location(formattedAddress)
  print('getting user location pass...')
  # Load model here
  print('loading savedmodel from gcs...')
  # MODEL V1
  # load_gcs_model = tf.saved_model.load('models/modelv1')
  # MODEL V2
  load_gcs_model = tf.saved_model.load('models/modelv2')
  print('load model pass...')
  formality, recommendation = load_gcs_model({
    "price": tf.constant([price], dtype=tf.string),
    "rating": tf.constant([rating], dtype=tf.float32),
    "latitude": tf.constant([user_location['lat']], dtype=tf.float32),
    "longitude": tf.constant([user_location['lng']], dtype=tf.float32)
  })
  print('input pass...')
  x = recommendation[0].numpy()
  extract = []
  for value in x:
    extract.append(value.decode())
  
  print('extract pass...')
  # DATASET V1
  # dataset = pd.read_csv('gs://ml-models-capstone-ch2-ps514/datasets/v0.0.1/datacapstone.csv') 
  # DATASET V2
  dataset = pd.read_csv('gs://ml-models-capstone-ch2-ps514/datasets/v0.0.2/datacapstone_2.csv')
  print('load dataset success...')
  source_data = pd.DataFrame()
  print('load dataset frame pass...')
  source_data['price'], source_data['longitude'], source_data['latitude'], source_data['rating'], source_data['kategori'], source_data['Restaurant'], source_data['url'], source_data['id'] = dataset[['PriceLevel']], dataset[["Longitude"]], dataset[["Latitude"]], dataset[["Rating"]], dataset[["Category"]], dataset[["Restaurant"]], dataset[["URL"]], dataset[["id"]]
  print('creating dataframe...')
  source_data = source_data.reset_index()
  print('extracting results...')
  place_detail = source_data[source_data['Restaurant'].isin(extract)]
  print('complete...')
  
  return place_detail.drop(columns='index').to_dict("records")

# run uvicorn server programmatically
uvicorn.run(app=app, host='0.0.0.0', port=os.environ.get('PORT', 8080))
