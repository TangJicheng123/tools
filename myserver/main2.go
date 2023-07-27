package main

import (
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func main2() {
	r := gin.Default()

	r.POST("/api", queryHandler)
	r.POST("/user/:id", userHandler)

	r.Run(":8080")
}

func queryHandler(c *gin.Context) {
	name := c.Query("name")

	value := c.DefaultQuery("value", "None")

	ext, ok := c.GetQuery("ext")
	fmt.Println("[my] default ext: <", ext, ">")
	if !ok {
		ext = "haha"
	}

	fmt.Printf("[my] %s\n", name)
	c.String(http.StatusOK, "Your name: %s, value: %s, ext: %s", name, value, ext)
}

type user struct {
	ID int `json:"id"`
}

func userHandler(c *gin.Context) {
	id := c.Param("id")
	fmt.Println("[my]", id)
	idInt, err := strconv.Atoi(id)
	httpCode := http.StatusOK
	if err != nil {
		idInt = -1
		httpCode = http.StatusBadRequest
	}
	ret := user{ID: idInt}
	c.JSON(httpCode, ret)
}
