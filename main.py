from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(
    host='redis-14534.c243.eu-west-1-3.ec2.cloud.redislabs.com',
    port=14534,
    password='OprdsfdVpyMVY5Hoj8VEyO4lPntNuqKF',
    decode_responses=True
)
