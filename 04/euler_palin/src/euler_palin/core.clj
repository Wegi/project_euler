(ns euler-palin.core)

(defn palindrome? [x] (= (reverse (str x)) (seq(str x))))

(defn biggest3 []
  (reduce max (for [x (range 100 1000) y (range 100 1000) :when (palindrome? (* x y))]
                   (* x y))))