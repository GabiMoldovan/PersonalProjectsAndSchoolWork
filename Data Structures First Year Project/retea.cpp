#include "retea.h"
#include "chat.h"
#include "eveniment.h"
#include <fstream>
#include <iostream>
#include <cstring>
#include "Dictionary.h"

using namespace std;

Retea::Retea()
{
	// load users
	ifstream fin("./users/" + string("userinfo.in"));
	string nume, prenume, id;
	bool gender;
	int age, day, month, year;
	while (fin >> nume >> prenume >> gender >> age >> day >> month >> year >> id)
	{
		string numefinal = nume + " " + prenume;
		char* numefinaltochar = new char[numefinal.length() + 1];
		strcpy_s(numefinaltochar, numefinal.length() + 1, numefinal.c_str());
		numefinaltochar[strlen(numefinaltochar)] = '\0';
		Person asd(numefinaltochar, gender, age, day, month, year);
		char* idToChar = new char[id.length() + 1];
		strcpy_s(idToChar, id.length() + 1, id.c_str());
		asd.setId(idToChar);
		repo.addToRepo(asd);
	}
	fin.close();

	for (int i = 0; i < this->repo.size(); i++)
	{
		string filename = string(this->repo.get(i)->getId());
		ifstream fin("./friendship/" + string(filename + ".in"));
		int idUser = -1;
		char* filenameToChar = new char[filename.length() + 1];
		strcpy_s(filenameToChar, filename.length() + 1, filename.c_str());
		for (int j = 0; j < this->repo.size() && idUser == -1; j++)
			if (strcmp(this->repo.get(j)->getId(), filenameToChar) == 0) idUser = j;
		string user;
		while (fin >> user)
		{
			char* userToChar = new char[user.length() + 1];
			strcpy_s(userToChar, user.length() + 1, user.c_str());
			userToChar[strlen(userToChar)] = '\0';
			if (strcmp(userToChar, "") != 0)
				for (int j = 0; j < this->repo.size(); j++)
					if (strcmp(this->repo.get(j)->getId(), userToChar) == 0)
					{
						Person* pers = this->repo.get(j);
						this->repo.get(idUser)->addFriend(pers);
						break;
					}
			//cout << repo.get(idUser).getFrList().size() << " ";
		}
		fin.close();
	}
	
}

Retea::~Retea() {}

