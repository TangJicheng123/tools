package main

import "fmt"

type A struct {
	x int
	y string
}

func (a *A) Serialize() string {
	s := fmt.Sprintf("{\"x\":%d, \"y\":\"%s\"}", a.x, a.y)
	return s
}

func main1() {
	a := A{
		x: 123,
		y: "hello",
	}
	s := a.Serialize()
	fmt.Println(s)
}
