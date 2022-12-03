(add-to-load-path (dirname (current-filename)))
(use-modules
 (srfi srfi-41)
 (helpers))

(define (parse-line l)
  (let ((idx (/ (string-length l) 2)))
    (let ((strings (list (substring l 0 idx) (substring l idx))))
      (apply char-set-intersection (map string->char-set strings)))))

(define input (file->stream-lines "../input/day03.txt"))

(define (get-priority cset)
  (let ((c (car (char-set->list cset))))
    (if (char-set-contains? char-set:lower-case c)
        (- (char->integer c) 96)
        (- (char->integer c) 38))))

(define (part-1)
  (let loop ((input (stream-map parse-line input)) (sum 0))
    (if (stream-null? input)
        sum
        (loop (stream-cdr input) (+ sum (get-priority (stream-car input)))))))

(define (part-2)
  (let loop ((input (stream->list (stream-map string->char-set input))) (sum 0))
    (if (null? input)
        sum
        (let ((cset (apply char-set-intersection (list-head input 3))))
          (loop (list-tail input 3) (+ sum (get-priority cset)))))))



(display "Part 1: ")
(display (part-1))
(newline)
(display "Part 2: ")
(display (part-2))
(newline)
