#!/usr/bin/env python3
from fastapi import FastAPI
from .cors import args as cors_args


def init_middleware(app: FastAPI):
    app.add_middleware(**cors_args)