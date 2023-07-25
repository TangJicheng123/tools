package main

import (
	"fmt"
)

type Animal struct {
	name   string
	weight float32
}

func (a Animal) Eat() {
	fmt.Println("Animal is eating...")
}

type Dog struct {
	Animal // Animal 结构体嵌套到 Dog 结构体中
	breed  string
}

func (d Dog) Bark() {
	fmt.Println("Dog is barking...")
}

func main() {
	d := Dog{Animal: Animal{name: "ddd", weight: 3.4}, breed: "hahahaha"}
	d.Bark()
	d.Eat()
}
