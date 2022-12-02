(define-module (helpers)
  #:use-module (srfi srfi-41)
  #:use-module (ice-9 rdelim)
  #:export (file->stream-lines split-on-space))


(define-stream (file->stream-lines filename)
  ;; Stream a file line by line
  (let ((p (open-input-file filename)))
    (stream-let loop ((l (read-line p)))
                (if (eof-object? l)
                    (begin (close-input-port p)
                           stream-null)
                    (stream-cons l
                                 (loop (read-line p)))))))

(define split-on-space (lambda (s) (string-split s #\space)))
