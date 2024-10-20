# 5 kyu - Find character

## LINK
https://www.codewars.com/kata/5817030088ca96c0b7000083

## Task
>"TWhen no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process --myjinxin2015 said"

### Description:
Give you a character matrix. Find out the character which has the smallest amount.

### Arguments:
- ```matrix```: A string that contains some letters. Each row is separated by "\n".
### Results & Note:
- Returns the characters which has smallest amount, using string format.
- If more than one characters are found, sort them according to the order A-Za-z0-9.
- You can assume that there are at least two characters in the matrix.
- Please ignore the "\n" ;-)
### Some Examples
```
matrix=
00000000
0000O000
00000000
00000000
00000000
```
```
result -> "O"
matrix=
mmmmmmmmmmmmm
mmmmmmmmmmmmm
mmmmmmmmmmmmm
mmmmmmmmmnmmm
```
```
result -> "n"
matrix=
AAAAAAAAAAA
AABBBBBBBBB
BCCCCCCCCDD
DDDDEEEEFFF

result -> "F"
```
```
matrix=
AAAAA
ABBBB
BCCCC
DDDDE
EEEEF
FFFFF

result -> "CD"                                      =>  
```

### My kata answer

[Link of my solution](https://www.codewars.com/kata/reviews/5b86545bb80ee00ca6000358/groups/6712cbfed95a64f4b69139c6)

[find_characters.py](/python/5%20kyu/Find%20character/find_characters.py)
