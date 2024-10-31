#pragma once



template <class K, class V>
class Dictionary;

/// <summary>
/// Clasa Node pentru reprezentare inlantuita a dictionarului
/// </summary>
/// <typeparam name="K"></typeparam> Key-ul
/// <typeparam name="V"></typeparam> Parametrul stocat

template <class K, class V>
class Node 
{
private:
    K key;
    V value;
    Node<K, V>* next;
public:
    Node(K key, V value) : key(key), value(value) 
    { 
        this->next = nullptr; 
    }
    friend class Dictionary<K, V>;
};