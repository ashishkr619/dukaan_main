#!/usr/bin/env bash

# Push image to ECR(Skip Pushing the Docker Image to AWS ECR)
###################
# aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 

# # update latest version
# docker tag dukaan_shop/dukaan:latest 884880669712.dkr.ecr.us-west-2.amazonaws.com/dukaan_shop/dukaan_service:latest
# docker push 884880669712.dkr.ecr.us-west-2.amazonaws.com/dukaan_shop/dukaan_service:latest
