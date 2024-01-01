# Safari-bot

![ROS2](https://img.shields.io/badge/ROS2-Humble-%23F46800.svg?style=for-the-badge&logo=ROS2-Humble&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

ROS2 package for simulating autonomous navigation of a differential drive robot equipped with LiDAR and Camera.

To use:

1. Build the docker file using `docker build -t <image name> .`
2. Change the image name inside "docker_run.sh" and run it using `bash docker_run.sh`
3. Build the package using `colcon build --symlink-install`
4. Source using `source /docker_ws/install/setup.bash`
5. Run the nodes `ros2 launch safari_bot online_async_launch.py`
6. In another terminal run `ros2 launch nav2_bringup navigation_launch.py`

![Image](https://github.com/Akashdeep-Roy01/Safari_bot/assets/99131809/8d5be9d1-c27e-4036-929f-ef75d8eb04a9)

## Video

https://github.com/Akashdeep-Roy01/Safari_bot/assets/99131809/67779da3-3cc2-488a-8c17-045bfc202b32

