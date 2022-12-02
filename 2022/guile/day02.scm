(add-to-load-path (dirname (current-filename)))
(use-modules
 (helpers)
 (srfi srfi-1)
 (srfi srfi-41)
 (srfi srfi-69))

(define input (stream-map split-on-space (file->stream-lines "../input/day02.txt")))

;; Strings to moves
(define moves (make-hash-table string=?))
(hash-table-set! moves "A" 1) ;; rock
(hash-table-set! moves "B" 2) ;; paper
(hash-table-set! moves "C" 3) ;; scissors
(hash-table-set! moves "X" 1) ;; rock
(hash-table-set! moves "Y" 2) ;; paper
(hash-table-set! moves "Z" 3) ;; scissors

(define wins (circular-list 1 2 3)) ;; Item defeated by next item

(define (winning-move move)
  (cadr (find-tail (lambda (x) (eq? move x)) wins)))

(define (losing-move move)
  (winning-move (winning-move move)))

(define (i-win? moves)
  (eq? (cadr moves) (winning-move (car moves))))

;; Solutions
(define (parse-part-1 line)
  (map (lambda (s) (hash-table-ref moves s)) line))

(define (part-1)
  (let loop ((input (stream-map parse-part-1 input)) (score 0))
    (if (stream-null? input)
        score
        (let ((my-score (cadr (stream-car input))))
            (cond ((stream-null? input)
                score)
                ((apply eq? (stream-car input)) ;; Draw
                (loop (stream-cdr input) (+ score 3 my-score)))
                ((i-win? (stream-car input)) ;; I win
                (loop (stream-cdr input) (+ score 6 my-score)))
                (else ;; They win
                (loop (stream-cdr input) (+ score my-score))))))))

(define (parse-part-2 line)
  (cons (hash-table-ref moves (car line)) (cadr line)))

(define (part-2)
  (let loop ((input (stream-map parse-part-2 input)) (score 0))
    (if (stream-null? input)
        score
        (let ((my-move (cdr (stream-car input)))
              (their-move (car (stream-car input))))
          (cond ((string=? my-move "Y") ;; draw
                 (loop (stream-cdr input) (+ score their-move 3)))
                ((string=? my-move "Z") ;; I win
                 (loop (stream-cdr input) (+ score (winning-move their-move) 6)))
                (else ;; they win
                 (loop (stream-cdr input) (+ score (losing-move their-move)))))))))

(display "Part 1: ")
(display (part-1))
(newline)
(display "Part 2: ")
(display (part-2))
(newline)
