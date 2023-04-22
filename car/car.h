#pragma once
#include <string>
#include <vector>
#include <iostream>
#include "car.h"
#include "car_user_settings.h"
#include "user.h"

class car {
	std::string car_ID;
	std::vector<std::string> users_ID;
	car_user_settings* active_user_settings;
	std::string active_user_ID;
	//double interior_temperature;
	//double outside_temperature;
	double current_speed;
	bool is_car_locked;
	bool is_engine_on;
	bool is_key_docked;
	double localization[2];
	user* find_user();
	void set_active_user_settings(std::string);
	int authenticate(std::string);
public:
	void show_car_state();
	void show_users_ID();
	double* get_location();
	car(std::string, std::vector<std::string>, int*);
	void unlock(std::string);
	void lock();
	void start_engine(std::string = "");
	void stop_engine();
	void set_temperature(double);
	void drive();
};

extern std::vector<car*> cars_DB;