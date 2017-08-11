package main  

import "fmt"

func plus(a int, b int) int {
	return a + b
}

func plusPlus(a, b, c int) int {
	return a + b + c
}

func vals() (int, int) {
	return 3, 4
}

// variadic functions
func sums(nums ...int) {
	fmt.Print(nums, " ")
	total := 0
	for _, nums := range nums {
		total += nums
	}
	fmt.Println(total)
}

// anonymous functions (closures)
func intSeq() func() int {
	 i := 0
	 return func() int {
	 	i += 1
	 	return i
	 }
}

// recursion
func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	res := plus(1, 2)
	fmt.Println("1+2 =", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)

	a, b := vals()
	_, c := vals()
	fmt.Println("a: ", a)
	fmt.Println("b: ", b)
	fmt.Println("c: ", c)

	nums := []int{1, 2, 3, 4}
	sums(nums...)

	nextInt := intSeq()
	fmt.Println(nextInt()) // print 1
	fmt.Println(nextInt()) // print 2

	fmt.Println(fact(7)) // print 5040
}