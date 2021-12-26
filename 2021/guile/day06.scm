(use-modules (srfi srfi-1))

(define initial-fish (map string->number (string-split "3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,1,4,1,1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,3,1,4,1,1,1,1,1,4,5,1,1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3" #\,)))

(define (age-fish fish)
  ;; Take a fish, apply 1 day of aging to it
  (if (eq? fish 0)
      6
      (1- fish)))

(define (create-fish fish-list)
  ;; Count the number of zeros in the list, and return a list of 8s of the same length
  (let ((num-fish (length (lset-intersection eqv? fish-list '(0)))))
    (make-list num-fish 8)))

(define (increment-day fish-list)
  ;; Take a list of fish, age them and create new fish
  (append (map age-fish fish-list) (create-fish fish-list)))

(define (part-1 fish-list num-days)
  (let loop ((day 0) (fish fish-list))
    (if (eq? day num-days)
        (length fish)
        (loop (1+ day) (increment-day fish)))))

(part-1 initial-fish 80)
