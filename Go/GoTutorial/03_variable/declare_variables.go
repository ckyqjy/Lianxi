package main

import (
	"fmt"
)

func main() {
	// Type is string
	var student1 string = "John"
	// Type is inferred
	var student2 = "Jane"
	// Type is inferred
	x := 2

	fmt.Println(student1)
	fmt.Println(student2)
	fmt.Println(x)

	// Declare multiple variables
	var a, b, c, d int = 1, 3, 5, 7

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
}
