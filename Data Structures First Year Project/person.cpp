#include "person.h"
#include <random>
#include <cstring>

using namespace std;

/*

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
	char* getUsername();
	char* getId();
	bool getGender();
	int getBDay();
	int getBMonth();
	int getBYear();
	void addFriend(Person* pers);
	bool checkFriendWith(Person* pers);
	void delFriend(Person* pers);
	Person* getFriend(int ind);
	Array<Person*> getFrList();
	Person& operator=(const Person& p);
};

*/

Person::Person()
{
	/// <summary>
	/// Constructorul fara parametri
	/// </summary>
	this->username = NULL;
	this->gender = 0;
	this->age = 0;
	this->day = 0;
	this->month = 0;
	this->year = 0;
	//srand(time(NULL));
	char alphabet[26] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g',
						  'h', 'i', 'j', 'k', 'l', 'm', 'n',
						  'o', 'p', 'q', 'r', 's', 't', 'u',
						  'v', 'w', 'x', 'y', 'z' };
	char res[16] = "";
	for (int i = 0; i < 15; i++)
		res[i] = alphabet[rand() % 26];
	this->id = new char[strlen(res) + 1];
	strcpy_s(this->id, strlen(res) + 1, res);
	this->frlist = {};
}

Person::Person(const char* username, bool gender, int age, int day, int month, int year)
{
	/// <summary>
	/// Constructorul cu parametri
	/// </summary>
	/// <param name="username"></param> numele persoanei
	/// <param name="gender"></param> sexul persoanei
	/// <param name="age"></param> varsta persoanei
	/// <param name="day"></param> ziua nasterii
	/// <param name="month"></param> luna nasterii
	/// <param name="year"></param> anul nasterii
	this->username = new char[strlen(username) + 1];
	strcpy_s(this->username, strlen(username) + 1, username);
	this->gender = gender;
	this->age = age;
	this->day = day;
	this->month = month;
	this->year = year;
	//srand(time(NULL));
	char alphabet[26] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g',
						  'h', 'i', 'j', 'k', 'l', 'm', 'n',
						  'o', 'p', 'q', 'r', 's', 't', 'u',
						  'v', 'w', 'x', 'y', 'z' };
	char res[16] = "";
	for (int i = 0; i < 15; i++)
		res[i] = alphabet[rand() % 26];
	this->id = new char[strlen(res) + 1];
	strcpy_s(this->id, strlen(res) + 1, res);
}

Array<Person*>* Person::getFrList()
{
	/// <summary>
	/// Returneaza lista de prieteni a unui utilizator
	/// </summary>
	/// <returns></returns>
	return &this->frlist;
}

Person::Person(const Person& p)
{
	/// <summary>
	/// Constructorul care copiaza datele unei persoane
	/// </summary>
	/// <param name="p"></param>
	this->username = new char[strlen(p.username) + 1];
	strcpy_s(this->username, strlen(p.username) + 1, p.username);
	this->gender = p.gender;
	this->age = p.age;
	this->day = p.day;
	this->month = p.month;
	this->year = p.year;
	this->id = new char[strlen(p.id) + 1];
	strcpy_s(this->id, strlen(p.id) + 1, p.id);
}

Person::~Person()
{
	/// <summary>
	/// Destructorul
	/// </summary>
	if (this->username)
	{
		delete[] this->username;
		this->username = NULL;
	}
	if (this->id)
	{
		delete[] this->id;
		this->id = NULL;
	}
}

void Person::setUsername(const char* username)
{
	/// <summary>
	/// Setter pentru nume
	/// </summary>
	/// <param name="username"></param>
	if (this->username)
	{
		delete[] this->username;
		this->username = NULL;
	}
	this->username = new char[strlen(username) + 1];
	strcpy_s(this->username, strlen(username) + 1, username);
}

void Person::setGender(bool gender)
{
	/// <summary>
	/// Setter pentru sex
	/// </summary>
	/// <param name="gender"></param>
	this->gender = gender;
}

void Person::setAge(int age)
{
	/// <summary>
	/// Setter pentru varsta
	/// </summary>
	/// <param name="age"></param>
	this->age = age;
}

