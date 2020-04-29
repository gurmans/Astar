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
    * Output: all the puzzle transitions reaching out to a solved puzzle, each configuration represented by a 3X3 array
### <command-line-arguments>
  * The first 9 space separated numbers (1 to 8) including the underscore (_) represent the input puzzle
  * The last argument number represents the heuristic to be used, '1' for Manhattan distance and '2' for 0.


### Sample run

```
$ python3 puzzle.py 1 4 2 6 3 5 _ 7 8 1
* Output 
Heuristic used: Manhattan Distance
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
 ['6' '7' '8']] 4```

### Author

* **Gurman Singh**
