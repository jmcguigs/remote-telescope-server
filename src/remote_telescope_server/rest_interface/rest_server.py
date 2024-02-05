from fastapi import FastAPI
import socket


telescope_server = FastAPI()


@telescope_server.get("/")
async def read_root():
    return {"message": "Hello World"}


@telescope_server.get("/ip_info")
async def read_ip_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {"hostname": hostname, "ip_address": ip_address}
