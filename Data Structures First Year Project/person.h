#pragma once
#include <iostream>
#include "array.h"

/// <summary>
/// Clasa Persoana in care se stocheaza datele despre un user
/// </summary>

class Person
{
private:
	char* username;
	bool gender; // 0 for boys, 1 for girls
	int age;
	int day; // for birthday
	int month;
	int year;
	Array<Person*> frlist;
	char* id; // we have more persons with the same name, so we are gonna identify an user by their randomly generated id ( unique for each user )
public:
	Person();
	Person(const char* username, bool gender, int age, int day, int month, int year);
	Person(const Person& p);
	~Person();
	void setUsername(const char* username);
	void setGender(bool gender);
	void setAge(int age);
	void setBDay(int day);
	void setBMonth(int month);
	void setBYear(int year);
	void setId(const char* id);
	char* getUsername();
	char* getId();
	bool getGender();
	int getAge();
	int getBDay();
	int getBMonth();
	int getBYear();
	void addFriend(Person* pers);
	bool checkFriendWith(Person* pers);
	void delFriend(Person* pers);
	Person* getFriend(int ind);
	Array<Person*>* getFrList();
	Person& operator=(const Person& p);
};