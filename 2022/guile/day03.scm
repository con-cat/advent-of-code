(add-to-load-path (dirname (current-filename)))
(use-modules
 (srfi srfi-41)
 (helpers))

(define (parse-line l)
  (let ((idx (/ (string-length l) 2)))
    (let ((strings (list (substring l 0 idx) (substring l idx))))
      (car (char-set->list (apply char-set-intersection (map string->char-set strings)))))))

(define input (stream-map parse-line (file->stream-lines "../input/day03.txt")))

(define (get-priority c)
  (if (char-set-contains? char-set:lower-case c)
      (- (char->integer c) 96)
      (- (char->integer c) 38)))

(define (part-1)
  (let loop ((input input) (sum 0))
    (if (stream-null? input)
        sum
        (loop (stream-cdr input) (+ sum (get-priority (stream-car input)))))))


(display "Part 1: ")
(display (part-1))
(newline)
