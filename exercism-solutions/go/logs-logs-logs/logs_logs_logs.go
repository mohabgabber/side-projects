package logs

import "unicode/utf8"

// Application identifies the application emitting the given log.
func Application(log string) string {
	recommendation := '❗'
	search := '🔍'
	weather := '☀'

	for _, c := range log {
		if c == recommendation {
			return "recommendation"
		} else if c == search {
			return "search"
		} else if c == weather {
			return "weather"
		}
	}
	return "default"
}

// Replace replaces all occurrences of old with new, returning the modified log
// to the caller.
func Replace(log string, oldRune, newRune rune) string {
	var newStr string
	for _, c := range log {
		if c == oldRune {
			newStr += string(newRune)
		} else {
			newStr += string(c)
		}
	}
	return newStr
}

// WithinLimit determines whether or not the number of characters in log is
// within the limit.
func WithinLimit(log string, limit int) bool {
	return utf8.RuneCountInString(log) <= limit
}
