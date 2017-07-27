#use "set_ops.ml";;

(* member test *)
assert( member 1 [] = false);;
assert( member 2 [1; 2] = true);;
(* add *)
assert( add 1 [] = [1]);;
assert( add 2 [1; 2; 3;] = [1; 2; 3;]);;
assert( add 5 [1; 2] = [1; 2; 5]);;
(* union *)
assert( union [] [] = []);;
assert( union [1] [1; 2] = [1; 2]);;
assert( union [1; 2] [3; 4] = [3; 4; 1; 2]);;
assert( union [] [1; 2] = [1; 2]);;
assert( union [1] [1; 2; 3] = [1; 2; 3]);;
assert( union [5; 3; 2] [3; 7; 2] = [3; 7; 2; 5]);;
(* intersection *)
assert( intersection [] [] = []);;
assert( intersection [1] [] = []);;
assert( intersection [1] [1] = [1]);;
assert( intersection [1; 2; 3] [1; 3; 2] = [1; 3; 2]);;
(* setify *)
assert( setify [] = []);;
assert( setify [1; 2] = [1; 2]);;
assert( setify [1; 2; 1] = [2; 1]);;
assert( setify [1; 2; 1; 4; 1] = [2; 4; 1]);;
assert( setify [1; 2; 1; 4; 2; 5; 4] = [1; 2; 5; 4]);;
(* powerset *)
assert( powerset [] = [[]]);;
assert( powerset [1;2] = [[]; [2]; [1]; [1;2]]);;
assert( powerset [1;2;3] = [[]; [3]; [2]; [2;3]; [1]; [1;3]; [1;2]; [1;2;3]]);;