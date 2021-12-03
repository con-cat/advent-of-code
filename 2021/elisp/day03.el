(require 'cl-lib)

(defun current-word ()
  (thing-at-point 'word 'no-properties))

(defun word-to-int-sequence ()
  (mapcar 'string-to-number (mapcar 'string (current-word))))

(defun get-gamma-rate (count)
  (if (> count (/ (count-lines (point-min) (point-max)) 2))
    1
    0))

(defun bit-list-to-int (bit-list)
  (string-to-number (mapconcat 'number-to-string bit-list "") 2))


(defun day3-part1 ()
  (with-temp-buffer
    (insert-file-contents "../input/day03.txt")
    (goto-char (point-min))
    (setq byte-counts (make-list (length (current-word)) 0))
    (while (not (eobp))
      (setq byte-counts (cl-mapcar '+ (word-to-int-sequence) byte-counts))
      (forward-line 1))

    (setq gamma-rate (mapcar 'get-gamma-rate byte-counts))
    (setq epsilon-rate (mapcar (lambda (num) (if (= num 1) 0 1)) gamma-rate))
    (* (bit-list-to-int gamma-rate) (bit-list-to-int epsilon-rate))))


(setq debug-on-error t)
(message "Part 1 result: %s" (day3-part1))
