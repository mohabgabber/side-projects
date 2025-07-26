package birdwatcher

// TotalBirdCount return the total bird count by summing
// the individual day's counts.
func TotalBirdCount(birdsPerDay []int) int {
	var counter int
	for i := 0; i <= (len(birdsPerDay) - 1); i++ {
		counter += birdsPerDay[i]
	}
	return counter
}

// BirdsInWeek returns the total bird count by summing
// only the items belonging to the given week.
func BirdsInWeek(birdsPerDay []int, week int) int {
	var counter int
	newlist := birdsPerDay[(week*7)-7 : (week * 7)]
	for i := 0; i < len(newlist); i++ {
		counter += newlist[i]
	}
	return counter
}

// FixBirdCountLog returns the bird counts after correcting
// the bird counts for alternate days.
func FixBirdCountLog(birdsPerDay []int) []int {
	for i := 0; i < len(birdsPerDay); i++ {
		if i%2 == 0 {
			birdsPerDay[i] += 1
		}
	}
	return birdsPerDay
}
