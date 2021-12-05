(use-modules (ice-9 textual-ports))

(define (number-string->number-list str)
  ;; Convert a string of numbers to a list of integers
  (map (lambda (ch)
         (- (char->integer ch) 48))
       (string->list str)))

(define data
  (map number-string->number-list
       (string-split
        (string-drop-right (call-with-input-file "../input/day03.txt" get-string-all) 1) #\newline)))

(define (bit-list->number bit-list)
  (string->number (string-join (map number->string bit-list) "") 2))

(define data
  (map number-string->number-list
       (string-split
        (string-drop-right (call-with-input-file "../input/day03.txt" get-string-all) 1) #\newline)))

(define (sum-bits lst len)
        (if (null? lst)
            (make-list len 0)
            (map + (car lst) (sum-bits (cdr lst) len))))

(define (most-common-bit bit-sums len)
  (map (lambda (bit)
         (if (< bit (/ len 2))
             0
             1))
       bit-sums))

(define (flip-bit bit)
(if (= 0 bit)
    1
    0))

(define (part1)
  (let ((gamma-rate
         (let ((len (length (car data))))
           (most-common-bit (sum-bits data len) (length data)))))
    (* (bit-list->number gamma-rate) (bit-list->number (map flip-bit gamma-rate)))))

(define (part2)



(part1)
