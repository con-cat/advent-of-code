(use-modules
 (ice-9 textual-ports)
 (ice-9 common-list)
 (ice-9 string-fun)
 (srfi srfi-42)
 (srfi srfi-1))

;; Helper functions for converting input text to lists of two coordinates

(define (string->coord str)
  ;; Convert a string like "1,2" to a list of numbers like (1 2)
  (if (string-null? str)
      '()
      (let ((nums (string-split str #\,)))
        (map string->number nums))))

(define (string->vec2 line)
  ;; Convert a line of the input to a 'vec2', i.e. a list two x y coordinates
  (if (string-null? line)
      #nil
      (let ((split-line (string-split line #\space)))
        (let ((parts (list (list-ref split-line 0) (list-ref split-line 2))))
          (map string->coord parts)))))

;; Helper functions for dealing with 2D vectors and coordinates

(define (min-at-index vec2 i)
  ;; Return the minimum value at the specified index of both points of a vec2
  (min (list-ref (list-ref vec2 0) i) (list-ref (list-ref vec2 1) i)))

(define (max-at-index vec2 i)
  ;; Return the maximum value at the specified index of both points of a vec2
  (max (list-ref (list-ref vec2 0) i) (list-ref (list-ref vec2 1) i)))

(define (same-at-index? vec2 i)
  ;; Return whether a vec2's values at the specified index are duplicate
  (eq? (list-ref (list-ref vec2 0) i) (list-ref (list-ref vec2 1) i)))

(define (coord1+ coord)
  ;; Add 1 to both the x and y value of a coord
  (list (1+ (first coord)) (1+ (last coord))))

(define (coord<? coord-1 coord-2)
  ;; Is the first coord less than the second?
  (if (eq? (list-ref coord-1 0) (list-ref coord-2 0))
      (< (list-ref coord-1 1) (list-ref coord-2 1))
      (< (list-ref coord-1 0) (list-ref coord-2 0))))

(define (coord-eq? coord-1 coord-2)
  ;; Are two coordinates equal?
  (and? (eq? (first coord-1) (first coord-2)) (eq? (last coord-1) (last coord-2))))

(define (min-coord vec2)
  (if (coord<? (first vec2) (last vec2))
      (first vec2)
      (last vec2)))

(define (max-coord vec2)
  (if (coord<? (first vec2) (last vec2))
      (last vec2)
      (first vec2)))

(define (vec2->coords vec2 include-diagonals?)
  ;; Take a vec2, and return a list of all of the (x y) coordinates it covers
  (cond ((same-at-index? vec2 0)
         ;; It's a horizontal vector
         (let ((x (first (car vec2))))
           (list-ec (: y (min-at-index vec2 1) (1+ (max-at-index vec2 1))) (list x y))))
        ((same-at-index? vec2 1)
        ;; It's a vertical vector?
         (let ((y (last (car vec2))))
           (list-ec (: x (min-at-index vec2 0) (1+ (max-at-index vec2 0))) (list x y))))
        (include-diagonals?
         ;; It's a diagonal, calculate it if we're including them
         (let ((x-vals (list-ec (: x (min-at-index vec2 0) (1+ (max-at-index vec2 0))) x))
               (y-vals (list-ec (: y (min-at-index vec2 1) (1+ (max-at-index vec2 1))) y)))
           (zip
            (if (> (first (first vec2)) (min-at-index vec2 0))
                (reverse x-vals)
                x-vals)
            (if (> (last (first vec2)) (min-at-index vec2 1))
                (reverse y-vals)
                y-vals))))
        (else
         ;; Disregard the item
         '())))


(define (find-adjacent-duplicates coord-lst)
  ;; Return a list of unique duplicates from a sorted list of coordinates
  (let loop ((lst coord-lst) (result '()))
    (cond ((null? (cdr lst))
           result)
          ((coord-eq? (car lst) (car (cdr lst)))
           (loop (cdr lst) (lset-adjoin coord-eq? result (car lst))))
          (else
           (loop (cdr lst) result)))))

(define (flatten lst)
  ;; Flatten a three-dimensional list into a two-dimensional list
  (let loop ((lst lst) (acc '()))
    (if (null? lst)
        acc
        (loop (cdr lst) (fold cons acc (car lst))))))

;; Set up the input data

(define input-lines
  ;; Return the input file as a list of strings
  (string-split
   (sans-final-newline (call-with-input-file "../input/day05.txt" get-string-all))
   #\newline))


(define (part-1)
  (let ((coords
         ;; Get a list of all of the unique coordinates covered by the horizontal vectors defined in the input
         (sort-list
          (remove null?
                  (flatten (map (lambda (line) (vec2->coords (string->vec2 line) #f))
                                input-lines))) coord<?)))
    (length (find-adjacent-duplicates coords))))

(define (part-2)
  (let ((coords
         ;; As above, but include diagonals
         (sort-list
          (remove null?
                  (flatten (map (lambda (line) (vec2->coords (string->vec2 line) #t))
                                input-lines))) coord<?)))
    (length (find-adjacent-duplicates coords))))
