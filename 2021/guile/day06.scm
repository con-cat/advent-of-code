(use-modules (srfi srfi-1) (srfi srfi-42))

(define initial-fish (map string->number (string-split "3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,1,4,1,1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,3,1,4,1,1,1,1,1,4,5,1,1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3" #\,)))

;; PART 1

(define (age-fish fish)
  ;; Take a fish, apply 1 day of aging to it
  (if (eq? fish 0)
      6
      (1- fish)))

(define (create-new-fish fish-list)
  ;; Count the number of zeros in the list, and return a list of 8s of the same length
  (let ((num-fish (length (lset-intersection eqv? fish-list '(0)))))
    (make-list num-fish 8)))

(define (increment-day fish-list)
  ;; Take a list of fish, age them and create new fish
  (let ((new-fish (create-new-fish fish-list)))
    (append! (map! age-fish fish-list) new-fish)))

(define (part-1 fish-list num-days)
  (let loop ((day 0) (fish fish-list))
    (if (eq? day num-days)
        (length fish)
        (loop (1+ day) (increment-day fish)))))

;; PART 2 - with a hashmap

(define (initialise-fish-hash fish-list)
  ;; Populate our hash with the initial count of each number from the fish list
  (let loop ((num 0))
    (unless (eq? num 9)
      (let ((fish-count (length (filter (lambda (f) (eq? f num)) fish-list))))
        (hashq-set! fish-hash num fish-count)
        (loop (1+ num))))))

(define (age-fish-hash-1-day)
  (let ((current (hash-map->list cons fish-hash)))
    (hashq-set! fish-hash 8 (assq-ref current 0))
    (hashq-set! fish-hash 0 (assq-ref current 1))
    (hashq-set! fish-hash 1 (assq-ref current 2))
    (hashq-set! fish-hash 2 (assq-ref current 3))
    (hashq-set! fish-hash 3 (assq-ref current 4))
    (hashq-set! fish-hash 4 (assq-ref current 5))
    (hashq-set! fish-hash 5 (assq-ref current 6))
    (hashq-set! fish-hash 6 (+ (assq-ref current 0) (assq-ref current 7)))
    (hashq-set! fish-hash 7 (assq-ref current 8))))

(define (count-fish)
  ;; Return the number of fish represented by our hash
  (apply + (map (lambda (i) (cdr i)) (hash-map->list cons fish-hash))))

(define (part-2 num-days)
  (let loop ((num 0))
    (unless (eq? num num-days)
      (age-fish-hash-1-day)
      (loop (1+ num)))
    (count-fish)))

(define fish-hash (make-hash-table 9))
(initialise-fish-hash initial-fish)
(part-2 256)
