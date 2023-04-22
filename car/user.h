#pragma once
#include <string>
#include <vector>
#include "car_user_settings.h"

class user {
	std::string user_ID;
	std::vector<car_user_settings*> cars_settings;
public:
	user(std::string, std::vector<car_user_settings*>);
	std::string get_user_ID() { return user_ID; }
	std::vector<car_user_settings*> get_cars_settings() { return cars_settings; }
};

extern std::vector<user*> users_DB;