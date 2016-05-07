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
	int const caseCount = readCaseCount();

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
		for (sregex_iterator i = iterator; i != iteratorDone; ++i)
		{
			wordStack.push(i->str());
		}
		while (!wordStack.empty())
		{
			output.append(" " + wordStack.top());
			wordStack.pop();
		}

		outputLine(&output);
	}
}