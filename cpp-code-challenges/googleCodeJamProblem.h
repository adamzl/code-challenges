#pragma once
#include <iostream>
#include <fstream>
#include <regex>
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
	int const readCaseCount();
	void const readLine();
	char getLineBuffer[1000];
	std::string* getLineString;

private:
	std::ifstream inputFileHandle;
	std::ofstream outputFileHandle;
};

