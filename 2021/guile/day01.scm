(use-modules
 (ice-9 rdelim)
 (srfi srfi-1)
 (srfi srfi-42)
 (srfi srfi-41))


(define (get-lines proc)
  (call-with-input-file "/Users/caitlinwhite/src/advent-of-code/2021/input/day01.txt"
    (lambda (port)
      (let loop ((lines '()))
        (let ((line (read-line port)))
          (if (eof-object? line)
              lines
              (loop (append lines (list (proc line))))))))))

;; PART 1
(define increase-count 0)
(define (part-1)
  (let loop ((nums (get-lines string->number)))
    (unless (null? (cdr nums))
      (when (< (car nums) (cadr nums))
        (set! increase-count (1+ increase-count)))
      (loop (cdr nums))
    increase-count)))


;; PART 2
(define (sum-window nums)
  ;; Sum the first three numbers in a list of numbers
  ;; unless it's less than three numbers long
  (if (or
           (null? (cdr nums))
           (null? (cddr nums))
           (null? (cddr nums)))
      0
      (+ (car nums) (cadr nums) (caddr nums))))

(define increase-count 0)
(define (part-2)
  (let loop ((nums (get-lines string->number)))
    (unless (null? (cdr nums))
      (when (< (sum-window nums) (sum-window (cdr nums)))
        (set! increase-count (1+ increase-count)))
      (loop (cdr nums))
    increase-count)))

(part-2)
