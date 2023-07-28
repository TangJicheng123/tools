package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main3() {
	r := gin.Default()
	r.POST("/somejson", assicJson)
	r.Run(":8080")
}

func assicJson(c *gin.Context) {
	data := map[string]any{
		"lang": "Go语言",
		"tag":  "<br>",
	}

	c.AsciiJSON(http.StatusOK, data)
}
