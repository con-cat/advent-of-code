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

(define (part-1)
  (let ((x 0) (y 0))
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
             (loop (cdr directions)))))))

;; PART 2

(define (part-2)
  (let ((x 0) (y 0) (aim 0))
    (let loop ((directions input))
      (cond ((null? directions)
             (* x y))
            ((string=? (caar directions) "forward")
             (set! x (+ x (cdar directions)))
             (set! y (+ y (* aim (cdar directions))))
             (loop (cdr directions)))
            ((string=? (caar directions) "up")
             (set! aim (- aim (cdar directions)))
             (loop (cdr directions)))
            ((string=? (caar directions) "down")
             (set! aim (+ aim (cdar directions)))
             (loop (cdr directions)))))))


(part-2)
