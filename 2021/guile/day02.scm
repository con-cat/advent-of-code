(use-modules
 (ice-9 rdelim)
 (srfi srfi-1)
 (srfi srfi-42)
 (srfi srfi-41))


(define (get-lines proc filename)
  (call-with-input-file filename
    (lambda (port)
      (let loop ((lines '()))
        (let ((line (read-line port)))
          (if (eof-object? line)
              lines
              (loop (append lines (list (proc line))))))))))

(define (process-line line)
  (let ((split (string-split line #\space)))
    (cons (car split) (string->number (cadr split)))))

(define input (get-lines process-line "/Users/caitlinwhite/src/advent-of-code/2021/input/day02.txt"))

;; PART 1
(define x 0)
(define y 0)

(define (part-1)
  (let loop ((directions input))
    (cond ((null? directions)
           (* x y))
          ((string=? (caar directions) "forward")
            (set! x (+ x (cdar directions)))
            (loop (cdr directions)))
          ((string=? (caar directions) "up")
            (set! y (- y (cdar directions)))
            (loop (cdr directions)))
          ((string=? (caar directions) "down")
            (set! y (+ y (cdar directions)))
            (loop (cdr directions))))))

(part-1)
