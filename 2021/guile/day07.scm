(use-modules
 (ice-9 rdelim)
 (srfi srfi-42))

(define (get-initial-positions)
  (call-with-input-file "../input/day07.txt"
    (lambda (port)
      (let loop ((nums '()))
        (let ((num (read-delimited ",\n" port)))
          (if (eof-object? num)
              nums
              (loop (append nums (list (string->number num))))))))))

(define (calculate-fuel-part-1 lst pos)
  (apply + (map (lambda (i) (abs (- pos i))) lst)))

(define (calculate-fuel-part-2 lst pos)
  (apply + (map
            (lambda (i)
              (let ((steps (abs (- pos i))))
                (/ (* steps (1+ steps)) 2)))
            lst)))

(define (calculate-minimum-fuel lst proc)
  (let ((fuel-calcs (list-ec (: i (1+ (apply max lst))) (proc lst i))))
    (apply min fuel-calcs)))

(calculate-minimum-fuel (get-initial-positions) calculate-fuel-part-2)
