#pragma once

/// <summary>
/// Header-ul clasei Chat
/// </summary>

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
	const char* getFilename();
	void clearFile();
};