#use "vector_matrix_ops.ml";;

(* If the boolean 'expr' evaluates to false, then print the error 'message' *)
let test = 
  fun expr message -> 
    if expr = false then
      print_string message; print_newline ();;

(* vplus test cases *)
let result = vplus [] [] in
  let vout = (result = []) in 
    test (vout = true) "Test failed: result should be [].";;