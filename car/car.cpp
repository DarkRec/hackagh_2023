#include "car.h"

user* car::find_user() {
	for (user* us : users_DB)
		if (us->get_user_ID() == active_user_ID)
			return us;
	return nullptr;
}

void car::set_active_user_settings(std::string uID)
{
	for (car_user_settings* cs : find_user()->get_cars_settings())
		if (cs->get_car_ID() == car_ID) {
			active_user_settings = cs;
			std::cout << "Imported settings for user " << active_user_ID << std::endl;
			return;
		}
	std::cout << "Can't find settings for user " << active_user_ID << std::endl;
}

void car::show_car_state()
{
	std::cout << "Car ID: " << car_ID << '\n';
	std::cout << "Active user: " << active_user_ID << '\n';
	std::cout << "Doors locked: " << is_car_locked << '\n';
	std::cout << "Engine on: " << is_engine_on << '\n';
	std::cout << "Key docked: " << is_key_docked << '\n';
	std::cout << "Car user settings\n";
	active_user_settings->show_settings();
	std::cout << std::endl;
}

void car::show_users_ID()
{
	std::cout << "Users allowed to use car " << car_ID << ": ";
	for (std::string u : users_ID)
		std::cout << u << ' ';
	std::cout << std::endl;
}

double* car::get_location()
{
	return new double[2] {localization[0], localization[1]};
}


car::car(std::string cID, std::vector<std::string> usID, int* def_set)
{
	car_ID = cID;
	users_ID = usID;
	active_user_settings = new car_user_settings(cID, def_set);
	active_user_ID = "";
	current_speed = 0;
	is_car_locked = true;
	is_engine_on = false;
	is_key_docked = false;
	localization[0] = 48.03245;
	localization[1] = 25.32521;
}

void car::unlock(std::string uID)
{
	for (std::string us : users_ID)
		if (uID == us)
			active_user_ID = uID;
	if (active_user_ID == "")
		return;
	is_car_locked = false;
	std::cout << "Car " << car_ID << " has been unlocked by user " << active_user_ID << std::endl;
	set_active_user_settings(uID);
}

void car::lock()
{
	is_car_locked = true;
}

void car::start_engine(std::string uID)
{
	is_engine_on = true;
	std::cout << "Engine has been started.\n";
	if (uID == active_user_ID) {
		is_key_docked = true;
		std::cout << "Key has been docked.\n";
	}
}

void car::stop_engine()
{
	is_engine_on = false;
	std::cout << "Engine has been stopped.\n";
	is_key_docked = false;
	std::cout << "Key is undocked.\n";
}

void car::drive()
{
	double accel = 10;
	int loc_index = 0;
	for (int i = 0; i < 7; i++)
	{
		std::cout << "Speed: " << current_speed << " | ";
		std::cout << "Localization: [" << localization[0] << ", " << localization[1] << "]\n";
		if (is_key_docked == false && current_speed > 20)
		{
			std::cout << "Key isn't docked, unauthorized use of car " << car_ID << " detected.\n";
			std::cout << "Pulling over to a safe localization.\n";
			accel = -10.;
			loc_index = 1;
		}
		if (current_speed < 60)
			current_speed = current_speed + accel;
		localization[loc_index] += current_speed / 3.6;
		if (current_speed <= 0) {
			std::cout << "Speed: " << current_speed << " | ";
			std::cout << "Localization: [" << localization[0] << ", " << localization[1] << "]\n";
			std::cout << "Car has been stopped.\n";
			is_engine_on = false;
			is_key_docked = false;
			return;
		}
	}
	accel = -20;
	loc_index = 1;
	for (int i = 0; i < 3; i++) {
		std::cout << "Speed: " << current_speed << " | ";
		std::cout << "Localization: [" << localization[0] << ", " << localization[1] << "]\n";
		if (current_speed > 0)
			current_speed = current_speed + accel;
		if (current_speed <= 0) {
			std::cout << "Speed: " << current_speed << " | ";
			std::cout << "Localization: [" << localization[0] << ", " << localization[1] << "]\n";
			std::cout << "Car has been stopped.\n";
			is_engine_on = false;
			is_key_docked = false;
			return;
		}
		localization[loc_index] += current_speed / 3.6;
	}
}
