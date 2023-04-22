#pragma once
#include <string>
#include <vector>
#include <iostream>

class car_user_settings {
	int seat_angle;
	int seat_height;
	int seat_distance;
	int steering_wheel_height;
	int steering_wheel_distance;
	int left_mirror_angle_x;
	int left_mirror_angle_y;
	int right_mirror_angle_x;
	int right_mirror_angle_y;
	int rear_mirror_angle_x;
	int rear_mirror_angle_y;
	int lights_angle;
	std::string car_ID;
public:
	std::string get_car_ID() { return car_ID; }
	car_user_settings(std::string, int*);
	void show_settings();
};