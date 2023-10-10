#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/metrics")
def metrics():
    return {"data": "Prometheus monitoring data"}


@app.get("/ok")
def ok():
    return {"message": "hello world"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
