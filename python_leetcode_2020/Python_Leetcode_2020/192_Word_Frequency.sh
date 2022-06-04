solution 1

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1 }'

tr -s: truncate the string with target string, but only remaining one instance (e.g. multiple whitespaces)

sort: To make the same string successive so that uniq could count the same string fully and correctly.

uniq -c: uniq is used to filter out the repeated lines which are successive, -c means counting

sort -r: -r means sorting in descending order

awk '{ print $2, $1 }': To format the output, see here.


Very Nice solution. Since I am not very thorough with Shell, so I thought of executing every seperate block. Just sharing the output, since it might help someone visualize the solution after reading it.
➜ Desktop cat Words.txt
the day is sunny the the
the sunny is is
➜ Desktop cat Words.txt| tr -s ' ' '\n'
the
day
is
sunny
the
the
the
sunny
is
is
➜ Desktop cat Words.txt| tr -s ' ' '\n' | sort
day
is
is
is
sunny
sunny
the
the
the
the
➜ Desktop cat Words.txt| tr -s ' ' '\n' | sort | uniq -c
1 day
3 is
2 sunny
4 the
➜ Desktop cat Words.txt| tr -s ' ' '\n' | sort | uniq -c | sort -r
4 the
3 is
2 sunny
1 day
➜ Desktop cat Words.txt| tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'
the 4
is 3
sunny 2
day 1



Solution 2:
cat words.txt | tr -s '[[:space:]]' '\n'| sort | uniq -c | sort -r | sed -r -e 's/[[:space:]]*([[:digit:]]+)[[:space:]]*([[:alpha:]]+)/\2 \1/g'



Solutionj 3

#  I should count the words. So I chose the awk command.
#  I use a dictionary in awk. For every line I count every word in the dictionary.
#  After deal with all lines. At the END, use for (item in Dict) { #do someting# } to print every words and its frequency.
#  Now the printed words are unsorted. Then I use a | pipes and sort it by sort
#  sort -n means "compare according to string numerical value".
#  sort -r means "reverse the result of comparisons".
#  sort -k 2 means "sort by the second word"
awk '\
{ for (i=1; i<=NF; i++) { ++D[$i]; } }\
END { for (i in D) { print i, D[i] } }\
' words.txt | sort -nr -k 2




Solution 4:

cat words.txt | tr -s [:blank:] '\n' | sort | uniq -c | sort -nr -k 1 | awk '{print $2, $1}'
tr -s translate, squeeze+replace: replaces [tab, newline, vertical tab, form feed, carriage return, and space] i.e., space characters [:space:] with a newline \n.
sort sort: sorts alphabetically (ascending order)
uniq -c unique, count: prints after omitting repeating adjacent lines uniq along with number of occurrences -c
sort -nr -k 1 sort, numeric+reverse, key: sorts numerically and in reverse -nr based on the key - first column -k 1
awk '{print $2 $1}' awk - split line into fields: splitting each line into specified fields (word first and then frequency). You can find more info on awk here.

TEST CASE:
In case there are punctuations in the text:

cat words.txt | tr -s [:blank:] '\n' | tr -d [:punct:] | sort | uniq -c | sort -nr -k 1 | awk '{print $2, $1}'
tr -d translate, delete: deletes any [! ” # $ % & ‘ ( ) * + , – . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~. ] i.e., punctuation characters [:punct:]



