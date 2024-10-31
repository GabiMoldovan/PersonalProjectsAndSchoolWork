#pragma once

/// <summary>
/// TAD Lista cu elemente generice (Template<class T> ) cu reprezentare pe array
/// </summary>
/// <typeparam name="T"></typeparam> Tipul elementului

template <typename T>
class Array
{
private:
	int maxSize;
	int currSize;
	T* arr;
public:
	Array()
	{
		this->maxSize = 500;
		this->currSize = 0;
		this->arr = new T[this->maxSize];
	}
	~Array()
	{
		delete[] this->arr;
	}
	int size()
	{
		return this->currSize;
	}
	void add(T& elem)
	{
		if (this->currSize+1 >= this->maxSize)
			this->maxSize++;
		this->arr[this->currSize++] = elem;
	}
	T& get(int ind)
	{

		if (!(ind >= 0 && ind < currSize))
			throw"Index not found!";
		return this->arr[ind];
	}
	void set(int ind, const T& elem)
	{
		if (!(ind >= 0 && ind < currSize))
			throw"Index not found!";
		this->arr[ind] = elem;
	}
	void remove(int ind)
	{
		if (!(ind >= 0 && ind < currSize))
			throw"Index not found!";
		if (this->currSize == 1 && ind == 0)
		{
			this->arr = new T;
		}
		for (int i = ind; i < currSize - 1; i++)
			this->arr[i] = this->arr[i + 1];
		if(this->currSize>0) this->currSize--;
	}
};