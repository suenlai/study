// You can edit this code!
// Click here and start typing.
package main

import "fmt"

func main() {
	var a, b, su int
	a = 123
	b = 456
	su = sum(a, b)
	fmt.Println("su", su)
	fmt.Println("Hello, 世界")
}
func sum(a, b int) (re int) {
	re = a + b
	return re
}
