#!/bin/bash
docker run -it \
    --name safari_bot_1 \
    --user ros \
    --gpus all \
    --env NVIDIA_VISIBLE_DEVICES=all   \
    --env NVIDIA_DRIVER_CAPABILITIES=all  \
    --env DISPLAY=${DISPLAY}  \
    --volume /tmp/.X11-unix:/tmp/.X11-unix \
    -v $PWD:/docker_ws \
    --network host \
    --runtime nvidia \
    safari_bot:v1

