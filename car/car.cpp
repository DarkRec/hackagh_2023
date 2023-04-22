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
		if (cs->get_car_ID() == car_ID)
			active_user_settings = cs;
}

int car::authenticate(std::string uID)
{
	return 0;
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
	set_active_user_settings(uID);
	std::cout << "Car is unlocked" << std::endl;
}

void car::lock()
{
	is_car_locked = true;
}

void car::start_engine()
{
	is_engine_on = true;
}

void car::stop_engine()
{
	is_engine_on = false;
}

void car::set_temperature(double temperature)
{

}

void car::drive()
{
}
