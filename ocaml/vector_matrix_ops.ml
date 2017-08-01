(* type aliases for vectors and matrices *)            
type vector = float list                                 
type matrix = vector list

(* vector addition *)
let (vplus : vector -> vector -> vector) =
  fun v1 v2 ->
    match (v1, v2) with
      ([], [])     -> []
    | (_::_, [])   -> v1
    | ([], _::_)   -> v2
    | (_::_, _::_) -> List.map2 (fun x y -> x +. y) v1 v2
;;