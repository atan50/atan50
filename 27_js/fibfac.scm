;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname fibfac) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Team MagiMan :: Amanda Tan, Kishi Wijaya
;SoftDev pd4
;K27 - Basic functions in JavaScript
;2025-01-06m

;factorial
(define fac (λ(n)
              (if (= n 1)
                  1
                  (* n (fac (- n 1))))))

(fac 1) ;1
(fac 2) ;2
(fac 3) ;6

;fibonacci
(define fib (λ(n)
              (if (= n 0)
                  0
                  (if (= n 1)
                      1
                      (+ (fib(- n 1)) (fib(- n 2)))))))

(fib 0) ;0
(fib 1) ;1
(fib 2) ;1
(fib 3) ;2