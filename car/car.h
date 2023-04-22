#pragma once
#include <string>
#include <vector>
#include "car_user_settings.h"

class car {
	std::string ID;
	std::vector<std::string> users_ID;
	car_user_settings active_user_settings;
	double interior_temperature;
	double outside_temperature;
	double current_speed;
	double localization[2];
	std::string active_session_ID;
	void send_localization();
	void authenticate();
	void set_active_user_settings();
public:
	car(std::string);
	void unlock();
	void lock();
	void open_door();
	void start_engine();
	void stop_engine();
	void heat_up();
	void cool_down();
	void drive();
};