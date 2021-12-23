(use-modules (ice-9 textual-ports) (srfi srfi-1) (ice-9 common-list))

(define input (string-split (call-with-input-file "../input/day04.txt" get-string-all) #\newline))

;; Get numbers from the first row of the input
(define numbers (map string->number (string-split (list-ref input 0) #\,)))

;; Convert an input board line to a list of numbers
(define (get-board-line line) (map string->number (delete "" (string-split line #\space))))

;; Get bingo boards as a three-dimensional array of numbers
(define board-list
  (let loop ((l (list-tail input 2)) (board '()) (result '()))
    (if (null? l)
        result
        (if (string-null? (car l))
            (loop (cdr l) '() (append result (list board)))
            (loop (cdr l) (append board (list (get-board-line (car l)))) result)))))

(define (mark-line line nums)
  (map (lambda (item) (list item (list? (member item nums)))) line))

(define (mark-board board nums)
  (map (lambda (line) (mark-line line nums)) board))

(define (all lst)
  (or (null? lst)
      (and (car lst)
           (all (cdr lst)))))

(define (row-bingo? row)
  (all (map (lambda (item) (list-ref item 1)) row)))

(define (true-at-index line index)
  (if (>= index (length line))
      #f
      (let ((item (list-ref line index)))
        (if (list? item)
            (list-ref item 1)
            #f))))

(define (column-bingo? marked-board)
  (if (null? marked-board)
      #f
      (let loop ((i 0))
        (if (> i 5)
            #f
            (if (all (map (lambda (line) (true-at-index line i)) marked-board))
                #t
                (loop (+ 1 i)))))))


(define (board-bingo? marked-board)
  (if (null? marked-board)
      #f
      (if (column-bingo? marked-board)
          #t
          (let loop ((b marked-board))
            (if (null? b)
                #f
                (if (row-bingo? (car b))
                    #t
                    (loop (cdr b))))))))

(define (not-bingo? marked-board)
  (if (board-bingo? marked-board)
      #f
      #t))

(define (sum-marked-row row)
  (if (null? row)
      0
      (if (list-ref (car row) 1)
          (+ 0 (sum-marked-row (cdr row)))
          (+ (list-ref (car row) 0) (sum-marked-row (cdr row))))))

(define (sum-marked-board board)
  (if (null? board)
      0
      (+ (sum-marked-row (car board)) (sum-marked-board (cdr board)))))

(define (draw-number-part-1 i)
  (let loop ((b board-list) (nums (list-head numbers i)))
    (if (null? b)
        '()
          (let ((marked-board (mark-board (car b) nums)))
            (if (board-bingo? marked-board)
                (* (last nums) (sum-marked-board marked-board))
                (loop (cdr b) nums))))))

(define (part-1)
  (let loop ((i 1))
    (if (> i (length numbers))
        0
        (let ((result (draw-number-part-1 i)))
          (if (null? result)
              (loop (1+ i))
              result)))))

(define (draw-number-part-2 i)
  (let ((nums (list-head numbers i)))
  (let ((boards (map (lambda (board) (mark-board board nums)) board-list)))
    (if (eq? 1 (count not-bingo? boards))
        (list-ref board-list (list-index not-bingo? boards))
        '()))))

(define (part-2)
  (let loop ((i 1))
    (if (> i (length numbers))
        0
        (let ((board (draw-number-part-2 i)))
          (if (null? board)
              (loop (1+ i))
              ;; We have the final board, now we need to keep marking it until it bingos and do the final calculation
              (let final-loop ((j (1+ i)))
                (let ((marked-board (mark-board board (list-head numbers j))))
                  (if (board-bingo? marked-board)
                      (* (sum-marked-board marked-board) (list-ref numbers (- j 1)))
                      (final-loop (1+ j))))))))))


(part-2)
