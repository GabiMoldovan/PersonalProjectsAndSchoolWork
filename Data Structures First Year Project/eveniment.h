#pragma once
#include <string>
#include "person.h"
#include "array.h"

using namespace std;

/// <summary>
/// Header-ul clasei eveniment
/// </summary>

class Eveniment
{
private:
	string descriere;
	Array<Person>* listaInv = new Array<Person>(); // listaInv.get(0) = organizator
public:
	Eveniment();
	Eveniment(string desc, Array<Person> lista);
	~Eveniment();
	string getDesc();
	Array<Person>* getListaInv();
	void setDesc(string desc);
	void setListaInv(Array<Person> lista);
	void adaugaParticipant(Person& pers);
};