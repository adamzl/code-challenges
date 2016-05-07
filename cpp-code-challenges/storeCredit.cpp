#include "storeCredit.h"
#include <list>

using namespace std;

storeCredit::storeCredit()
{
}

storeCredit::~storeCredit()
{
}

class item
{
public:
	int cost;
	int index;

	item(int _cost, int _index)
		: cost(_cost)
		, index(_index)
	{}

	bool operator<(item& right)
	{
		return cost < right.cost;
	}
};

void storeCredit::execute()
{
	int const caseCount = readSingleInt();

	for (int curCase = 1; curCase <= caseCount; curCase++)
	{
		int const credits = readSingleInt();
		readSingleInt();
		list<int> storeItems;
		readManyInt(storeItems);

		list<item> sortedItems;

		int index = 1;
		for (auto it = storeItems.begin(); it != storeItems.end(); it++)
		{
			sortedItems.push_back(item(*it, index));
			index++;
		}
		sortedItems.sort();
		auto leftIt = sortedItems.begin();
		auto rightIt = sortedItems.rbegin();
		while ((leftIt->cost + rightIt->cost) != credits)
		{
			if ((leftIt->cost + rightIt->cost) < credits)
			{
				leftIt++;
			}
			else
			{
				rightIt++;
			}
		}

		int leftIndex, rightIndex;
		if (leftIt->index < rightIt->index)
		{
			leftIndex = leftIt->index;
			rightIndex = rightIt->index;
		}
		else
		{
			rightIndex= leftIt->index;
			leftIndex = rightIt->index;
		}
		string output("Case #" + to_string(curCase) + ": " + to_string(leftIndex) + " " + to_string(rightIndex));
		outputLine(&output);
	}
}
