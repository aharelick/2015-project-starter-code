#!/bin/sh

curl -H "Content-Type: application/json" -X POST -d '{"coordinates":[{"latitude": 1.0, "longitude": 2.0, "notes": "these are notes!"}]}' http://localhost:5000/coordinates