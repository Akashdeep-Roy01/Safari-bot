# Safari-bot

![ROS2](https://camo.githubusercontent.com/b874e7cbc7323284002070083cf5fc1cfff41a3a5573f598638564fa4017fd65/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f524f5320322d68756d626c652d626c756576696f6c6574)
![Docker](https://camo.githubusercontent.com/b609225bdb4ad668a23ec18b022f166bd86e184b28ddcf34b604f4a68837907f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3234393645443f7374796c653d666c61742d737175617265266c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465)

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

