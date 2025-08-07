#service_camera

#TERMINAL 1
ssh sonata
docker ps -a           # check the status of containers
docker exec -it kornelia_humble bash   # run your docker container

cd ..
cd ros2_ws/            # now in: root@lrm-sonata:~/ros2_ws#

source /opt/ros/humble/setup.bash
source install/setup.bash

#clone the package
git clone https://github.com/korneliasko/service_camera.git

colcon build

ros2 run py_srvcli service


#TERMINAL 2
ssh sonata
#docker exec -it kornelia_humble bash   # (uncomment if needed inside Docker)

cd ..
cd ros2_ws/

ros2 launch orbbec_camera femto_mega.launch.py


#TERMINAL 3
docker exec -it kornelia_humble bash

source /opt/ros/humble/setup.bash
source install/setup.bash

ros2 service call /save_image example_interfaces/srv/Trigger


