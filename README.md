service_camera

# TERMINAL 1
ssh sonata

docker ps -a           # check the status of containers (optional)

docker exec -it kornelia_humble bash   # run your docker container

cd ros2_ws/            # now in: root@lrm-sonata:~/Shared/ros2_ws#

source /opt/ros/humble/setup.bash

source install/setup.bash

git clone https://github.com/korneliasko/service_camera.git # clone the package - not needed i think

colcon build

ros2 run py_srvcli service


# TERMINAL 2
ssh sonata
docker exec -it kornelia_humble bash  

cd ros2_ws/

source /opt/ros/humble/setup.bash

source install/setup.bash

ros2 launch orbbec_camera femto_mega.launch.py 

#for a narrow view:
ros2 launch orbbec_camera femto_mega.launch.py depth_mode:=NFOV_UNBINNED
ros2 launch orbbec_camera femto_mega.launch.py fov:=narrow


#if launched the camera already
ros2 param set /camera depth_mode NFOV_UNBINNED
ros2 param set /camera fov narrow


# TERMINAL 3

ssh sonata

docker exec -it kornelia_humble bash

cd ros2_ws (always in: root@lrm-sonata:~/Shared/ros2_ws/)

source /opt/ros/humble/setup.bash

source install/setup.bash

ros2 service call /save_image example_interfaces/srv/Trigger


# COPY

to copy from the root first from outside the container do:

skorupk@lrm-sonata:~$ docker cp kornelia_humble:/root/Shared/ros2_ws/images ~/images
Successfully copied 20MB to /home/skorupk/images
copying from the docker to images folder in /home/skorupk

now in another window, from outside sonata: 

PS C:\Users\korne> scp -r sonata:~/images "C:/Users/korne/14_08_complex_scenarios" 

scp -r to copy the whole folder instead of only one file

