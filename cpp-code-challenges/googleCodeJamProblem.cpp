#include "googleCodeJamProblem.h"

using namespace std;

googleCodeJamProblem::googleCodeJamProblem()
{
	getLineString = NULL;
}

googleCodeJamProblem::~googleCodeJamProblem()
{
	inputFileHandle.close();
	outputFileHandle.close();
	if (getLineString) { delete getLineString; }
}

void googleCodeJamProblem::openFiles(string const * inputFilename, string const * outputFilename)
{
	inputFileHandle.open(*inputFilename);
	outputFileHandle.open(*outputFilename);
	if (!inputFileHandle.is_open() || !outputFileHandle.is_open())
	{
		throw azlException(azlException::reasons::inoutFileOpenFailure);
	}
}

void googleCodeJamProblem::outputLine(std::string const * outputString)
{
	if (!outputFileHandle.is_open())
	{
		throw azlException(azlException::reasons::inoutFileOpenFailure);
	}

	printf("%s\n", outputString->c_str());
	outputFileHandle.write(outputString->c_str(), outputString->length());
	outputFileHandle.write("\n", 1);
}

int const googleCodeJamProblem::readSingleInt()
{
	inputFileHandle.getline(getLineBuffer, sizeof getLineBuffer);
	return atoi(getLineBuffer);
}

void const googleCodeJamProblem::readManyInt(list<int>& outputList)
{
	outputList.clear();
	readLine();

	regex wordPattern("\\d+");
	sregex_iterator iterator = sregex_iterator(getLineString->begin(), getLineString->end(), wordPattern);
	sregex_iterator iteratorDone = sregex_iterator();
	for (; iterator != iteratorDone; iterator++)
	{
		int number = stoi(iterator->str());
		outputList.push_back(number);
	}
}

void const googleCodeJamProblem::readLine()
{
	inputFileHandle.getline(getLineBuffer, sizeof getLineBuffer);
	for (int index = 0; index < sizeof getLineBuffer; index++)
	{
		if (getLineBuffer[index] == '\n')
		{
			getLineBuffer[index] = '\0';
			break;
		}
	}
	if (getLineString) { delete getLineString; }
	getLineString = new string(getLineBuffer);
}
