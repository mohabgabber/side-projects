package sorting

import (
	"fmt"
	"strconv"
)

// DescribeNumber should return a string describing the number.
func DescribeNumber(f float64) string {
	str := fmt.Sprintf("This is the number %v", strconv.FormatFloat(f, 'f', 1, 64))
	return str
}

type NumberBox interface {
	Number() int
}

// DescribeNumberBox should return a string describing the NumberBox.
func DescribeNumberBox(nb NumberBox) string {
	return fmt.Sprintf("This is a box containing the number %v", strconv.FormatFloat(float64(nb.Number()), 'f', 1, 64))
}

type FancyNumber struct {
	n string
}

func (i FancyNumber) Value() string {
	return i.n
}

type FancyNumberBox interface {
	Value() string
}

// ExtractFancyNumber should return the integer value for a FancyNumber
// and 0 if any other FancyNumberBox is supplied.
func ExtractFancyNumber(fnb FancyNumberBox) int {
	var holder int
	switch fnb.(type) {
	case FancyNumber:
		holder, _ = strconv.Atoi(fnb.Value())
	default:
		holder = 0
	}
	return holder
}

// DescribeFancyNumberBox should return a string describing the FancyNumberBox.
func DescribeFancyNumberBox(fnb FancyNumberBox) string {
	return "This is a fancy box containing the number " + strconv.FormatFloat(float64(ExtractFancyNumber(fnb)), 'f', 1, 64)
}

// DescribeAnything should return a string describing whatever it contains.
func DescribeAnything(i interface{}) string {
	integer, ok := i.(int)
	if ok {
		return DescribeNumber(float64(integer))
	}
	fancynumber, ok := i.(FancyNumberBox)
	if ok {
		return DescribeFancyNumberBox(fancynumber)
	}
	floating, ok := i.(float64)
	if ok {
		return DescribeNumber(floating)
	}
	numbox, ok := i.(NumberBox)
	if ok {
		return DescribeNumberBox(numbox)
	}
	return "Return to sender"
}
