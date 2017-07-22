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