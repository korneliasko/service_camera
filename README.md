# 📷 service_camera – ROS 2 Image Capture Service

![ROS 2 Humble](https://img.shields.io/badge/ROS%202-Humble-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey)

This repository contains a **ROS 2 service node** that allows capturing and saving an image from an **Orbbec Femto Mega camera** using a simple service call.  
The node is designed to run inside a **Docker container** with **ROS 2 Humble**.

---

## 🧩 Overview

- **Camera driver:** Orbbec Femto Mega  
- **ROS 2 distro:** Humble  
- **Service type:** `example_interfaces/srv/Trigger`  
- **Service name:** `/save_image`  
- **Output:** Images saved inside the container and copied to the host machine  

---

## 🖥️ System Setup

All commands are executed on the remote machine **`sonata`**, inside the Docker container:

```bash
docker exec -it kornelia_humble bash
