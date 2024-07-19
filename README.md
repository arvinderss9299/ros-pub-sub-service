# ROS Topic and Service Project

This project demonstrates the implementation of a publisher and subscriber node for a ROS topic, as well as a service server and client node for a ROS service. We will be calculating x to the power of y as an example.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

This project includes:
- A publisher node that publishes messages to a topic.
- A subscriber node that subscribes to the same topic and processes the messages.
- A service server node that provides a service.
- A service client node that calls the service.

## Requirements

- ROS (Robot Operating System) installed
- Python installed

## Installation

Clone the repository and navigate to the project directory:

## Usage
- Source your ROS setup file:
  	```sh
	source /opt/ros/<distro>/setup.bash
- Make sure your ROS master is running:
  	```sh
	roscore
- Run the publisher node:
	```sh
	rosrun  publisher_node.py
- Run the subscriber node:
	```sh
	rosrun pub-sub-service subscriber_node.py
- Run the service server node:
	```sh
	rosrun pub-sub-service exp_calc_service.py
- Run the service client node:
	```sh
	rosrun pub-sub-service exp_calc_client.py


