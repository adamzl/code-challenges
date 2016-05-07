#include "spelling.h"
#include <map>
#include <regex>

using namespace std;

spelling::spelling()
{
}

spelling::~spelling()
{
}

void spelling::execute()
{
	map<char, string> keypadMap;
	keypadMap.insert(pair<char, string>('a', "2"));
	keypadMap.insert(pair<char, string>('b', "22"));
	keypadMap.insert(pair<char, string>('c', "222"));
	keypadMap.insert(pair<char, string>('d', "3"));
	keypadMap.insert(pair<char, string>('e', "33"));
	keypadMap.insert(pair<char, string>('f', "333"));
	keypadMap.insert(pair<char, string>('g', "4"));
	keypadMap.insert(pair<char, string>('h', "44"));
	keypadMap.insert(pair<char, string>('i', "444"));
	keypadMap.insert(pair<char, string>('j', "5"));
	keypadMap.insert(pair<char, string>('k', "55"));
	keypadMap.insert(pair<char, string>('l', "555"));
	keypadMap.insert(pair<char, string>('m', "6"));
	keypadMap.insert(pair<char, string>('n', "66"));
	keypadMap.insert(pair<char, string>('o', "666"));
	keypadMap.insert(pair<char, string>('p', "7"));
	keypadMap.insert(pair<char, string>('q', "77"));
	keypadMap.insert(pair<char, string>('r', "777"));
	keypadMap.insert(pair<char, string>('s', "7777"));
	keypadMap.insert(pair<char, string>('t', "8"));
	keypadMap.insert(pair<char, string>('u', "88"));
	keypadMap.insert(pair<char, string>('v', "888"));
	keypadMap.insert(pair<char, string>('w', "9"));
	keypadMap.insert(pair<char, string>('x', "99"));
	keypadMap.insert(pair<char, string>('y', "999"));
	keypadMap.insert(pair<char, string>('z', "9999"));
	keypadMap.insert(pair<char, string>(' ', "0"));

	int const caseCount = readSingleInt();

	for (int curCase = 1; curCase <= caseCount; curCase++)
	{
		readLine();
		char previousChar = '*';
		string output;
		output.append("Case #" + to_string(curCase) + ": ");
		for (int index = 0; getLineBuffer[index] != '\0'; index++)
		{
			string& mapString = keypadMap[getLineBuffer[index]];
			if (mapString[0] == previousChar)
			{
				output.append(" ");
			}
			output.append(mapString);
			previousChar = mapString[0];
		}
		outputLine(&output);
	}
}


