(use-modules (ice-9 rdelim))

(define (parse-input)
  ;; Return a list of lists of signal patterns and output values
  (call-with-input-file "../input/day08.txt"
    (lambda (port)
      (let loop ((data '()))
        (let ((line (read-line port)))
          (if (eof-object? line)
              data
              (let ((parts (string-split line #\|)))
                (loop (cons
                       (list
                        (string-split (string-trim-right (car parts)) #\space)
                        (string-split (string-trim (car (cdr parts))) #\space))
                       data)))))))))

(define (easy-digit? str)
  (let ((len (string-length str)))
    (or (eq? len 2) (eq? len 3) (eq? len 7) (eq? len 4))))

(define (count-easy-digits item)
  (let ((output (list-ref item 1)))
    (length (filter (lambda (i) (easy-digit? i)) output))))

(define (part-1 lst)
  (apply + (map count-easy-digits lst)))
