#include "user.h"

user::user(std::string uID, std::vector<car_user_settings*> user_set)
{
	user_ID = uID;
	cars_settings = user_set;
}

void user::show_cars_settings()
{
	if (cars_settings.size() == 0) {
		std::cout << "User " << user_ID << " doesn't have any saved settings.\n";
		return;
	}
	std::cout << "User " << user_ID << " has saved settings for cars: ";
	for (car_user_settings* set : cars_settings)
		std::cout << set->get_car_ID() << ' ';
	std::cout << std::endl;
}
