package main

import (
	"fmt"
)

type A struct {
	x int
}

func (a A) test1() {
	a.x = -1
}

func main() {
	a := A{x: 100}
	fmt.Println(a.x)
	a.test1()
	fmt.Println(a.x)
}
