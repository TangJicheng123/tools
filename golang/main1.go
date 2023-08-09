package main

import "fmt"

type Base struct{}

func (base *Base) Run() {
	fmt.Println("Base Run")
}

type A struct {
	Base
}

func (a *A) Run() {
	fmt.Println("A run")
}

func main1() {
	a := A{
		Base: Base{},
	}
	a.Base.Run()
	a.Run()
}
