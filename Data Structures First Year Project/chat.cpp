#include "chat.h"
#include <fstream>
#include <iostream>
#include <cstring>

using namespace std;

/*

class Chat
{
private:
	char* id1;
	char* id2;
	char* filename;
public:
	Chat();
	Chat(const char* id1, const char* id2);
	~Chat();
	void writeMessageinFile(const char* username, const char* msg);
	void printMessagesfromFile();
	const char* generateFilename(const char* id1, const char* id2);
};

*/

Chat::Chat()
{
	/// <summary>
	/// Constructor fara parametri
	/// </summary>
	this->id1 = NULL;
	this->id2 = NULL;
	this->filename = NULL;
}

Chat::Chat(const char* id1, const char* id2)
{
	/// <summary>
	/// Constructor cu parametri
	/// Construieste automat fisierul de chat intre doua persoane pe baza id-urilor
	/// Acesta o sa fie de forma id1-id2.txt
	/// </summary>
	/// <param name="id1"></param>
	/// <param name="id2"></param>
	if (this->id1)
	{
		delete[] this->id1;
		this->id1 = NULL;
	}
	if (this->id2)
	{
		delete[] this->id2;
		this->id2 = NULL;
	}
	this->id1 = new char[strlen(id1) + 1];
	this->id2 = new char[strlen(id2) + 1];
	strcpy_s(this->id1, strlen(id1) + 1, id1);
	strcpy_s(this->id2, strlen(id2) + 1, id2);

	char* file = new char[strlen(id1) + strlen(id2) + 1];
	strcpy_s(file, strlen(id1) + 1, id1);
	int len = strlen(file);
	file[strlen(file)] = '-';
	file[len + 1] = '\0';
	char* nr2 = new char[strlen(id2) + 1];
	strcpy_s(nr2, strlen(id2) + 1, id2);
	for (int i = strlen(file); i < strlen(file) + strlen(nr2); i++)
		file[i] = nr2[i - strlen(nr2)];
	this->filename = file;
}

Chat::~Chat()
{
	/// <summary>
	/// Destructor
	/// </summary>
	if (this->id1)
	{
		delete[] this->id1;
		this->id1 = NULL;
	}
	if (this->id2)
	{
		delete[] this->id2;
		this->id2 = NULL;
	}
}

void Chat::writeMessageinFile(const char* username, const char* msg)
{
	/// <summary>
	/// Metoda care adauga un mesaj nou in chatul dintre doua persoane
	/// </summary>
	/// <param name="username"></param> numele utilizatorului care trimite mesajul
	/// <param name="msg"></param> mesajul
	ofstream fout("./mesaje/" + string(filename), ios::app);  // ios:app = when we write a message in the file, the past messages don't get deleted
	fout << username << ": " << msg<<"\n";
	fout.close();
}

void Chat::printMessagesfromFile()
{
	/// <summary>
	/// Metoda care afiseaza toate mesajele din chat
	/// </summary>
	char mesaj[999] = "";
	ifstream fin("./mesaje/" + string(filename));
	if (fin.is_open() == true)
		while (!fin.eof())
		{
			fin.getline(mesaj, 999);
			cout << mesaj << "\n";
		}
	else cout << "Aceste persoane nu au conversat inainte!\n";
	fin.close();
}

const char* Chat::getFilename()
{
	/// <summary>
	/// Metoda care returneaza numele fisierului in care sunt stocate conversatiile
	/// </summary>
	/// <returns></returns>
	return this->filename;
}

void Chat::clearFile()
{
	/// <summary>
	/// Metoda care sterge conversatiile
	/// </summary>
	ofstream ofs;
	ofs.open("./mesaje/" + string(filename), ofstream::out | ofstream::trunc);
	ofs.close();
}
