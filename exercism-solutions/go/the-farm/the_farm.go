package thefarm

import (
	"errors"
	"fmt"
	"strconv"
)

// TODO: define the 'DivideFood' function
func DivideFood(c FodderCalculator, cows int) (float64, error) {
	amo, err := c.FodderAmount(cows)
	if err != nil {
		return 0, err
	}
	fac, err := c.FatteningFactor()
	if err != nil {
		return 0, err
	}
	var tot float64 = (amo / float64(cows)) * fac
	return tot, nil
}

// TODO: define the 'ValidateInputAndDivideFood' function
func ValidateInputAndDivideFood(c FodderCalculator, cows int) (float64, error) {
	if cows > 0 {
		return DivideFood(c, cows)
	} else {
		return 0, errors.New("invalid number of cows")
	}
}

// TODO: define the 'ValidateNumberOfCows' function
type InvalidCowsError struct {
	numOfCows int
	cusError  string
}

func (e *InvalidCowsError) Error() string {
	return fmt.Sprintf("%s cows are invalid: %s", strconv.Itoa(e.numOfCows), e.cusError)
}
func ValidateNumberOfCows(cows int) error {
	if cows < 0 {
		return &InvalidCowsError{numOfCows: cows, cusError: "there are no negative cows"}
	} else if cows == 0 {
		return &InvalidCowsError{numOfCows: cows, cusError: "no cows don't need food"}
	} else {
		return nil
	}
}

// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
//
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more
// functionality.
