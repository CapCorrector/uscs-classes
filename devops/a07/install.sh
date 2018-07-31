#!/bin/bash
export FRONTEND_IP=10.0.1.16
export BACKEND_IP=10.0.1.17

# Build backend service 
cd backend

vagrant up

cd ..

# Build frontend webservice. 

cd frontend

vagrant up
