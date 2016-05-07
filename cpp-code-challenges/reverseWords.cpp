#include "reverseWords.h"
#include <stack>

using namespace std;

reverseWords::reverseWords()
{
}

reverseWords::~reverseWords()
{
}

void reverseWords::execute()
{
	int const caseCount = readSingleInt();

	regex wordPattern("[^\\s]+");
	string output;
	output.resize(200);
	for (int curCase = 1; curCase <= caseCount; curCase++)
	{
		output.clear();
		output.append("Case #" + to_string(curCase) + ":");
		readLine();
		sregex_iterator iterator = sregex_iterator(getLineString->begin(), getLineString->end(), wordPattern);
		sregex_iterator iteratorDone = sregex_iterator();
		stack<string> wordStack;
		for (; iterator != iteratorDone; iterator++)
		{
			wordStack.push(iterator->str());
		}
		while (!wordStack.empty())
		{
			output.append(" " + wordStack.top());
			wordStack.pop();
		}

		outputLine(&output);
	}
}
