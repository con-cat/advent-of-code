(use-modules (srfi srfi-41))

(define-stream (file->stream-lines filename)
  ;; Stream a file line by line
  (let ((p (open-input-file filename)))
    (stream-let loop ((l (read-line p)))
                (if (eof-object? l)
                    (begin (close-input-port p)
                           stream-null)
                    (stream-cons l
                                 (loop (read-line p)))))))

(define (parse-line line)
  ;; Parse the line to a pair of string and int
  (let ((split (string-split line #\space)))
    (cons (car split) (string->number (cadr split)))))

(define input (stream-map parse-line (file->stream-lines "/Users/caitlinwhite/src/advent-of-code/2021/input/day02.txt")))


(define (direction s)
  ;; Return the direction string from the first item of the input stream
  (let ((item (stream-car s)))
    (car item)))

(define (n s)
  ;; Return the number from the first item of the input stream
  (let ((item (stream-car s)))
    (cdr item)))

;; PART 1

(define (part-1)
  (let ((x 0) (y 0))
    (let loop ((input input))
      (cond ((stream-null? input)
             (* x y))
            ((string=? (direction input) "forward")
             (set! x (+ x (n input)))
             (loop (stream-cdr input)))
            ((string=? (direction input) "up")
             (set! y (- y (n input)))
             (loop (stream-cdr input)))
            ((string=? (direction input) "down")
             (set! y (+ y (n input)))
             (loop (stream-cdr input)))))))

;; PART 2

(define (part-2)
  (let ((x 0) (y 0) (aim 0))
    (let loop ((input input))
      (cond ((stream-null? input)
             (* x y))
            ((string=? (direction input) "forward")
             (set! x (+ x (n input)))
             (set! y (+ y (* aim (n input))))
             (loop (stream-cdr input)))
            ((string=? (direction input) "up")
             (set! aim (- aim (n input)))
             (loop (stream-cdr input)))
            ((string=? (direction input) "down")
             (set! aim (+ aim (n input)))
             (loop (stream-cdr input)))))))


(part-2)
