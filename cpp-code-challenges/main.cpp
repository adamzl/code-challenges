#include <iostream>
#include "reverseWords.h"
#include "storeCredit.h"

using namespace std;

int main(int argc, char** argv)
{
	try
	{
		string const inputFilename = "c:\\users\\adam\\desktop\\input.txt";
		string const outputFilename = "c:\\users\\adam\\desktop\\output.txt";

		//googleCodeJamProblem* problem = new reverseWords();
		googleCodeJamProblem* problem = new storeCredit();

		problem->openFiles(&inputFilename, &outputFilename);
		problem->execute();

		delete problem;

		cout << "done, <enter> to exit.\n";
		getchar();
		return 0;
	}
	catch(const std::exception& e)
	{
		cout << e.what();
		getchar();
		return 1;
	}
}