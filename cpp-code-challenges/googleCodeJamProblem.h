#pragma once
#include <iostream>
#include <fstream>
#include <regex>
#include <list>
#include "azlException.h"

class googleCodeJamProblem
{
public:
	void openFiles(std::string const * inputFilename, std::string const * outputFilename);
	virtual void execute() = 0;
	virtual ~googleCodeJamProblem();

protected:
	googleCodeJamProblem();
	void outputLine(std::string const * outputString);
	
	void const readLine();
	int const readSingleInt();
	void const readManyInt(std::list<int>& outputList);

	char getLineBuffer[10000];
	std::string* getLineString;

private:
	std::ifstream inputFileHandle;
	std::ofstream outputFileHandle;
};