void Retea::meniuPersoane()
{
	while (true) // exception!
	{
		char task;
		cout << "Selectati una dintre optiuni tastand cifra corespunzatoare:\n";
		cout << "1. Afiseaza toate persoanele din retea\n";
		cout << "2. Adauga o persoana noua\n";
		cout << "3. Afiseaza datele despre o persoana\n";
		cout << "4. Afiseaza toti prietenii unei persoane\n";
		cout << "5. Afiseaza datele prietenilor unei persoane\n";
		cout << "6. Modifica datele unei persoane\n";
		cout << "7. Adauga un prieten pentru o persoana\n";
		cout << "8. Sterge un prieten al unei persoane\n";
		cout << "x. Paraseste acest meniu\n";
		cout << "Dati optiunea: ";
		cin >> task;
		if (task == '1')
		{
			for (int i = 0; i < repo.size(); i++)
				cout << i << ". " << repo.get(i)->getUsername() << "\n";
		}
		else if (task == '2')
		{
			/// <summary>
			/// Adauga o persoana in repository si in fisierul in care se stocheaza persoanele
			/// </summary>
			string newUsername, nume, prenume;
			int newDay, newMonth, newYear, newAge, newGender;
			cout << "Dati nume: ";
			cin >> nume;
			cout << "Dati prenume: ";
			cin >> prenume;
			newUsername = nume + " " + prenume;
			cout << "Dati genul (0 - masculin, 1- feminin): ";
			cin >> newGender;
			while (newGender > 1 && newGender < 0)
			{
				cout << "Ati introdus un numar gresit, incarcati din nou(0 - masculin, 1- feminin): ";
				cin >> newGender;
			}
			cout << "Dati ziua nasterii: ";
			cin >> newDay;
			while (newDay < 0 || newDay>31)
			{
				cout << "Ati introdus un numar gresit, incercati din nou: ";
				cin >> newDay;
			}
			cout << "Dati luna nasterii: ";
			cin >> newMonth;
			while (newMonth < 0 || newMonth>12)
			{
				cout << "Ati introdus un numar gresit, incercati din nou: ";
				cin >> newMonth;
			}
			cout << "Dati anul nasterii: ";
			cin >> newYear;
			cout << "Dati varsta: ";
			cin >> newAge;
			while (newAge != 2022 - newYear && newAge != 2021 - newYear && newAge != 2023 - newYear)
			{
				cout << "Varsta trebuie sa fie cu o unitate mai mica/mare decat anul nasterii, incercati din nou: ";
				cin >> newAge;
			}
			char* newUsernameToChar = new char[newUsername.length() + 1];
			strcpy_s(newUsernameToChar, newUsername.length() + 1, newUsername.c_str());
			Person toAdd(newUsernameToChar, newGender, newAge, newDay, newMonth, newYear);
			repo.addToRepo(toAdd);
			repo.addPersonToRepoFile(toAdd);
		}
		else if (task == '3')
		{
			/// <summary>
			/// Afiseaza datele despre o persoana a carui indice este citit de la tastatura
			/// </summary>
			int ind;
			cout << "Dati indicele persoanei: ";
			cin >> ind;
			while (ind < 0 || ind >= repo.size())
			{
				cout << "Ati introdus un indice gresit, incercati din nou: ";
				cin >> ind;
			}
			cout << "Numele: " << repo.get(ind)->getUsername() << "\n";
			cout << "Genul: " << (repo.get(ind)->getGender() == 1 ? "Masculin" : "Feminin") << "\n";
			cout << "Varsta: " << repo.get(ind)->getAge() << "\n";
			cout << "Data nasterii (an.luna.zi): " << repo.get(ind)->getBYear() << '.' << repo.get(ind)->getBMonth() << '.' << repo.get(ind)->getBDay() << "\n";
		}
		else if (task == '4')
		{
			/// <summary>
			/// Afiseaza toti prietenii unei persoane
			/// </summary>
			int id;
			cout << "Dati indicele persoanei: ";
			cin >> id;
			while (id < 0 || id >= repo.size())
			{
				cout << "Ati introdus un indice gresit, incercati din nou: ";
				cin >> id;
			}
			if (repo.get(id)->getFrList()->size() == 0)
				cout << "Aceasta persoana nu are prieteni\n";
			for (int i = 0; i < repo.get(id)->getFrList()->size(); i++)
				cout << i << ". " << repo.get(id)->getFriend(i)->getUsername() << "\n";
		}
		else if (task == '5')
		{
			/// <summary>
			/// Afiseaza datele prietenilor unei persoane a carui indice este citit de la tastatura
			/// </summary>
			int id;
			cout << "Dati indicele persoanei: ";
			cin >> id;
			while (id < 0 || id >= repo.size())
			{
				cout << "Ati introdus un indice gresit, incercati din nou: ";
				cin >> id;
			}
			for (int i = 0; i < repo.get(id)->getFrList()->size(); i++)
			{
				cout << "Numele: " << repo.get(id)->getFrList()->get(i)->getUsername() << "\n";
				cout << "Genul: " << (repo.get(id)->getFrList()->get(i)->getGender() == 1 ? "Masculin" : "Feminin") << "\n";
				cout << "Varsta: " << repo.get(id)->getFrList()->get(i)->getAge() << "\n";
				cout << "Data nasterii (an.luna.zi): " << repo.get(id)->getFrList()->get(i)->getBYear() << '.' << repo.get(id)->getFrList()->get(i)->getBMonth() << '.' << repo.get(id)->getFrList()->get(i)->getBDay() << "\n\n";
			}
		}
		else if (task == '6')
		{
			/// <summary>
			/// Modifica datele unei persoane
			/// </summary>
			int id;
			cout << "Dati indicele persoanei: ";
			cin >> id;
			while (id < 0 || id >= repo.size())
			{
				cout << "Ati introdus un indice gresit, incercati din nou: ";
				cin >> id;
			}
			string newUsername;
			int newDay, newMonth, newYear, newAge, newGender;
			cout << "Dati noul nume: ";
			cin >> newUsername;
			cout << "Dati noul gen(0 - masculin, 1- feminin): ";
			cin >> newGender;
			while (newGender > 1 && newGender < 0)
			{
				cout << "Ati introdus un numar gresit, incercati din nou(0 - masculin, 1- feminin): ";
				cin >> newGender;
			}
			cout << "Dati noua zi a nasterii: ";
			cin >> newDay;
			while (newDay < 0 || newDay>31)
			{
				cout << "Ati introdus o zi gresita, incercati din nou: ";
				cin >> newDay;
			}
			cout << "Dati noua luna a nasterii: ";
			cin >> newMonth;
			while (newMonth < 0 || newMonth>12)
			{
				cout << "Ati introdus o luna gresita(1-12), incercati din nou: ";
				cin >> newMonth;
			}
			cout << "Dati noul an al nasterii: ";
			cin >> newYear;
			cout << "Dati noua varsta: ";
			cin >> newAge;
			while (newAge != 2022 - newYear && newAge != 2021 - newYear && newAge != 2023 - newYear)
			{
				cout << "Varsta trebuie sa fie cu o unitate mai mica/mare decat anul nasterii, incercati din nou: ";
				cin >> newAge;
			}
			char* newUsernameToChar = new char[newUsername.length() + 1];
			strcpy_s(newUsernameToChar, newUsername.length() + 1, newUsername.c_str());
			repo.get(id)->setUsername(newUsernameToChar);
			repo.get(id)->setAge(newAge);
			repo.get(id)->setBDay(newDay);
			repo.get(id)->setBMonth(newMonth);
			repo.get(id)->setBYear(newYear);
			repo.get(id)->setGender(newGender);
		}
		else if (task == '7')
		{
			/// <summary>
			/// Adauga o persoana in lista de prieteni al altei persoane
			/// </summary>
			int id;
			cout << "Dati indicele persoanei: ";
			cin >> id;
			while (id < 0 || id >= repo.size())
			{
				cout << "Ati introdus un indice gresit, incercati din nou: ";
				cin >> id;
			}
			int id2;
			cout << "Dati indicele persoanei de adaugat la prieteni: ";
			cin >> id2;
			while ((id2 < 0 || id2 >= repo.size()) || id == id2)
			{
				cout << "Ati introdus un indice gresit, incercati din nou: ";
				cin >> id2;
			}
			bool ok = true;
			Person* asdf = repo.get(id2);
			for (int i = 0; i < repo.get(id2)->getFrList()->size(); i++)
				if (strcmp(asdf->getId(), repo.get(i)->getId()) == 0)
				{
					ok = false;
					cout << "Aceasta persoana se afla deja in lista de prieteni a utilizatorului!\n";
					break;
				}
			if (ok)
			{
				repo.get(id)->addFriend(asdf);
				repo.addFriendToRepoFile(*repo.get(id), asdf->getId());
				repo.get(id2)->addFriend(repo.get(id));
				repo.addFriendToRepoFile(*repo.get(id2), repo.get(id)->getId());
			}
		}
		else if (task == '8')
		{
			/// <summary>
			/// Sterge un prieten din lista de prieteni a unei persoane
			/// </summary>
			int id;
			cout << "Dati indicele persoanei: ";
			cin >> id;
			while (id < 0 || id >= repo.size())
			{
				cout << "Ati introdus un indice gresit, incercati din nou: ";
				cin >> id;
			}
			int id2;
			cout << "Dati indicele persoanei pe care doriti sa o stergeti: ";
			cin >> id2;
			while (id2 < 0 || id2 >= repo.size())
			{
				cout << "Ati introdus un indice gresit, incercati din nou: ";
				cin >> id2;
			}
			repo.get(id)->getFrList()->remove(id2);
			repo.get(id2)->getFrList()->remove(id);
		}
		else if (task == 'x')
			break;
	}
}

