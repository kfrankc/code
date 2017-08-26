package main 

import "fmt"
import "os"

type point struct {
	x, y int
}

var pr = fmt.Printf

func main() {
	p := point{1, 2}
	pr("%v\n", p)

	pr("%+v\n", p)
	pr("%#v\n", p)
	pr("%T\n", p)
	pr("%t\n", true)

	pr("%d\n", 123)
	pr("%b\n", 14)
	pr("%c\n", 33)
	pr("%x\n", 456)
	pr("%f\n", 78.9)
}