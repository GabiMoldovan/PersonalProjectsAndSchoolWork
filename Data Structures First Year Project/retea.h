#pragma once
#include "array.h"
#include "person.h"
#include "repository.h"

/// <summary>
/// Clasa Retea in care se asambleaza programul
/// </summary>

class Retea
{
private:
	Repository repo;
public:
	Retea();
	~Retea();
	void meniuPersoane();
	void meniuChat();
	void meniuEvenimente();
};