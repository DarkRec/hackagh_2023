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
	ca->show_car_state();
	ca->unlock(us->get_user_ID());
	ca->show_car_state();
}