void Retea::meniuChat()
{
	while (true) // exception!
	{
		char task;
		cout << "Selectati una dintre optiuni tastand cifra corespunzatoare:\n";
		cout << "1. Afiseaza toate persoanele din retea\n";
		cout << "2. Afiseaza conversatiile dintre doua persoane\n";
		cout << "3. Acceseaza conversatia dintre doua persoane\n";
		cout << "4. Sterge conversatiile dintre doua persoane\n";
		cout << "x. Paraseste acest meniu\n";
		cout << "Dati optiunea: ";
		cin >> task;
		if (task == '1')
		{
			/// <summary>
			/// Afiseaza Userii din retea
			/// </summary>
			for (int i = 0; i < repo.size(); i++)
				cout << i << ". " << repo.get(i)->getUsername() << "    ID = " << repo.get(i)->getId() << "\n";
		}
		else if (task == '2')
		{
			/// <summary>
			/// Afiseaza conversatiile dintre doi useri
			/// </summary>
			int ind1, ind2;
			cout << "Dati indicele primei persoane: ";
			cin >> ind1;
			while (ind1 < 0 || ind1 >= repo.size())
			{
				cout << "Nu ati introdus un indice bun, incercati din nou: ";
				cin >> ind1;
			}
			cout << "Dati indicele persoanei a doua: ";
			cin >> ind2;
			while (ind2 < 0 || ind2 >= repo.size())
			{
				cout << "Nu ati introdus un indice bun, incercati din nou: ";
				cin >> ind2;
			}
			Chat chat(repo.get(ind1)->getId(), repo.get(ind2)->getId());
			chat.printMessagesfromFile();
		}
		else if (task == '3')
		{
			/// <summary>
			/// Adauga mesaje noi in chat-ul dintre doi useri
			/// </summary>
			int ind1, ind2;
			cout << "Dati indicele primei persoane: ";
			cin >> ind1;
			while (ind1 < 0 || ind1 >= repo.size())
			{
				cout << "Nu ati introdus un indice bun, incercati din nou: ";
				cin >> ind1;
			}
			cout << "Dati indicele persoanei a doua: ";
			cin >> ind2;
			while (ind2 < 0 || ind2 >= repo.size())
			{
				cout << "Nu ati introdus un indice bun, incercati din nou: ";
				cin >> ind2;
			}
			Chat chat(repo.get(ind1)->getId(), repo.get(ind2)->getId());
			while (true)
			{
				char opt;
				cout << "Selectati una dintre optiuni:\n";
				cout << "1. Adauga un mesaj in chat din partea primei persoane\n";
				cout << "2. Adauga un mesaj in chat din partea persoanei a doua\n";
				cout << "x. Paraseste meniul\n";
				cout << "Dati optiunea: ";
				cin >> opt;
				if (opt == '1')
				{
					/// <summary>
					/// Adauga mesaj din partea primului user
					/// </summary>
					string msg;
					cout << "Dati mesajul: ";
					
					cin.ignore();

					getline(cin, msg);
				
					chat.writeMessageinFile(repo.get(ind1)->getUsername(), msg.c_str());
				}
				else if (opt == '2')
				{
					/// <summary>
					/// Adauga mesaj din partea celui de-al doilea user
					/// </summary>
					string msg;
					cout << "Dati mesajul: ";

					cin.ignore();
					
					getline(cin, msg);

					chat.writeMessageinFile(repo.get(ind2)->getUsername(), msg.c_str());
				}
				else if (opt == 'x')
					break;
			}
		}
		else if (task == '4')
		{
			/// <summary>
			/// Sterge conversatiile dintre doi useri
			/// </summary>
			int ind1, ind2;
			cout << "Dati indicele primei persoane: ";
			cin >> ind1;
			while (ind1 < 0 || ind1 >= repo.size())
			{
				cout << "Nu ati introdus un indice bun, incercati din nou: ";
				cin >> ind1;
			}
			cout << "Dati indicele persoanei a doua: ";
			cin >> ind2;
			while (ind2 < 0 || ind2 >= repo.size())
			{
				cout << "Nu ati introdus un indice bun, incercati din nou: ";
				cin >> ind2;
			}
			Chat chat(repo.get(ind1)->getId(), repo.get(ind2)->getId());
			chat.clearFile();
		}
		else if (task == 'x')
			break;
	}
}

