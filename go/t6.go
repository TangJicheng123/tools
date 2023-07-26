package main

import (
	"fmt"
	"reflect"
)

func main() {
	var age int = 30
	var name string = "John"
	var pi float64 = 3.14

	// 使用reflect.TypeOf()函数获取变量的类型信息并打印
	fmt.Println("Type of age:", reflect.TypeOf(age))
	fmt.Println("Type of name:", reflect.TypeOf(name))
	fmt.Println("Type of pi:", reflect.TypeOf(pi))
}
