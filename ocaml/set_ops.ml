(* member function: check if x is a member of set s *)

let rec (member : 'a  -> 'a list -> bool) =
	fun x s ->
		match s with
			[] -> false
		| h::t -> if h = x then true else member x s
;;

(* add function: check if x is in s, if not, add x *)

let rec (add : 'a -> 'a list -> 'a list) =
	fun x s ->
		match s with
			[] -> [x]
		| h::t -> if h = x then s else h::add x t
;;

(* union function: return the union of s1 and s2 *)

let rec (union : 'a list -> 'a list -> 'a list) =
	fun s1 s2 ->
		match (s1, s2) with
			([], []) -> []
		| ([], _::_) -> s2
		| (_::_, []) -> s1
		| (h1::t1, h2::t2) -> union t1 (add h1 t2)
;;

(* intersection function: return the intersection of s1 and s2 *)

let (intersection : 'a list -> 'a list -> 'a list) =
	fun s1 s2 ->
		match (s1, s2) with
			([], []) -> []
		| ([], _::_) -> []
		| (_::_, []) -> []
		| (h1::t1, h2::t2) -> List.filter (fun (x) -> if member x s1 then true else false) s2
;;

(* setify *)

let rec (setify : 'a list -> 'a list) =
	fun l ->
		match l with
			[] -> []
		| [h] -> [h]
		| h::t -> if (member h t) then setify t else h::setify t
;;

(* powerset *)

let rec (powerset : 'a list -> 'a list list) =
  fun s ->
    match s with
      []   -> [[]]
    | h::t -> let s = powerset t in
                      s @ (List.map (fun x -> h :: x) s)
;;
