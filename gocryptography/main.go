package main

import (
	"flag"
	"fmt"
	"log"
)

func validate(msg, key string, csr, vgr, e, d bool) {
	if len(msg) < 2 {
		log.Fatal("Msg length is insufficient")
	}
	if (!csr && !vgr) || (csr && vgr) {
		log.Fatal("You need to choose one algorithm")
	}
	if (!e && !d) || (e && d) {
		log.Fatal("You need to choose one operation")
	}
	if vgr && len(key) < 2 {
		log.Fatal("You must provide a key of at least 2 chars when using vigenere cipher")
	}
}

func exec(msg, key string, csr, vgr, e, d bool) {
	validate(msg, key, csr, vgr, e, d)
	if csr {
		if e {
			fmt.Print(Caesarenc(msg))
		} else if d {
			fmt.Print(Caesardec(msg))
		}
	} else if vgr {
		if e {
			fmt.Print(Vigenereenc(msg, key))
		} else if d {
			fmt.Print(Vigeneredec(msg, key))
		}
	}
}

func main() {
	var (
		msg string
		key string
		csr bool
		vgr bool
		e   bool
		d   bool
	)
	flag.StringVar(&msg, "m", "", "Provide a message")
	flag.BoolVar(&csr, "csr", false, "Use caesar cipher")
	flag.BoolVar(&vgr, "vgr", false, "Use vigenere cipher")
	flag.BoolVar(&e, "e", false, "Decrypt msg")
	flag.BoolVar(&d, "d", false, "Encrypt msg")
	flag.StringVar(&key, "k", "", "Encryption key (Used with Vigenere Cipher Only)")
	flag.Parse()
	exec(msg, key, csr, vgr, e, d)
}
