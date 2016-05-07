#pragma once
#include <exception>

class azlException : virtual std::exception
{
public:
	enum reasons
	{
		inoutFileOpenFailure,
		charBufferexceeded,
	};
	reasons reason;

	azlException(reasons in_reason)
	{
		reason = in_reason;
	}

	virtual char const * what()
	{
		switch (reason)
		{
		case inoutFileOpenFailure:
			return "failed to open the input our output filenames";
		case charBufferexceeded:
			return "a chararacter buffer was written past its extents";
		default:
			return "unknown azlException";
		}
	}
};