(add-to-load-path (dirname (current-filename)))
(use-modules
 (srfi srfi-41)
 (helpers))

(define input (stream->list (file->stream-chars "../input/day06.txt")))

(define (solve n)
  (let loop ((input input) (idx n))
    (let ((chars (list-head input n)))
      (if (eq? (length chars) (char-set-size (list->char-set chars)))
          idx
          (loop (cdr input) (1+ idx))))))


(display "Part 1: ")
(display (solve 4))
(newline)
(display "Part 2: ")
(display (solve 14))
(newline)
