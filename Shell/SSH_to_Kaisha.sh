#!/bin/sh

ssh -i ~/.ssh/authorized_keys -R 8157:127.0.0.1:8888 -p 443 NMCORP\N196315@10.20.171.189

