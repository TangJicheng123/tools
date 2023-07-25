package main

import (
	"fmt"
)

type A struct {
	x int
}

func (a A) hello() {
	fmt.Println("this is A", a.x)
}

type B struct {
	y float32
}

func (b B) hello() {
	fmt.Println("this is B", b.y)
}

type HH interface {
	hello()
}

func test1(h HH) {
	h.hello()
}

func main() {
	a := A{x: 1}
	b := B{y: 3.4}
	test1(a)
	test1(b)
}
