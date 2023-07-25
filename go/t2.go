package main

import "fmt"

type A struct {
	Name string
	Age  int
}

type B struct {
	A
	Position string
}

func test1(base A) {
	fmt.Println(base.Name)
	fmt.Println(base.Age)
}

func main() {
	b := B{
		A:        A{Name: "John", Age: 30},
		Position: "Developer",
	}

	test1(b.A)
	// test1(b) // 会报错：cannot use b (variable of type B) as A value in argument to test1
}
