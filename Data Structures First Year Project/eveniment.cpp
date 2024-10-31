#include "eveniment.h"

Eveniment::Eveniment() 
{
	/// <summary>
	/// Constructor fara parametri
	/// </summary>
	this->descriere = "";
}

Eveniment::Eveniment(string desc, Array<Person> lista)
{
	/// <summary>
	/// Constructor cu parametri
	/// </summary>
	/// <param name="desc"></param>
	/// <param name="lista"></param>
	this->descriere = desc;
	for (int i = 0; i < lista.size(); i++)
		this->listaInv->add(lista.get(i));
}

Eveniment::~Eveniment() {}

string Eveniment::getDesc()
{
	/// <summary>
	/// Metoda care returneaza descrierea unui eveniment
	/// </summary>
	/// <returns></returns>
	return this->descriere;
}

Array<Person>* Eveniment::getListaInv()
{
	/// <summary>
	/// Metoda care returneaza lista de invitati al unui eveniment
	/// </summary>
	/// <returns></returns>
	return this->listaInv;
}

void Eveniment::setDesc(string desc)
{
	/// <summary>
	/// Setter descriere
	/// </summary>
	/// <param name="desc"></param>
	this->descriere = desc;
}

void Eveniment::setListaInv(Array<Person> lista)
{
	/// <summary>
	/// Setter lista invitati
	/// </summary>
	/// <param name="lista"></param>
	for (int i = 0; i < lista.size(); i++)
		this->listaInv->set(i, lista.get(i));
}

void Eveniment::adaugaParticipant(Person& pers)
{
	/// <summary>
	/// Adaugare participant la eveniment
	/// </summary>
	/// <param name="pers"></param>
	this->listaInv->add(pers);
}
