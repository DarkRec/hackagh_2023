#include "car_user_settings.h"

car_user_settings::car_user_settings(std::string cID, int* car_settings)
{
	car_ID = cID;
	seat_angle = car_settings[0];
	seat_height = car_settings[1];
	seat_distance = car_settings[2];
	steering_wheel_height = car_settings[3];
	steering_wheel_distance = car_settings[4];
	left_mirror_angle_x = car_settings[5];
	left_mirror_angle_y = car_settings[6];
	right_mirror_angle_x = car_settings[7];
	right_mirror_angle_y = car_settings[8];
	rear_mirror_angle_x = car_settings[9];
	rear_mirror_angle_y = car_settings[10];
	lights_angle = car_settings[11];
}

void car_user_settings::show_settings()
{
	std::cout << "Seat angle: " << seat_angle << '\n';
	std::cout << "Seat height: " << seat_height << '\n';
	std::cout << "Seat distance: " << seat_distance << '\n';
	std::cout << "Steering wheel height: " << steering_wheel_height << '\n';
	std::cout << "Steering wheel distance: " << steering_wheel_distance << '\n';
	std::cout << "Left mirror angle x: " << left_mirror_angle_x << '\n';
	std::cout << "Left mirror angle y: " << left_mirror_angle_y << '\n';
	std::cout << "Right mirror angle x: " << right_mirror_angle_x << '\n';
	std::cout << "Right mirror angle y: " << right_mirror_angle_y << '\n';
	std::cout << "Rear mirror angle x: " << rear_mirror_angle_x << '\n';
	std::cout << "Rear mirror angle y: " << rear_mirror_angle_y << '\n';
	std::cout << "Lights angle: " << lights_angle << '\n';
}
