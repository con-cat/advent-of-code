(require 'cl-lib)

(defun current-word ()
  (thing-at-point 'word 'no-properties))

(defun get-line-count ()
  (count-lines (point-min) (point-max)))

(defun word-to-int-sequence ()
  (mapcar 'string-to-number (mapcar 'string (current-word))))

(defun get-most-common-bit (num)
  (if (> num (/ (line-count) 2))
    1
    0))

(defun bit-list-to-int (bit-list)
  (string-to-number (mapconcat 'number-to-string bit-list "") 2))

(defun get-byte-counts ()
  (goto-char (point-min))
  (set 'byte-counts (make-list (length (current-word)) 0))
  (while (not (eobp))
    (set 'byte-counts (cl-mapcar '+ (word-to-int-sequence) byte-counts))
    (forward-line 1))
  byte-counts)

(defun day3-part1 ()
  (with-temp-buffer
    (insert-file-contents "../input/day03.txt")
    (setq byte-counts (get-byte-counts))
    (setq line-count (get-line-count))
    (setq gamma-rate (mapcar 'get-most-common-bit byte-counts))
    (setq epsilon-rate (mapcar (lambda (num) (if (= num 1) 0 1)) gamma-rate))
    (* (bit-list-to-int gamma-rate) (bit-list-to-int epsilon-rate))))

(defun day3-part2 ()
  (with-temp-buffer
    (insert-file-contents "../input/day03.txt")
    (setq byte-counts (get-byte-counts))
    (setq most-common-bits (mapcar 'number-to-string (mapcar 'get-most-common-bit byte-counts)))
    (goto-char (point-min))
    (while (not 'eopb)
      (if (string= (elt most-common-bits 0) (elt (mapcar 'string (current-word)) 0))
          (forward-line-1)
        (kill-whole-line)))
    (get-line-count)))


(setq debug-on-error t)
(message "Part 1 result: %s" (day3-part1))
(message "Part 2 result: %s" (day3-part2))
