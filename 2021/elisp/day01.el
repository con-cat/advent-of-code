(defun current-word-as-number ()
  (string-to-number (thing-at-point 'word 'no-properties)))

(defun day1-part1 ()
  (with-temp-buffer
    (insert-file-contents "../input/day01.txt")
    (goto-char (point-min))
    (set 'increase-count 0)
    (set 'prev-number (current-word-as-number))
    (while (not (eobp))
      (set 'current-number (current-word-as-number))
      (when (> current-number prev-number)
        (set 'increase-count (1+ increase-count)))
      (set 'prev-number current-number)
      (forward-line 1)))
  (message "Part 1 result: %d" increase-count))

(setq debug-on-error t)
(day1-part1)
