package main

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main2() {
	r := gin.Default()

	r.POST("/api", queryHandler)

	r.Run(":8080")
}

func queryHandler(c *gin.Context) {
	name := c.Query("name")
	fmt.Printf("[my] %s\n", name)
	c.String(http.StatusOK, "Your name: %s", name)
}
