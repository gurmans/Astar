# Astar


### Software Specifications

* Python 3.7
* Python Standard Libraries used
    * sys - for passing command line arguments
    * numpy - for support of multidimensional arrays
    * bisect - for dividing array according to different parameters
    * copy - for creating deep copies of objects
    

### How to run
```
$ python3 puzzle.py <command-line-arguments>
```
```
$ ./puzzle <command-line-arguments>
```
```
    * Output: all the puzzle transitions reaching out to a solved puzzle, each configuration represented by a 3X3 array
```

### command-line-arguments
* The first command line argument will determine the heuristic to be used in the program, 0 for 0, 1 or anything else for manhattan distance
* The next 9 space separated numbers (1 to 8) including the underscore (_) represent the input puzzle


### Sample run

```
$ python3 puzzle.py 0 1 4 2 6 3 5 _ 7 8
Heuristic used: 0
Input configuration:
[['1' '4' '2']
 ['6' '3' '5']
 ['_' '7' '8']]
The final path represented as a sequence of puzzle states:


 [['1' '4' '2']
 ['6' '3' '5']
 ['_' '7' '8']] 0

 [['1' '4' '2']
 ['_' '3' '5']
 ['6' '7' '8']] 1

 [['1' '4' '2']
 ['3' '_' '5']
 ['6' '7' '8']] 2

 [['1' '_' '2']
 ['3' '4' '5']
 ['6' '7' '8']] 3

 [['_' '1' '2']
 ['3' '4' '5']
 ['6' '7' '8']] 4

```

```
$ ./puzzle 1 1 4 2 6 3 5 _ 7 8
Heuristic used: Manhattan Distance
Input configuration:
[['1' '4' '2']
 ['6' '3' '5']
 ['_' '7' '8']]
The final path represented as a sequence of puzzle states:


 [['1' '4' '2']
 ['6' '3' '5']
 ['_' '7' '8']] 0

 [['1' '4' '2']
 ['_' '3' '5']
 ['6' '7' '8']] 1

 [['1' '4' '2']
 ['3' '_' '5']
 ['6' '7' '8']] 2

 [['1' '_' '2']
 ['3' '4' '5']
 ['6' '7' '8']] 3

 [['_' '1' '2']
 ['3' '4' '5']
 ['6' '7' '8']] 4
```

### Author

* **Gurman Singh**
