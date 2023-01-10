package main

import (
	"net/http"
	//"errors"
	"github.com/gin-gonic/gin"
)

type book struct {
	ID       string `json:"id"`
	Title    string `json:"title"`
	Author   string `json:"author"`
	Quantity int    `json:"quantity"`
}

var books = []book{
	{ID: "1", Title: "In Search of Lost Time", Author: "Marcel Proust", Quantity: 2},
	{ID: "2", Title: "The Great Gatsby", Author: "F. Scott Fitzgerald", Quantity: 5},
	{ID: "3", Title: "War and Peace", Author: "Leo Tolstoy", Quantity: 6},
}

func getBooks(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, books)
}

func createBook(c *gin.Context) {
	var newbook book
	if err := c.BindJSON(&newbook); err != nil {
		return
	}
	books = append(books, newbook)
	c.IndentedJSON(http.StatusCreated, newbook)
}

func main() {
	router := gin.Default()
	router.GET("/books", getBooks)
	router.POST("/create", createBook)
	router.Run("localhost:8080")
}
