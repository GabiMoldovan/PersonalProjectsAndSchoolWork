#include <iostream>
#include "person.h"
#include "chat.h"
#include "Dictionary.h"
#include <fstream>
#include "eveniment.h"
#include "retea.h"

using namespace std;

int main()
{

    /// <summary>
    /// Main-ul programului, de aici se apeleaza meniurile
    /// </summary>
    /// <returns></returns>

    Retea retea;

    while (true)
    {
        char selectMenu;
        cout << "Selectati unul dintre meniuri tastand cifra corespunzatoare acestuia:\n";
        cout << "1 -> Meniul de persoane\n";
        cout << "2 -> Meniul pentru conversatii\n";
        cout << "3 -> Meniul evenimentelor\n";
        cout << "x -> Opreste programul\n";
        cout << "Dati optiunea: ";
        cin >> selectMenu;
        if (selectMenu == '1')
            retea.meniuPersoane();
        else if (selectMenu == '2')
            retea.meniuChat();
        else if (selectMenu == '3')
            retea.meniuEvenimente();
        else if (selectMenu == 'x')
            break;
        else
            cout << "Ati ales o optiune gresita, incercati din nou!\n";
    }
    return 0;
}