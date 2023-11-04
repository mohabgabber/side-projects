package main

import (
	"strings"
)

func keylength(msg, key string) string {
	if len(key) != len(msg) {
		if len(msg) > len(key) {
			diff := len(msg) - len(key)
			iterator := 0
			nkey := key
			for i := 0; i <= diff; i++ {
				if len(msg) == len(nkey) {
					break
				} else {
					if iterator > (len(key) - 1) {
						iterator = 0
					}
					nkey += string(key[iterator])
					iterator++
				}
			}
			return nkey
		} else if len(msg) < len(key) {
			nkey := key[0:len(msg)]

			return nkey
		}
	} else {
		return key
	}
	return ""
}

func Vigenereenc(msg, key string) string {
	nkey := keylength(msg, key)
	var encindex int
	var enctxt string
	for i, c := range msg {
		encindex = (strings.Index(CHARS, string(c)) + strings.Index(CHARS, string(nkey[i]))) % len(CHARS)
		enctxt += string(CHARS[encindex])
	}
	return enctxt
}

func Vigeneredec(msg, key string) string {
	nkey := keylength(msg, key)
	var decindex int
	var dectxt string
	for i, c := range msg {
		decindex = (strings.Index(CHARS, string(c)) - strings.Index(CHARS, string(nkey[i]))) % len(CHARS)
		dectxt += string(CHARS[decindex])
	}
	return dectxt
}
