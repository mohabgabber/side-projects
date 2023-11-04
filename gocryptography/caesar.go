package main

import (
	"strings"
)

func Caesarenc(msg string) string {
	var enc string
	for _, c := range msg {
		encindex := (strings.Index(CHARS, string(c)) + 3) % len(CHARS)
		enc += string(CHARS[encindex])
	}
	return enc
}

func Caesardec(msg string) string {
	var dec string
	for _, c := range msg {
		decindex := (strings.Index(CHARS, string(c)) - 3) % len(CHARS)
		dec += string(CHARS[decindex])
	}
	return dec
}
