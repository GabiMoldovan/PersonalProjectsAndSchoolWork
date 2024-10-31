#pragma once
#include "array.h"
#include "person.h"

/// <summary>
/// Repository pentru stocarea persoanelor
/// Prin intermediul acestuia se adauga si persoane/prieteni in fisiere
/// </summary>

class Repository
{
private:
	Array<Person>* repo = new Array<Person>();
public:
	Repository();
	Repository(Array<Person> lista);
	~Repository();
	void addToRepo(Person& pers);
	Person* get(int ind);
	int size();
	void removeFromRepo(int ind);
	void addPersonToRepoFile(Person& pers);
	void addFriendToRepoFile(Person& pers, const char* id);
};