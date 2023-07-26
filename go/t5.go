package main

import (
	"encoding/json"
	"fmt"
)

type Person struct {
	Name     string `json:"fullName"`      // 指定字段在JSON中的名称为"fullName"
	Age      int    `json:"age,omitempty"` // 省略空值字段，如果Age为0，则在JSON中省略该字段
	Email    string `json:"-"`             // 在JSON编码/解码时忽略Email字段
	Password string `json:"password,omitempty"`
}

func main() {
	p := Person{
		Name:  "John Doe",
		Age:   30,
		Email: "john.doe@example.com",
	}

	// 将结构体转换为JSON
	jsonData, err := json.Marshal(p)
	if err != nil {
		fmt.Println("JSON encoding error:", err)
		return
	}

	fmt.Println(string(jsonData))
}
