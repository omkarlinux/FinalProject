A program that accept multiple keywords that we wish to compare as input as below.
$ ./Main.py <keyword 1> <keyword 2> ...

If we wished to compare the popularity of different programming languages we would run the
program as below
$ ./Main.py Java Python CSS C++ C# Ruby

OR to compare the popularity of different companies we would run the program as below
$ ./Main.py IBM Oracle Microsoft SAP Intel Hadoop SQL

The program will search Google for those keywords. It will fetch the page content from the resulting links
for each keyword. It will then count the number of times the keyword is used in the pages.
It will then rank the keywords with the highest to lowest count which shows a little information on
how popular the keyword currently is.

This is similar to what Google Trends does. Except that it has an already built database for this.
As we don't have one we rely on Google search results to find that.