void Person::setBDay(int day)
{
	/// <summary>
	/// Setter pentru ziua nasterii
	/// </summary>
	/// <param name="day"></param>
	this->day = day;
}

void Person::setBMonth(int month)
{
	/// <summary>
	/// Setter pentru luna nasterii
	/// </summary>
	/// <param name="month"></param>
	this->month = month;
}

void Person::setBYear(int year)
{
	/// <summary>
	/// Setter pentru anul nasterii
	/// </summary>
	/// <param name="year"></param>
	this->year = year;
}

void Person::setId(const char* id)
{
	/// <summary>
	/// Setter pentru ID-ul unic al unei persoane ( folosit cand dam load la useri )
	/// </summary>
	/// <param name="id"></param>
	if (this->id)
	{
		delete[] this->id;
		this->id = NULL;
	}
	this->id = new char[strlen(id) + 1];
	strcpy_s(this->id, strlen(id) + 1, id);
}

char* Person::getUsername()
{
	/// <summary>
	/// Getter nume
	/// </summary>
	/// <returns></returns>
	return this->username;
}

char* Person::getId()
{
	/// <summary>
	/// Getter id
	/// </summary>
	/// <returns></returns>
	return this->id;
}

bool Person::getGender()
{
	/// <summary>
	/// Getter gender
	/// </summary>
	/// <returns></returns>
	return this->gender;
}

int Person::getAge()
{
	/// <summary>
	/// Getter varsta
	/// </summary>
	/// <returns></returns>
	return this->age;
}

int Person::getBDay()
{
	/// <summary>
	/// Getter ziua nasterii
	/// </summary>
	/// <returns></returns>
	return this->day;
}

int Person::getBMonth()
{
	/// <summary>
	/// Getter luna nasterii
	/// </summary>
	/// <returns></returns>
	return this->month;
}

int Person::getBYear()
{
	/// <summary>
	/// Getter anul nasterii
	/// </summary>
	/// <returns></returns>
	return this->year;
}


bool Person::checkFriendWith(Person* pers)
{
	/// <summary>
	/// Metoda care verifica daca pers este in lista de prieteni al unui user
	/// </summary>
	/// <param name="pers"></param>
	/// <returns></returns>
	for (int i = 0; i < this->frlist.size(); i++)
		if (strcmp(pers->getId(), this->frlist.get(i)->getId()) == 0) return true;
	return false;
}

void Person::addFriend(Person* pers)
{
	/// <summary>
	/// Metoda care adauga o persoana in lista de prieteni al altei persoane
	/// </summary>
	/// <param name="pers"></param>
	if (this->checkFriendWith(pers) == false)
	{
		this->frlist.add(pers);
	}
}

void Person::delFriend(Person* pers)
{
	/// <summary>
	/// Metoda care sterge o persoana din lista de prieteni al unui user
	/// </summary>
	/// <param name="pers"></param>
	if (this->checkFriendWith(pers) && this->getFrList()->size()>1)
	{
		int ind = -1;
		for (int i = 0; i < this->frlist.size() && ind == -1; i++)
			if (pers->getId() == this->frlist.get(i)->getId()) ind = i;
		for (int i = ind; i < this->frlist.size() - 1; i++)
			this->frlist.get(i) = this->frlist.get(i + 1);
	}
}

Person* Person::getFriend(int ind)
{
	/// <summary>
	/// Metoda care returneaza prietenul de pe pozitia ind
	/// </summary>
	/// <param name="ind"></param>
	/// <returns></returns>
	return this->frlist.get(ind);
}


Person& Person::operator=(const Person& p)
{
	/// <summary>
	/// Supraincarcare operator = ( face ca o persoana sa primeasca atributele altei persoane )
	/// </summary>
	/// <param name="p"></param>
	/// <returns></returns>
	this->setUsername(p.username);
	this->setAge(p.age);
	this->setBDay(p.day);
	this->setBMonth(p.month);
	this->setBYear(p.year);
	this->setGender(p.gender);
	if (this->id)
	{
		delete[] this->id;
		this->id = NULL;
	}
	this->id = new char[strlen(p.id) + 1];
	strcpy_s(this->id, strlen(p.id) + 1, p.id);
	return *this;
}