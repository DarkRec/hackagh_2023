#include "functions.h"

void import_cars(std::string filename)
{
	std::string car_ID = "1000";
	std::vector<std::string> users_ID = { "933","2","34","523","63" };
	int default_settings[12];
	for (int i = 0; i < 12; i++)
		default_settings[i] = 0;
	cars_DB.push_back(new car(car_ID, users_ID, default_settings));
	car_ID = "2421";
	users_ID = { "2","435","665","31" };
	cars_DB.push_back(new car(car_ID, users_ID, default_settings));
	//std::fstream file;
	//file.open(filename);
	//if (file.good())
	//{
	//	while (!file.eof())
	//	{
	//		std::string car_ID;
	//		std::vector<std::string> users_ID;
	//		std::vector<int> default_user_settings;
	//		std::string temp;
	//		std::stringstream t;
	//		std::getline(file, car_ID, ';');
	//		std::getline(file, temp, ';');
	//		t.str(temp);
	//		//std::cout << temp << std::endl;
	//		while (std::getline(t, temp, ','))
	//			users_ID.push_back(temp);
	//		std::getline(file, temp, '\n');
	//		std::cout << temp << std::endl;
	//		t.str(temp);
	//		std::cout << t.rdbuf() << std::endl;
	//		while (std::getline(t, temp, ',')) {
	//			std::cout << temp << std::endl;
	//			default_user_settings.push_back(stoi(temp));
	//		}
	//		std::cout << default_user_settings.size() << std::endl;
	//		car* c = new car(car_ID, users_ID, default_user_settings);
	//		cars_DB.push_back(c);
	//	}
	//}
}

void import_users(std::string filename)
{
	std::string user_ID = "933";
	std::string car_ID = "1000";
	int car_settings[12];
	for (int i = 0; i < 12; i++)
		car_settings[i] = 1;
	std::vector<car_user_settings*> cs;
	cs.push_back(new car_user_settings(car_ID, car_settings));
	users_DB.push_back(new user(user_ID, cs));
	user_ID = "2";
	cs.clear();
	users_DB.push_back(new user(user_ID, cs));
	//std::fstream file;
	//file.open(filename);
	//if (file.good())
	//{
	//	while (!file.eof())
	//	{
	//		std::string user_ID;
	//		std::vector<car_user_settings*> user_settings;
	//		std::string temp;
	//		std::stringstream tstr;
	//		int i;
	//		std::getline(file, user_ID, ';');
	//		//std::cout << user_ID << std::endl;
	//		std::getline(file, temp, '\n');
	//		tstr.str(temp);
	//		while (std::getline(tstr, temp, ';'))
	//		{
	//			std::string car_ID;
	//			std::vector<int> temp_settings;
	//			std::stringstream t;
	//			t.str(temp);
	//			std::getline(t, car_ID, ',');
	//			while (std::getline(t, temp, ','))
	//				temp_settings.push_back(stoi(temp));
	//			car_user_settings* cu_set = new car_user_settings(car_ID, temp_settings);
	//			user_settings.push_back(cu_set);
	//		}
	//		user* u = new user(user_ID, user_settings);
	//		users_DB.push_back(u);
	//	}
	//}
}

void initialize()
{
    import_cars("cars.txt");
    import_users("users.txt");
}
