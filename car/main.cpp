#include "car_user_settings.h"
#include "car.h"
#include "user.h"
//#include "connection.h"
#include "functions.h"

std::vector<car*> cars_DB;
std::vector<user*> users_DB;

int main()
{
	initialize();
	user* us = users_DB[0];
	car* ca = cars_DB[0];
	us->show_cars_settings();
	ca->show_users_ID();
	ca->unlock(us->get_user_ID());
	ca->start_engine(us->get_user_ID());
	ca->drive();
	ca->stop_engine();

	std::cout << std::endl;

	us = users_DB[1];
	us->show_cars_settings();
	ca->show_users_ID();
	ca->unlock(us->get_user_ID());
	ca->start_engine();
	ca->drive();
}