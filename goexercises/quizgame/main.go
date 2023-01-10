package main

import (
	"encoding/csv"
	"flag"
	"os"
	"time"

	// "strconv"
	"fmt"
)

type csvlines struct {
	Column1 string
	Column2 string
}

func main() {
	// 1st Reading the default csv file
	var csvflag string
	var times int
	flag.StringVar(&csvflag, "f", "default.csv", "Enter The Desired CSV file")
	flag.IntVar(&times, "t", 30, "Enter the quiz timer")
	flag.Parse()
	csvdata, err := readincsv(csvflag)
	timer := time.NewTimer(time.Duration(times) * time.Second)

	if err != nil {
		panic(err)
	}
	score := 0
	var ans string
	for _, line := range csvdata {
		fmt.Println(line[0])
		answerch := make(chan string)
		go func() {
			fmt.Scanln(&ans)
			answerch <- ans
		}()
		select {
		case <-timer.C:
			fmt.Printf("Your Score Is %d", score)
			return
		case answer := <-answerch:
			if ans == answer {
				score++
			}
		}
	}
	fmt.Printf("Your Score Is %d", score)
}

func readincsv(filename string) ([][]string, error) {
	csvfile, err := os.Open(filename)
	if err != nil {
		return [][]string{}, err
	}
	defer csvfile.Close()
	lines, err := csv.NewReader(csvfile).ReadAll()
	if err != nil {
		return [][]string{}, err
	}
	return lines, nil
}