void Retea::meniuEvenimente()
{
	/*
	
	Dictionary<int, string> d;
	d.add(1, "Dan");
	d.add(2, "Ioan");
	d.add(3, "Daniel");
	d.add(4, "Mara");
	cout << d.get(3)<<" ";
	d.remove(4);
	cout << d.get_size()<<" "<<d.get(4);
	
	Eveniment test;
	test.adaugaParticipant(guy2);
	test.setDesc("testetst");
	cout << test.getDesc();

	*/

	Eveniment* test = new Eveniment();
	//test.adaugaParticipant(repo.get(0));
	//test.setDesc("testetst");
	//cout << test.getDesc();

	Dictionary<string, Eveniment*> events;
	Array<string> titluri;

	while (true) // exception!
	{
		char task;
		cout << "Selectati una dintre optiuni tastand cifra corespunzatoare:\n";
		cout << "1. Creaza un eveniment\n";
		cout << "2. Afiseaza titlurile evenimentelor\n";
		cout << "3. Afiseaza detaliile despre un eveniment\n";
		cout << "4. Afiseaza lista participantilor la un eveniment\n";
		cout << "5. Inscrie o persoana la un eveniment\n";
		cout << "6. Afiseaza prietenii unei persoane care participa la un eveniment\n";
		cout << "x. Paraseste acest meniu\n";
		cout << "Dati optiunea: ";
		cin >> task;
		if (task == '1')
		{
			/// <summary>
			/// Creeaza un eveniment
			/// </summary>
			string titlu;
			cout << "Dati titlul evenimentului: ";
			cin >> titlu;
			titluri.add(titlu);
			cout << "\n";
			for (int i = 0; i < repo.size(); i++)
				cout << i << ". " << repo.get(i)->getUsername() << "\n";
			int indOrganiz;
			cout << "Dati indicele persoanei care organizeaza evenimentul: ";
			cin >> indOrganiz;
			while (indOrganiz < 0 || indOrganiz >= repo.size())
			{
				cout << "Ati introdus un indice incorect, incercati din nou: ";
				cin >> indOrganiz;
			}
			string descriere;
			cout << "Setati o descriere a evenimentului: ";
			cin >> descriere;
			test->adaugaParticipant(*repo.get(indOrganiz));
			test->setDesc(descriere);
			events.add(titlu, test);

		}
		
		else if (task == '2')
		{
			/// <summary>
			/// Afiseaza titlurile evenimentelor
			/// </summary>
			for (int i = 0; i < titluri.size(); i++)
				cout << i << ". " << titluri.get(i) << "\n";
		}
		else if (task == '3')
		{
			/// <summary>
			/// Afiseaza detaliile despre un eveniment al carui indice este citit de la tastatura
			/// </summary>
			int ind;
			cout << "Dati indicele evenimentului: ";
			cin >> ind;
			while (ind < 0 || ind >= titluri.size())
			{
				cout << "Ati introdus un indice incorect, incercati din nou: ";
				cin >> ind;
			}
			cout << "Titlu: " << titluri.get(ind) << "\n";
			cout << "Descriere: " << events.get(titluri.get(ind))->getDesc() << "\n";
			cout << "Numar de invitati: " << events.get(titluri.get(ind))->getListaInv()->size()<<"\n";
		}
		else if (task == '4')
		{
			/// <summary>
			/// Afiseaza lista participantilor la un eveniment al carui indice este citit de la tastatura
			/// </summary>
			int ind;
			cout << "Dati indicele evenimentului: ";
			cin >> ind;
			while (ind < 0 || ind >= titluri.size())
			{
				cout << "Ati introdus un indice incorect, incercati din nou: ";
				cin >> ind;
			}
			Array<Person>* listaInv = events.get(titluri.get(ind))->getListaInv();
			cout << "Organizator: ";
			for (int i = 0; i < listaInv->size(); i++)
				cout << i << ". " << listaInv->get(i).getUsername() << "\n";
		}
		else if (task == '5')
		{
			/// <summary>
			/// Adauga un participant la un eveniment
			/// </summary>
			int ind;
			cout << "Dati indicele persoanei: ";
			cin >> ind;
			while (ind < 0 || ind >= repo.size())
			{
				cout << "Ati dat un indice incorect, incercati din nou: ";
				cin >> ind;
			}
			int indEvent;
			cout << "Dati indicele evenimentului: ";
			cin >> indEvent;
			while (indEvent < 0 || indEvent >= titluri.size())
			{
				cout << "Ati introdus un indice incorect, incercati din nou: ";
				cin >> indEvent;
			}
			bool ok = true;
			for (int i = 0; i < events.get(titluri.get(indEvent))->getListaInv()->size(); i++)
				if (strcmp(repo.get(ind)->getId(), events.get(titluri.get(indEvent))->getListaInv()->get(i).getId()) == 0)
				{
					ok = false;
					break;
				}
			if (ok == true) events.get(titluri.get(indEvent))->adaugaParticipant(*repo.get(ind));
			else cout << "Aceasta persoana participa deja la acest eveniment\n";
		}
		else if (task == '6')
		{
			/// <summary>
			/// Afiseaza prietenii unui utilizator care participa la un eveniment
			/// </summary>
			int indEvent;
			cout << "Dati indicele evenimentului: ";
			cin >> indEvent;
			while (indEvent < 0 || indEvent >= titluri.size())
			{
				cout << "Ati introdus un indice incorect, incercati din nou: ";
				cin >> indEvent;
			}
			int idPers;
			cout << "Dati indicele persoanei: ";
			cin >> idPers;
			while (idPers < 0 || idPers >= repo.size())
			{
				cout << "Ati introdus un indice incorect, incercati din nou: ";
				cin >> idPers;
			}
			int poz = 0;
			for (int i = 0; i < events.get(titluri.get(indEvent))->getListaInv()->size(); i++)
				if (repo.get(idPers)->checkFriendWith(&events.get(titluri.get(indEvent))->getListaInv()->get(i)))
					cout << poz++ << ". " << repo.get(idPers)->getFrList()->get(i)->getUsername() << "\n";
		}
		else if (task == 'x')
			break;
	}
}