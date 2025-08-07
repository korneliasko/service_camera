# service_camera

# TERMINAL 1
# ssh sonata
# docker ps -a (check the status)
# docker exec -it kornelia_humble bash (run your docker)
# cd ..
# cd ros2_ws/ (to be in: root@lrm-sonata:~/ros2_ws#)
# source /opt/ros/humble/setup.bash
# source install/setup.bash
# sklonuj paczke: git clone https://github.com/korneliasko/service_camera.git
# colcon build
# ros2 run py_srvcli service

# TERMINAL 2
#ssh sonata
#docker exec -it kornelia_humble bash
#cd ..
#cd ros2_ws/
#ros2 launch orbbec_camera femto_mega.launch.py

# TERMINAL 3
docker exec -it kornelia_humble bash
source
source
ros2 service call /save_image example_interfaces/srv/Trigger

