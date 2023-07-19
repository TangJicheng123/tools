package main

import (
	"fmt"
)

var x int = 2

// syntax error: non-declaration statement outside function body
// y := 3

func My1() {
	// var a = 1
	// b := 1.1
	// fmt.Printf("%d %d %.4f\n", a, x, b)

	// x := 1
	// p := &x         // p, of type *int, points to x
	// fmt.Println(*p) // "1"
	// *p = 2          // equivalent to x = 2
	// fmt.Println(x)  // "2"

	// fmt.Println(f() == f()) // "false"

	v := 1
	incr(&v)              // side effect: v is now 2
	fmt.Println(incr(&v)) // "3" (and v is 3)
}

var p = f()

func f() *int {
	v := 1
	return &v
}

func incr(p *int) int {
	*p++ // 非常重要：只是增加p指向的变量的值，并不改变p指针！！！
	return *p
}

type Celsius float64    // 摄氏温度
type Fahrenheit float64 // 华氏温度

const (
	AbsoluteZeroC Celsius = -273.15 // 绝对零度
	FreezingC     Celsius = 0       // 结冰点温度
	BoilingC      Celsius = 100     // 沸水温度
)

func CToF(c Celsius) Fahrenheit { return Fahrenheit(c*9/5 + 32) }

func FToC(f Fahrenheit) Celsius { return Celsius((f - 32) * 5 / 9) }
