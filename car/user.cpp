#include "user.h"

user::user(std::string uID, std::vector<car_user_settings*> user_set)
{
	user_ID = uID;
	cars_settings = user_set;
}
