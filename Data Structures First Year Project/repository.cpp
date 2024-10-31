#include "repository.h"
#include <fstream>
#include <iostream>

using namespace std;

Repository::Repository() {}

Repository::Repository(Array<Person> lista)
{
	/// <summary>
	/// Constructorul care atribuie repository-ului o lista transmisa prin parametru
	/// </summary>
	/// <param name="lista"></param>
	for (int i = 0; i < lista.size(); i++)
		this->repo->add(lista.get(i));
}

Repository::~Repository() {}

void Repository::addToRepo(Person& pers)
{
	/// <summary>
	/// Metoda care adauga o persoana in repository
	/// </summary>
	/// <param name="pers"></param>
	this->repo->add(pers);
}

Person* Repository::get(int ind)
{
	/// <summary>
	/// Metoda care returneaza persoana aflata pe pozitia "ind" din repository
	/// </summary>
	/// <param name="ind"></param>
	/// <returns></returns>
	return &this->repo->get(ind);
}

int Repository::size()
{
	/// <summary>
	/// Metoda care returneaza size-ul repository-ului
	/// </summary>
	/// <returns></returns>
	return this->repo->size();
}

void Repository::removeFromRepo(int ind)
{
	/// <summary>
	/// Metoda care sterge un element aflat pe o pozitie din repository
	/// </summary>
	/// <param name="ind"></param>
	this->repo->remove(ind);
}


void Repository::addPersonToRepoFile(Person& pers)
{
	/// <summary>
	/// Metoda care adauga datele unei persoane in fisierul de stocare al persoanelor
	/// Aceste persoane vor primi load la inceperea programului
	/// </summary>
	/// <param name="pers"></param>
	ofstream fout("./users/" + string("userinfo.in"), ios::app);  // ios:app = when we write a message in the file, the past messages don't get deleted
	fout << "\n";
	fout << pers.getUsername() << " " << pers.getGender() << " " << pers.getAge() << " " << pers.getBDay() << " " << pers.getBMonth() << " " << pers.getBYear() << " " << pers.getId();
	fout.close();
}

void Repository::addFriendToRepoFile(Person& pers, const char* id)
{
	/// <summary>
	/// Metoda care adauga un prieten in fisierul de prieteni al utilizatorului pers
	/// </summary>
	/// <param name="pers"></param>
	/// <param name="id"></param>
	string filename = string(pers.getId());
	ofstream fout("./friendship/" + string(filename + ".in"), ios::app);
	fout << id << " ";
	fout.close();
}