(add-to-load-path (dirname (current-filename)))
(use-modules
 (helpers)
 (srfi srfi-41)
 (srfi srfi-69))

(define input (stream-map split-on-space (file->stream-lines "../input/day02.txt")))

;; Strings to moves
(define moves (make-hash-table string=?))
(hash-table-set! moves "A" 'rock)
(hash-table-set! moves "B" 'paper)
(hash-table-set! moves "C" 'scissors)
(hash-table-set! moves "X" 'rock)
(hash-table-set! moves "Y" 'paper)
(hash-table-set! moves "Z" 'scissors)

;; Moves to scores
(define scores (make-hash-table))
(hash-table-set! scores 'rock 1)
(hash-table-set! scores 'paper 2)
(hash-table-set! scores 'scissors 3)

(define (my-score input)
  (hash-table-ref scores (cadr (stream-car input))))

;; Which move defeats which?
(define defeats (make-hash-table))
(hash-table-set! defeats 'rock 'scissors)
(hash-table-set! defeats 'scissors 'paper)
(hash-table-set! defeats 'paper 'rock)

(define (losing-move m) ;; E.g. scissors for rock
  (hash-table-ref defeats m))

(define (draw? pair)
  (eq? (car pair) (cadr pair)))

(define (i-win? pair)
  (eq? (losing-move (cadr pair)) (car pair)))

;; Solutions
(define (part-1-moves pair)
  (map (lambda (s) (hash-table-ref moves s)) pair))

(define (part-2-moves p)
  (let ((their-move (hash-table-ref moves (car p)))
        (result (cadr p)))
    (cond ((string=? result "Y") ;; Draw
           (list their-move their-move))
          ((string=? result "X") ;; They win
           (list their-move (losing-move their-move)))
          (else ;; I win
           (list their-move (losing-move (losing-move their-move)))))))

(define (solve proc)
  (let loop ((input (stream-map proc input)) (score 0))
    (cond ((stream-null? input)
           score)
          ((draw? (stream-car input))
           (loop (stream-cdr input) (+ score 3 (my-score input))))
          ((i-win? (stream-car input))
           (loop (stream-cdr input) (+ score 6 (my-score input))))
          (else
           (loop (stream-cdr input) (+ score (my-score input)))))))

(display "Part 1: ")
(display (solve part-1-moves))
(newline)
(display "Part 2: ")
(display (solve part-2-moves))
(newline)
