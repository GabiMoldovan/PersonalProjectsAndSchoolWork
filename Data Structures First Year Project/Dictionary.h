#pragma once
#include "Node.h"

/// <summary>
/// TAD Dictionar cu elemente generice (Template <class T> ) cu reprezentare inlantuita
/// </summary>
/// <typeparam name="K"></typeparam> Key-ul cu care accesam elementul returnat
/// <typeparam name="V"></typeparam> Elementul returnat

template<class K, class V>
class Dictionary 
{
private:
    Node<K, V>* first;
    int size;
public:
    Dictionary() 
    {
        this->first = nullptr;
        this->size = 0;
    }
    void add(K key, V value) 
    {
        if (first == nullptr) 
        {
            first = new Node<K, V>(key, value);
            this->size++;
        }
        else 
        {
            Node<K, V>* p = first;
            while (p->next != nullptr && p->key != key) p = p->next;
            if (p->key == key) p->value = value;
            else p->next = new Node<K, V>(key, value), this->size++;
        }
    }
    V get(K key) {
        Node<K, V>* p = first;
        while (p != nullptr) 
        {
            if (p->key == key) return p->value;
            p = p->next;
        }
        return {};
    }
    int get_size()
    {
        return this->size;
    }
    void remove(K key)
    {
        Node<K, V>* p = first;
        Node<K, V>* prev = NULL;
        if (p != NULL && p->key == key)
        {
            first = p->next;
            delete p;
            this->size--;
            return;
        }
        else
        {
            while (p != nullptr && p->key != key)
            {
                prev = p;
                p = p->next;
            }
            if (p == NULL)
                return;
            prev->next = p->next;
            delete p;
            this->size--;
        }
    }
};