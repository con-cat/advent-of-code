(add-to-load-path (dirname (current-filename)))
(use-modules
 (helpers)
 (srfi srfi-41))

(define input
  (stream-map string->number (file->stream-lines "../input/day01.txt")))


(define (part-1 elves)
  (apply max elves))

(define (part-2 elves)
  (apply + (list-head (sort elves >) 3)))

(define (solve proc)
  (let loop ((input input) (elf 0) (all-elves '()))
    (cond ((stream-null? input)
           ;; We've read the whole file, return the maximum calories
           (proc (append (list elf) all-elves)))
          ((not (stream-car input))
           ;; Blank line, move to the next elf
           (loop (stream-cdr input) 0 (append (list elf) all-elves)))
          (else
           ;; Keep summing the current elf's calories
           (loop (stream-cdr input) (+ elf (stream-car input)) all-elves)))))


(display (solve part-1))
(newline)
(display (solve part-2))
(newline)
