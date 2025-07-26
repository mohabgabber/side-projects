package airportrobot

import "fmt"

// Write your code here.
// This exercise does not have tests for each individual task.
// Try to solve all the tasks first before running the tests.
type Greeter interface {
	LanguageName() string
	Greet(name string) string
}

type Italian struct {
}

func (i Italian) Greet(name string) string {
	return "Ciao " + name + "!"
}

func (i Italian) LanguageName() string {
	return "Italian"
}

type Portuguese struct {
}

func (p Portuguese) LanguageName() string {
	return "Portuguese"
}
func (p Portuguese) Greet(name string) string {
	return "Olá " + name + "!"
}

func SayHello(name string, g Greeter) string {
	return fmt.Sprintf("I can speak %v: %v", g.LanguageName(), g.Greet(name))
}
